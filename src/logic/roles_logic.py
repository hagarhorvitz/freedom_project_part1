from utils.dal import *
from models.roles_model import *

class RolesLogic:
    def __init__(self):
        self.dal = DAL()

    def close(self):
        self.dal.close()
    
    @staticmethod
    def display_roles(sql_result):
        for item in sql_result:
            print(item)

    def get_all_roles(self):
        sql = "select * from freedom.roles" 
        roles_data_dictionary = self.dal.get_table(sql)
        roles_data_dict_to_obj = RolesModel.dictionaries_to_objects_roles(roles_data_dictionary)
        return roles_data_dict_to_obj
    
    def get_one_role(self):
        sql = "select * from freedom.roles limit 1"
        role_data_dictionary = self.dal.get_table(sql)
        role_data_dict_to_obj = RolesModel.dictionary_to_one_object_role(role_data_dictionary)
        return role_data_dict_to_obj




