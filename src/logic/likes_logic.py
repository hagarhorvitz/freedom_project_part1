from utils.dal import *
from models.likes_model import *

class LikesLogic:
    def __init__(self):
        self.dal  = DAL()

    def close(self):
        self.dal.close()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_likes(self):
        sql = "select * from freedom.likes" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = LikesModel.dictionaries_to_objects_likes(data_in_dictionary)
        return data_dict_to_object
    
    def get_one_like(self):
        sql = "select * from freedom.likes limit 1" #enter query for one result...
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = LikesModel.dictionary_to_one_object_like(data_in_dictionary)
        return data_dict_to_object
    
    @staticmethod
    def display_likes(sql_result):
        for item in sql_result:
            print(item)

    # add raise/if if userid/vacationid not existed
    # add raise/if something wrong
    def add_like(self, userId, vacationId): 
        sql = "INSERT INTO freedom.likes (userId, vacationId) VALUES (%s,%s)"
        params = (userId, vacationId)
        new_like = self.dal.insert(sql, (params))
        return f"Thank you for liking our vacation 👍"
    
    # add raise/if if userid/vacationid not existed
    # add raise/if something wrong
    def delete_like(self, userId, vacationId): 
        sql = "DELETE FROM freedom.likes WHERE userId = %s and vacationId = %s"
        params = (userId, vacationId)
        delete_like_row = self.dal.delete(sql, (params))
        return f"Deleted {delete_like_row} like successfully (unlike) from user ID {userId} for vacation ID {vacationId}"
    


