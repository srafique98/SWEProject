from db_client import DB_Client

def test_first():
    return True

def test_db_connection():
    newDB = DB_Client(True)
    return newDB.intitialized

def test_db_location_filter():
    newDB = DB_Client(True)
    try:
        newDB.fil_location("Berkeley")
        return True
    except:
        return False

def test_db_profession_filter():
    newDB = DB_Client(True)
    try:
        newDB.fil_sect_profession("Engineer")
        return True
    except:
        return False 