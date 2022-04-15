from src.db_client import DB_Client

# DB USER fetch TESTS
def test_dbGetNameByID():
    newDB = DB_Client(True, "Jobs","users")
    names = []
    try:
        for i in range(3):
            names.append(newDB.get_name_by_id(i))
        print(names)
        assert len(names) == 3
    except:
        assert False