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
            print(item)

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_users(self):
        sql = "select * from freedom.users" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = UsersModel.dictionaries_to_objects_users(data_in_dictionary)
        return data_dict_to_object
    
    #################################################
    #fix and enter query for one result...
    def get_one_user(self):
        sql = "select * from freedom.users limit 1"
        data_in_dictionary = self.dal.get_scalar(sql)
        data_dict_to_object = UsersModel.dictionary_to_one_object_user(data_in_dictionary)
        return data_dict_to_object
    #################################################

    def insert_new_user(self, firstname, lastname, email, password, roleId): 
        sql = "INSERT INTO freedom.users (firstname, lastname, email, password, roleId) VALUES (%s,%s,%s,%s,%s)"
        params = (firstname, lastname, email, password, roleId)
        new_user_id = self.dal.insert(sql, (params))
        if new_user_id > 0:
            return new_user_id
        else:
            return False

    def check_if_email_exists(self, email):
        sql = "select * from freedom.users where email = %s"
        params = (email, )
        user_data = self.dal.get_scalar(sql, (params))
        if user_data == None:
            return False
        else:
            return True
        
        
    # add raise if email incorrect/not in the system or password incorrect
    def get_user_by_email_and_password(self, email, password):
        sql = "select * from freedom.users where email = %s and password = %s"
        params = (email, password)
        user_data = self.dal.get_scalar(sql, (params))
        if user_data == None:
            return False
        else:
            user = UsersModel.dictionary_to_one_object_user(user_data)
            return user
        

    
        







