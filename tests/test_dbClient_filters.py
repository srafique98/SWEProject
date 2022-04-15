from src.db_client import DB_Client

def test_dbLocationFilter():
    newDB = DB_Client(True, "Jobs","NewJobs")
    try:
        doc_cursor = newDB.fil_location("Berkeley")
        assert doc_cursor is not None
    except:
        assert False


def test_DbProfessionFilter():
    newDB = DB_Client(True, "Jobs","NewJobs")
    try:
        doc_cursor = newDB.fil_sect_profession("Engineer")
        assert doc_cursor is not None
    except:
        assert False
