from dataclasses import field
import socket
import src.db_client as db_cli
from datetime import datetime
from src.query_helper import usr_q_by_id
import base64

uso = "User not signed in! Error running: "

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

    def __init__(self):
        
        try:
            local_hostname = socket.gethostname()
            self.profile_info["host_addres"] = local_hostname
            self.profile_info["ip"] = socket.gethostbyname(local_hostname)
        except:
            print("Unable to get hostname or ip address")
        self.profile_info["last_logged"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

#   *****************************************

# SIGN IN
    def validateUserLogin(self, email, pw):
        db_obj = db_cli.DB_Client(True,"Jobs","users")
        doc_cursor = db_obj.get_all_users()

        for usr_doc in doc_cursor:
            if usr_doc["email"] == email and usr_doc["Password"] == pw:
                self.profile_info["email"] = usr_doc["email"]
                self.profile_info["username"] = usr_doc["email"]
                self.profile_info["u_id"] = usr_doc["u_id"]
                self.profile_info["fullname"] = usr_doc["first_name"] + " " + usr_doc["last_name"]
                user_query = {"u_id":self.profile_info["u_id"]}
                user_insert = ({"$set":{"date_last_signin":self.profile_info["last_logged"]}},{"$set":{"last_ip":self.profile_info["ip"]}},{"$set":{"ip_hostname":self.profile_info["host_address"]}})
                for db_insert in user_insert:
                    db_obj.dbCollection.update_one(user_query,db_insert)
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
        db_obj = db_cli.DB_Client(True,"Jobs","users")
        largest_u_id = db_obj.dbCollection.find().sort("u_id",-1).limit(1)
        high = None
        for field in largest_u_id:
            high = field["u_id"]
        user_insert = {"u_id":high+1, "first_name":f_name, "last_name":l_name,"email":email,"Password":pw,"date_last_signin":self.profile_info["last_logged"],"last_ip":self.profile_info["ip"]}
        db_obj.dbCollection.insert_one(user_insert)

#   *****************************************

# CHANGE USER SPECIFIC DATA
    # Pass in the 'field' that you want to change
    # Pass in the 'value' that you would like to change it to
    def changeUserData(self, field, value): # self, string, (int or string)
        if self.signed_in:
            db_obj = db_cli.DB_Client(True, "Jobs", "users")
            user_query = {"u_id": self.profile_info["u_id"] }
            user_update = {"$set":{ field : value }}
            db_obj.dbCollection.update_one(user_query, user_update)
            print("Changed " + self.profile_info["fullname"] + " " + field + " to " + ("*"*len(value)))
        else:
            print(uso + "User.changeUserData()")

# QUERY USER SPECIFIC DATA
    def getUserField(self, field):
        if self.signed_in:
            db_obj = db_cli.DB_Client(True, "Jobs", "users")
            user_query = {"u_id": self.profile_info["u_id"] }
            db_cursor = db_obj.dbCollection.find(user_query)
            field_value = None
            for doc in db_cursor:
                field_value = doc[field]
            print(field_value)
            return field_value
        else:
            print(uso + "User.getUserField()")
            return None

# repopulate local user info
    def updateLocalInfo(self):
        if self.signed_in:
            db_obj = db_cli.DB_Client(True,"Jobs","users")
            doc_cursor = db_obj.get_user_by_id(int(self.profile_info["u_id"]))
            for doc in doc_cursor:
                self.profile_info["u_id"] = doc["u_id"]
                self.profile_info["fullname"] = doc["first_name"] + " " + doc["last_name"]
                self.profile_info["email"] = doc["email"]
            print("Updated user: "+ str(self.profile_info["u_id"]))
            print(self.profile_info)
        else:
            print(uso + "User.updateLocalInfo()")
    
    def uploadResume(self, FILE_PATH):
        if self.signed_in:
            db_obj = db_cli.DB_Client(True,"Jobs","users")
            with open(FILE_PATH,"rb") as pdf_file:
                encoded_string = base64.b64encode(pdf_file.read())    
            user_query = {"u_id": self.profile_info["u_id"] }
            user_update = {"$set":{ "resume" : encoded_string }}
            db_obj.dbCollection.update_one(user_query, user_update)
            print("Uploaded resume for " + self.profile_info["fullname"])
        else:
            print(uso + "User.uploadResume()")

    def downloadResume(self, DIRECTORY):
        if self.signed_in:
            db_obj = db_cli.DB_Client(True,"Jobs","users")
            user_query = {"u_id": self.profile_info["u_id"]}
            user_doc_cursor = db_obj.dbCollection.find_one(user_query)
            byte_string = None
            for x in user_doc_cursor:
                byte_string = x["resume"]
            with open(DIRECTORY+"pdf_download.pdf","wb") as f:
                f.write(byte_string)   

