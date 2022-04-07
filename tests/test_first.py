from src.db_clientt import DB_Client

def test_first():
    return True

# JOB db tests
def test_dbConnectionJobs():
    newDB = DB_Client(True, "Jobs","NewJobs")
    return newDB.intitialized

def test_dbConnectionUsers():
    newDB = DB_Client(True, "Jobs","users")
    return newDB.intitialized

def test_dbLocationFilter():
    newDB = DB_Client(True, "Jobs","NewJobs")
    try:
        newDB.fil_location("Berkeley")
        return True
    except:
        return False


def test_DbProfessionFilter():
    newDB = DB_Client(True, "Jobs","NewJobs")
    try:
        newDB.fil_sect_profession("Engineer")
        return True
    except:
        return False


# DB USER fetch TESTS
def test_dbGetNameByID():
    newDB = DB_Client(True, "Jobs","users")
    names = []
    try:
        for i in range(3):
            names.append(newDB.get_name_by_id(i))
        print(names)
        return True
    except:
        return False
