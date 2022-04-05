from db_client import DB_Client

def test_first():
    return True

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

def test_dbGetNameByID():
    newDB = newDB = DB_Client(True, "Jobs","users")
    names = []
    try:
        for i in range(3):
            names.append(newDB.get_name_by_id(i))
        print(names)
        return True
    except:
        return False
#def test_windowInit():
#    testFile = "../ui/mainmenu.ui"
#    try:
#        app = QApplication(sys.argv)
#        testWindow = Menu()
#        testWindow.windowInit(testFile)
#        return True
#    except SystemExit:
#        return False
