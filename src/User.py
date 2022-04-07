import socket
import src.db_clientt as db_cli
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
        