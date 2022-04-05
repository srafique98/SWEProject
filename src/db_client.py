import pymongo
import certifi
from . import db_library as dblib


class DB_Client:
    dbPassword = None
    CONNECT_STRING = None
    clientConnection = None
    dbName = None
    dbCollection = None
    intitialized = False

    def __init__(self, initialized, db_name, db_collection):
        self.dbPassword = dblib.get_db_pw()
        self.CONNECT_STRING = dblib.get_connection_string()
        self.clientConnection = pymongo.MongoClient(self.CONNECT_STRING, tlsCAFile=certifi.where())
        self.dbName = self.clientConnection[db_name]
        self.dbCollection = self.dbName[db_collection]
        self.intitialized = initialized

    def general_search(self, general_text, projection):
        loc_query = { "$or": [ { "job_title" : {"$regex":general_text}}, { "description": {"$regex":general_text}},{ "location" : {"$regex":general_text}} ] }
        fil_document = self.dbCollection.find(loc_query, projection)
        return fil_document

    def fil_location(self,in_str):
        loc_query = {"location" : {"$regex":in_str}}
        fil_document = self.dbCollection.find(loc_query)
        return fil_document

    def fil_sect_profession(self,in_str):
        loc_query = {"job_title" : {"$regex":in_str}}
        fil_document = self.dbCollection.find(loc_query)
        return fil_document
    
    def fil_salary_range(self, min_sal, max_sal):
        loc_query = {"$and": [{"min_salary_range":{"$gte":min_sal}},{"max_salary_range":{"$lte":max_sal}}]}
        fil_document = self.dbCollection.find(loc_query)
        return fil_document

    # Data retreival for user db connection
    def get_all_users(self):
        fil_document = self.dbCollection.find()
        return fil_document
    
    def get_user_by_id(self,user_id):
        loc_query = {"u_id":user_id}
        fil_document = self.dbCollection.find(loc_query)
        return fil_document

    def get_name_by_id(self,user_id):
        loc_query = {"u_id":user_id}
        fil_document = self.dbCollection.find(loc_query)
        u_name = None
        for cursor_pointer in fil_document:
            u_name = (cursor_pointer["first_name"], cursor_pointer["last_name"])
        return u_name # returns a tuple of strings -> ("first_name", "last_name")
