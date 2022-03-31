from src.db_client import DB_Client
from src.Window import Window


def test_first():
    return True


def test_dbConnection():
    newDB = DB_Client(True)
    return newDB.intitialized


def test_dbLocationFilter():
    newDB = DB_Client(True)
    try:
        newDB.fil_location("Berkeley")
        return True
    except:
        return False


def test_DbProfessionFilter():
    newDB = DB_Client(True)
    try:
        newDB.fil_sect_profession("Engineer")
        return True
    except:
        return False


def test_windowInit():
    testFile = "../ui/mainmenu.ui"

    try:
        testWindow = Window()
        testWindow.windowInit(testFile)
    except SystemExit:
        return False
