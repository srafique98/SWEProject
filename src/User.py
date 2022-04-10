import socket
from datetime import datetime
from src.db_client import DB_Client


class User:
    """Generic placeholder for user interactive class"""
    signed_in = False
    profile_info = {
        "username" : None,
        "email" : None,
        "account_lvl" : None,
        "last_logged" : None,
        "ip" : None,
        "host_address" : None
    }

    def __init__(self):
        self.profile_info["host_addres"] = socket.gethostname()
        self.profile_info["ip"] = socket.gethostbyname(self.profile_info["host_address"])
        self.profile_info["last_logged"] = datetime.now()

    def login(email,pw):
        new_db = DB_Client(True,"Jobs","users")
        # to be continued
