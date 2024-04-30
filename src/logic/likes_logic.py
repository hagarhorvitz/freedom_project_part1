from utils.dal import *
from models.likes_model import *

class LikesLogic:
    def __init__(self):
        self.dal  = DAL()

    def close(self):
        self.dal.close()

    @staticmethod
    def display_likes(sql_result):
        for item in sql_result:
            print(f"{item}\n{"="*15}")

    def get_all_likes(self):
        sql = "select * from freedom.likes" 
        likes_data_dictionary = self.dal.get_table(sql)
        likes_data_dict_to_obj = LikesModel.dictionaries_to_objects_likes(likes_data_dictionary)
        return likes_data_dict_to_obj
    
    def get_one_like(self):
        sql = "select * from freedom.likes limit 1" 
        like_data_dictionary = self.dal.get_scalar(sql)
        like_data_dict_to_obj = LikesModel.dictionary_to_one_object_like(like_data_dictionary)
        return like_data_dict_to_obj
    
    ######################################################################
    def add_like(self, userId, vacationId): 
        sql = "INSERT INTO freedom.likes (userId, vacationId) VALUES (%s,%s)"
        params = (userId, vacationId)
        new_like = self.dal.insert(sql, (params))
        if new_like == None:
            return True
        else:
            return False
    ######################################################################

    def delete_like(self, userId, vacationId): 
        sql = "DELETE FROM freedom.likes WHERE userId = %s and vacationId = %s"
        params = (userId, vacationId)
        delete_like_row = self.dal.delete(sql, (params))
        if delete_like_row > 0:
            return True
        else:
            return False
    


