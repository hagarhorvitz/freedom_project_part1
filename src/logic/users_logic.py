from utils.dal import *
from models.users_model import *

class UsersLogic:
    def __init__(self):
        self.dal = DAL()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_users(self):
        sql = "select * from freedom.users" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = UsersModel.dictionaries_to_objects_users(data_in_dictionary)
        return data_dict_to_object
    
    def get_one_user(self):
        sql = "select * from freedom.users limit 1" #enter query for one result...
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = UsersModel.dictionary_to_one_object_user(data_in_dictionary)
        return data_dict_to_object
    
    def insert_new_user(self, object_new_user):
        sql = "INSERT INTO freedom.users ('firstname', 'lastname', 'email', 'password', 'roleId') VALUES (%s)"
        params = ()
        new_user = self.dal.insert(sql, params)


    @staticmethod
    def display_users(sql_result):
        for item in sql_result:
            print(item)

    def close(self):
        self.dal.close()

# def insert(self, sql, params=None):
#     with self.connection.cursor() as cursor:
#         cursor.execute(sql, params)
#         self.connection.commit()
#         last_row_id = cursor.lastrowid
#         return last_row_id

