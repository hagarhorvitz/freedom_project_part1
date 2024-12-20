from utils.dal import *
from models.users_model import *

class UsersLogic:
    def __init__(self):
        self.dal = DAL()
    
    def close(self):
        self.dal.close()

    @staticmethod
    def display_users(sql_result):
        for item in sql_result:
            print(f"{item}\n{"="*25}")

    def get_all_users(self):
        sql = "select * from freedom.users" 
        users_data_dictionary = self.dal.get_table(sql)
        users_data_dict_to_obj = UsersModel.dictionaries_to_objects_users(users_data_dictionary)
        return users_data_dict_to_obj

    def get_one_user(self):
        sql = "select * from freedom.users limit 1"
        user_data_dictionary = self.dal.get_scalar(sql)
        user_data_dict_to_obj = UsersModel.dictionary_to_one_object_user(user_data_dictionary)
        return user_data_dict_to_obj

    def insert_new_user(self, firstname, lastname, email, password, roleId): 
        sql = "INSERT INTO freedom.users (firstname, lastname, email, password, roleId) VALUES (%s,%s,%s,%s,%s)"
        params = (firstname, lastname, email, password, roleId)
        try:
            new_user_id = self.dal.insert(sql, (params))
            return new_user_id
        except Exception as err:
            if hasattr(err, "errno") and err.errno == 1452:
                raise Exception("Invalid roleId or roleId doesn't exist. Please provide a valid roleId")
            else:
                raise Exception("Unfortunately something went wrong...Please try again and make sure all provided information is valid (L)")
    
    def check_if_email_exists(self, email):
        sql = "select * from freedom.users where email = %s"
        params = (email, )
        user_data = self.dal.get_scalar(sql, (params))
        if user_data == None:
            return False
        else:
            return True
        
    def get_user_by_email_and_password(self, email, password):
        sql = "select * from freedom.users where email = %s and password = %s"
        params = (email, password)
        user_data = self.dal.get_scalar(sql, (params))
        if user_data == None:
            return False
        else:
            user = UsersModel.dictionary_to_one_object_user(user_data)
            return user
        

    
        







