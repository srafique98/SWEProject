from src.db_client import DB_Client

# JOB db tests
def test_dbConnectionJobs():
    newDB = DB_Client(True, "Jobs","NewJobs")
    assert newDB.initialized == True, "DB connection failed"

def test_dbConnectionUsers():
    newDB = DB_Client(True, "Jobs","users")
    assert newDB.initialized == True, "DB connection failed"