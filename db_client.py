import pymongo
import certifi

class DB_Client:
    dbPassword = None
    CONNECT_STRING = None
    clientConnection = None
    dbName = None
    dbCollection = None
    intitialized = False
    
    def __init__(self, initialized):
        self.dbPassword = "trx9bsx2oGhtz4DJ"
        self.CONNECT_STRING = "mongodb+srv://root:"+self.dbPassword+"@cluster0.ehbu1.mongodb.net/Jobs?retryWrites=true&w=majority"
        self.clientConnection = pymongo.MongoClient(self.CONNECT_STRING, tlsCAFile=certifi.where())
        self.dbName = self.clientConnection["Jobs"]
        self.dbCollection = self.dbName["NewJobs"]
        self.intitialized = initialized

    def fil_location(self,in_str):
        loc_query = {"location" : {"$regex":in_str}}
        fil_document = self.dbCollection.find(loc_query)
        return fil_document

    def fil_sect_profession(self,in_str):
        loc_query = {"job_title" : {"$regex":in_str}}
        fil_document = self.dbCollection.find(loc_query)
        return fil_document
