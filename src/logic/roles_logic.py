from utils.dal import *
from models.roles_model import *

class RolesLogic:
    def __init__(self):
        self.dal = DAL()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_roles(self):
        sql = "select * from freedom.roles" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = RolesModel.dictionaries_to_objects_roles(data_in_dictionary)
        return data_dict_to_object
    
    def get_one_role(self):
        sql = "select * from freedom.roles limit 1" #enter query for one result...
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = RolesModel.dictionary_to_one_object_role(data_in_dictionary)
        return data_dict_to_object
    
    @staticmethod
    def display_roles(sql_result):
        for item in sql_result:
            print(item)

    def close(self):
        self.dal.close()


