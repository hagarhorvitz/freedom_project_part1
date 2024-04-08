from utils.dal import *
from models.likes_model import *

class LikesLogic:
    def __init__(self):
        self.dal  = DAL()

    def get_all_likes(self):
        sql = "select * from freedom.likes" 
        data_in_dictionary = self.dal.get_table(sql)
        ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
        data_dict_to_object = LikesModel.dictionaries_to_objects_likes(data_in_dictionary)
        return data_dict_to_object
    
    def get_one_like(self):
        sql = "select * from freedom.likes limit 1" #enter query for one result...
        data_in_dictionary = self.dal.get_scalar(sql)
        ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
        data_dict_to_object = LikesModel.dictionary_to_one_object_like(data_in_dictionary)
        return data_dict_to_object
    
    @staticmethod
    def display_likes(sql_result):
        for item in sql_result:
            print(item)

    def close(self):
        self.dal.close()


