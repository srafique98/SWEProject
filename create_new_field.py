from src.User import User
from src.db_client import DB_Client

users_or_new_jobs = str(input("pick a colleciton: \n   1 - user\n   2 - NewJobs\n >> "))

field_name = input("Enter the name of the field you want to create(use underscores[_] for spaces): ")

if users_or_new_jobs == "1":
    new_cil = DB_Client(True, "Jobs", "users")
else:
    new_cil = DB_Client(True, "Jobs", "NewJobsPrt3")

new_cil.create_new_document_field(field_name)
