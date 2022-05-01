from dataclasses import field
import socket
import src.db_client as db_cli
from datetime import datetime
import base64

# NOTES (updated Wed Apr 27, 2022) 
#   jobs_client and users_client have been created and initialized in the
#   User constructor to reduce load times and the number of active db clients

uso = "User not signed in! Error running: " # error message string for console read-out

class User:
    signed_in = False
    profile_info = {
        "username" : None,
        "email" : None,
        "account_lvl" : None,
        "last_logged" : None,
        "ip" : None,
        "host_address" : None,
        "u_id": None,
        "fullname" : None
    }
    # db connections
    jobs_client = None
    users_client = None

    def __init__(self):
        try:
            #   gather ip/date/time infromation about the copmuter trying to sign-in
            local_hostname = socket.gethostname()
            self.profile_info["host_addres"] = local_hostname
            self.profile_info["ip"] = socket.gethostbyname(local_hostname)
        except:
            print("Unable to get hostname or ip address")
        
        try: # attempt to initialize connections to the database
            self.jobs_client = db_cli.DB_Client(True,"Jobs","NewJobsPrt3")
            self.users_client = db_cli.DB_Client(True,"Jobs","users")
        except:
            print("Unable to initialize DB_Client objects")
        self.profile_info["last_logged"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

#   *****************************************

#   SIGN IN and VALIDATE USER
#       (email) email associated with the user in the db
#       (pw) password associated with the user in the db
    def validateUserLogin(self, email, pw):
        doc_cursor = self.users_client.get_all_users()
        for usr_doc in doc_cursor:
            if usr_doc["email"] == email and usr_doc["Password"] == pw:
                self.profile_info["email"] = usr_doc["email"]
                self.profile_info["username"] = usr_doc["email"]
                self.profile_info["u_id"] = usr_doc["u_id"]
                self.profile_info["fullname"] = usr_doc["first_name"] + " " + usr_doc["last_name"]
                user_query = {"u_id":self.profile_info["u_id"]}
                user_insert = ({"$set":{"date_last_signin":self.profile_info["last_logged"]}},{"$set":{"last_ip":self.profile_info["ip"]}},{"$set":{"ip_hostname":self.profile_info["host_address"]}})
                for db_insert in user_insert:
                    self.users_client.dbCollection.update_one(user_query,db_insert)
                self.signed_in = True
                return True
        return False    
        
#   *****************************************
# SIGN UP 

#User creation
#   user_1 = User()
#signup ex
#                   email               paswword        firstname lastname
# user_1.signUp("fake_email@uop.net","sonicthehedgehog","Doctor","Eggman")

    def signUp(self, email, pw, f_name, l_name):
        largest_u_id = self.users_client.dbCollection.find().sort("u_id",-1).limit(1)
        high = None
        for field in largest_u_id:
            high = field["u_id"]
        user_insert = {"u_id":high+1, "first_name":f_name, "last_name":l_name,"email":email,"Password":pw,"date_last_signin":self.profile_info["last_logged"],"last_ip":self.profile_info["ip"]}
        self.users_client.dbCollection.insert_one(user_insert)

#   *****************************************

# CHANGE USER SPECIFIC DATA
    # Pass in the 'field' that you want to change
    # Pass in the 'value' that you would like to change it to
    def changeUserData(self, field, value): # self, string, (int or string)
        if self.signed_in:
            user_query = {"u_id": self.profile_info["u_id"] }
            user_update = {"$set":{ field : value }}
            self.users_client.dbCollection.update_one(user_query, user_update)
            print("Changed " + self.profile_info["fullname"] + " " + field + " to " + ("*"*len(value)))
        else:
            print(uso + "User.changeUserData()")

#   QUERY USER SPECIFIC DATA
#       (field) string that is matched case w/ field value in a user document
    def getUserField(self, field):
        if self.signed_in:
            user_query = {"u_id": self.profile_info["u_id"] }
            db_cursor = self.users_client.dbCollection.find(user_query)
            field_value = None
            for doc in db_cursor:
                field_value = doc[field]
            print(field_value)
            return field_value
        else:
            print(uso + "User.getUserField()")
            return None

#   UPDATES PROFILE INFO TO REDUCE OVERALL DB WORK
    def updateLocalInfo(self):
        if self.signed_in:
            doc_cursor = self.users_client.get_user_by_id(int(self.profile_info["u_id"]))
            for doc in doc_cursor:
                self.profile_info["u_id"] = doc["u_id"]
                self.profile_info["fullname"] = doc["first_name"] + " " + doc["last_name"]
                self.profile_info["email"] = doc["email"]
            print("Updated user: "+ str(self.profile_info["u_id"]))
            print(self.profile_info)
        else:
            print(uso + "User.updateLocalInfo()")


#   UPLOAD RESUME TO USER DOCUMENT
#       (FILE_PATH) string that defines the filepath and filename of the resume the user is going to upload   
    def uploadResume(self, FILE_PATH):
        if self.signed_in:
            #   encode reusme as b64 string
            with open(FILE_PATH,"rb") as pdf_file:
                encoded_string = base64.b64encode(pdf_file.read())  
            user_query = {"u_id": self.profile_info["u_id"] }
            user_update = {"$set":{ "resume" : encoded_string }}
            #   push encoded string to user 'resume' field
            self.users_client.dbCollection.update_one(user_query, user_update)
            print("Uploaded resume for " + self.profile_info["fullname"])
        else:
            print(uso + "User.uploadResume()")

#   UPLOAD COVER LETTER TO USER DOCUMENT 
#       (FILE_PATH) string that defines the filepath and filename of the cover-letter the user is going to upload  
    def uploadLetter(self, FILE_PATH):
        if self.signed_in:
            with open(FILE_PATH,"rb") as pdf_file:
                encoded_string = base64.b64encode(pdf_file.read())    
            user_query = {"u_id": self.profile_info["u_id"] }
            user_update = {"$set":{ "cover_letter" : encoded_string }}
            self.users_client.dbCollection.update_one(user_query, user_update)
            print("Uploaded letter for " + self.profile_info["fullname"])
        else:
            print(uso + "User.uploadLetter()")

#   DOWNLOAD USER RESUME TO A DIRECTORY
#       (DIRECTORY PATH) string that defines the filepath where the user would like to store the downloaded resume 
    def downloadResume(self, DIRECTORY_PATH):
        if self.signed_in:
            user_query = {"u_id": self.profile_info["u_id"]}
            user_doc_cursor = self.users_client.dbCollection.find_one(user_query)
            byte_string = None
            for x in user_doc_cursor:
                byte_string = x["resume"]
            #   write to file as pdf_download.pdf
            with open(DIRECTORY_PATH+"pdf_download.pdf","wb") as f:
                f.write(byte_string) 
        else:
            print(uso + "User.downloadResume()")  

#   APPLY A USER TO A SPECIFIC JOB
#       (job_id) '_id' field string that is specific to each job in the db
    def applyForJob(self, job_id): 
        # job_id is a string in NewJobsPrt2 this would be '_id' field
        # when clicking quick apply the job should be queried so the _id
        # field should be accessable. This must be passed here so as to add the u_id 
        # of the user to the list field 'users_applied'
        if self.signed_in:
            my_id = self.profile_info["u_id"]
            job_query = {"_id":job_id}
            job_cursor = self.jobs_client.dbCollection.find(job_query)
            u_ids_to_check = None
            for x in job_cursor:
                u_ids_to_check = x["users_applied"]
            if u_ids_to_check is not None:
                if my_id not in u_ids_to_check:
                    self.jobs_client.dbCollection.update_one(job_query,{"$push":{"users_applied":my_id}})
                    print("added userID to job: " + job_id)
                else:
                    print("User hasalready applied")
            else:
                id_list = []
                id_list.append(my_id)
                self.jobs_client.dbCollection.update_one(job_query,{"$set":{"users_applied":id_list}})
                print("added userID to job: " + job_id)
        else:
            print(uso + "User.applyForJob()")


