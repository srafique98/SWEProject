from select import select
import pymongo
import certifi
import src.db_library as dblib


class DB_Client:
    dbPassword = None
    CONNECT_STRING = None
    clientConnection = None
    dbName = None
    dbCollection = None
    initialized = False

    def __init__(self, initialized, db_name, db_collection):
        self.dbPassword = dblib.get_db_pw()
        self.CONNECT_STRING = dblib.get_connection_string()
        self.clientConnection = pymongo.MongoClient(self.CONNECT_STRING, tlsCAFile=certifi.where())
        self.dbName = self.clientConnection[db_name]
        self.dbCollection = self.dbName[db_collection]
        self.initialized = initialized

    def __del__(self):
        self.clientConnection.close()

    # Create new fields within all documents
        # pass in the new field name (string) ex: "resume" or "item_number"
        # pass in OPTIONAL argument for the value in field
    def create_new_document_field(self, field_name, *args):
        passed_value = None
        for ar in args:
            if len(args) > 1:
                print("new field creation failed")
            else:
                passed_value = ar
        if passed_value is not None:
            new_q = {"$set": {field_name : passed_value}}
            self.dbCollection.update_many({},new_q)
        else:
            new_q = {"$set": {field_name : None}}
            self.dbCollection.update_many({},new_q)

#   General search used in the top search bar in Listing Window
#       (general_text) pass in text to regex for in DB
#       (projection) field value to be returned
    def general_search(self,general_text, projection):
        loc_query = { "$or": [ { "job_title" : {"$regex":general_text}},{"job_description": {"$regex":general_text}}, { "location" : {"$regex":general_text}},{"$and": [{"min_salary_range":{"$gte":general_text}},{"max_salary_range":{"$lte":general_text}}]} ] }
        doc_cursor = self.dbCollection.find(loc_query, projection)
        return doc_cursor

#   Deprecated search function *as to Sean's understanding*
    def fil_search(self, str_job, str_loc,flt_min,flt_max, projection):
        loc_query = { "$and": [ { "job_title" : {"$regex":str_job}}, { "location" : {"$regex":str_loc}},{"$and": [{"min_salary_range":{"$gte":flt_min}},{"max_salary_range":{"$lte":flt_max}}]} ] }
        print(loc_query)
        doc_cursor = self.dbCollection.find(loc_query, projection)
        print(doc_cursor)
        return doc_cursor

#   Filter DB by location regex
#       (in_str) regex to check against db location field values
    def fil_location(self,in_str):
        agg_query = [{ '$match': {'$or': [ {  'Full_State': in_str }, { 'State': in_str },{"Zip Code":in_str},{"City":in_str},{"location":in_str}]}}]
        doc_cursor = self.dbCollection.aggregate(agg_query)
        return doc_cursor

#   Filter DB by profession regex
#       (in_str) regex to check against db job_title field values
    def fil_sect_profession(self,in_str):
        loc_query = {"job_title" : {"$regex":in_str}}
        doc_cursor = self.dbCollection.find(loc_query)
        return doc_cursor

#   Filter DB by profession regex
#       (in_str) regex to check against db job_title field values   
    def fil_salary_range(self, min_sal, max_sal):
        loc_query = {"$and": [{"min_salary_range":{"$gte":min_sal}},{"max_salary_range":{"$lte":max_sal}}]}
        doc_cursor = self.dbCollection.find(loc_query)
        return doc_cursor

# --------------------------------------------------------------------
# Data retrieval for USER db connection

#   Returns document cursor object of all users and all fields in mongodb.Jobs.users
    def get_all_users(self):
        doc_cursor = self.dbCollection.find()
        return doc_cursor

#   Returns document cursor object of user by u_id value
#       (user_id) unique integer value assigned to each user document 
    def get_user_by_id(self,user_id):
        loc_query = {"u_id":user_id}
        doc_cursor = self.dbCollection.find(loc_query)
        return doc_cursor

#   Returns a tuple of strings ("first_name", "last_name") of a specific user filtered by u_id
#       (user_id) unique integer value assigned to each user document
    def get_name_by_id(self,user_id):
        loc_query = {"u_id":user_id}
        doc_cursor = self.dbCollection.find(loc_query)
        u_name = None
        for cursor_pointer in doc_cursor:
            u_name = (cursor_pointer["first_name"], cursor_pointer["last_name"])
        return u_name # returns a tuple of strings -> ("first_name", "last_name")

#   Returns the base64 encoded bytes of a specific user filtered by u_id
#       (user_id) unique integer value assigned to each user document 
    def get_resume_by_u_id(self, user_id):
        loc_query = {"u_id":user_id}
        doc_cursor = self.dbCollection.find(loc_query)
        pdf_bytes = None
        for pointer in doc_cursor:
            pdf_bytes = pointer["resume"]
        return pdf_bytes
