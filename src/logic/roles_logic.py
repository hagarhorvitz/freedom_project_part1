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
            print(f"{item}\n{"="*20}")

    def get_all_roles(self):
        sql = "select * from freedom.roles" 
        roles_data_dictionary = self.dal.get_table(sql)
        roles_data_dict_to_obj = RolesModel.dictionaries_to_objects_roles(roles_data_dictionary)
        return roles_data_dict_to_obj
    
    def get_one_role_by_id(self, roleId):
        sql = "select * from freedom.roles where roleId = %s"
        params = (roleId, )
        role_data_dictionary = self.dal.get_scalar(sql, (params))
        if role_data_dictionary == None:
            raise ValueError("No role by this ID")
        else:
            role_data_dict_to_obj = RolesModel.dictionary_to_one_object_role(role_data_dictionary)
            return role_data_dict_to_obj
    
    def get_one_role_by_name(self, roleName):
        sql = "select * from freedom.roles where roleName = %s"
        params = (roleName, )
        role_data_dictionary = self.dal.get_scalar(sql, (params))
        if role_data_dictionary == None:
            raise ValueError("No role by this name")
        else:
            role_data_dict_to_obj = RolesModel.dictionary_to_one_object_role(role_data_dictionary)
            return role_data_dict_to_obj



