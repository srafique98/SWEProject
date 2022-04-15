from src.db_client import DB_Client

# JOB db tests
def test_dbConnectionJobs():
    newDB = DB_Client(True, "Jobs","NewJobs")
    return newDB.intitialized

def test_dbConnectionUsers():
    newDB = DB_Client(True, "Jobs","users")
    return newDB.intitialized