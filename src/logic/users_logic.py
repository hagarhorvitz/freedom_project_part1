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
    
    @staticmethod
    def display_users(sql_result):
        for item in sql_result:
            print(item)

    def close(self):
        self.dal.close()



