# import random
from utils.dal import *
from models.vacations_model import *

class VacationsLogic:
    def __init__(self):
        self.dal  = DAL()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_vacations(self):
        sql = "select * from freedom.vacations" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = VacationsModel.dictionaries_to_objects_vacations(data_in_dictionary)
        return data_dict_to_object
    
    def get_one_vacation(self):
        sql = "select * from freedom.vacations limit 1" #enter query for one result...
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = VacationsModel.dictionary_to_one_object_vacation(data_in_dictionary)
        return data_dict_to_object

    @staticmethod
    def display_vacations(sql_result):
        for item in sql_result:
            print(item)
    
    # def count_all_vacations(self):
    #     sql = "select count(vacationId) from freedom.vacations"
    #     data = self.dal.get_scalar(sql)
    #     return data

    def close(self):
        self.dal.close()

