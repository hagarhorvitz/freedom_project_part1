from utils.dal import *
from models.users_model import *

class UsersLogic:
    def __init__(self):
        self.dal = DAL()
    
    def close(self):
        self.dal.close()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    
    def get_all_users(self):
        sql = "select * from freedom.users" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = UsersModel.dictionaries_to_objects_users(data_in_dictionary)
        return data_dict_to_object
    
    #fix and enter query for one result...
    def get_one_user(self):
        sql = "select * from freedom.users limit 1"
        data_in_dictionary = self.dal.get_scalar(sql)
        data_dict_to_object = UsersModel.dictionary_to_one_object_user(data_in_dictionary)
        return data_dict_to_object

    @staticmethod
    def display_users(sql_result):
        for item in sql_result:
            print(item)
    
    # add raise if roleid =1 or to set roleid as 2 in the params?
    # add raise if email already in the system
    def insert_new_user(self, firstname, lastname, email, password, roleId): 
        sql = "INSERT INTO freedom.users (firstname, lastname, email, password, roleId) VALUES (%s,%s,%s,%s,%s)"
        params = (firstname, lastname, email, password, roleId)
        new_user = self.dal.insert(sql, (params))
        return f"New user was added successfully\nNew user id: {new_user}"
    
    # add raise if email incorrect/not in the system or password incorrect
    def get_user_by_email_and_password(self, email, password):
        sql = "select * from freedom.users where email = %s and password = %s"
        params = (email, password)
        user_data = self.dal.get_scalar(sql, (params))
        user = UsersModel.dictionary_to_one_object_user(user_data)
        return user
    
    # add raise!
    def check_if_user_exists(self, email):
        sql = "select * from freedom.users where email = %s"
        params = (email, )
        user_data = self.dal.get_scalar(sql, (params))
        if user_data == None:
            return f"'{email}' doesn't exists in the system"
        else:
            return f"'{email}' is in the system (:"
    
        







