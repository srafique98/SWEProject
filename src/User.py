from dataclasses import field
import socket
import src.db_client as db_cli
from datetime import datetime


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
        local_hostname = socket.gethostname()
        self.profile_info["host_addres"] = local_hostname
        self.profile_info["ip"] = socket.gethostbyname(local_hostname)
        self.profile_info["last_logged"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def validateUserLogin(self, email, pw):
        db_obj = db_cli.DB_Client(True,"Jobs","users")
        doc_cursor = db_obj.get_all_users()

        for usr_doc in doc_cursor:
            if usr_doc["email"] == email and usr_doc["Password"] == pw:
                self.profile_info["email"] = usr_doc["email"]
                self.profile_info["username"] = usr_doc["email"]
                self.profile_info["u_id"] = usr_doc["u_id"]
                self.profile_info["fullname"] = usr_doc["first_name"] + " " + usr_doc["last_name"]
                
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
        user_insert = {"u_id":high+1, "first_name":f_name, "last_name":l_name,"email":email,"Password":pw}
        db_obj.dbCollection.insert_one(user_insert)

#   *****************************************
