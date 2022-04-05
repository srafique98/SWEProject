from multiprocessing import connection


connection_strings = {
    "db_string" : "mongodb+srv://root:trx9bsx2oGhtz4DJ@cluster0.ehbu1.mongodb.net/Jobs?retryWrites=true&w=majority",
    "pw"        : "trx9bsx2oGhtz4DJ"
}
def get_connection_string():
    return connection_strings["db_string"]
def get_db_pw():
    return connection_strings["pw"]
