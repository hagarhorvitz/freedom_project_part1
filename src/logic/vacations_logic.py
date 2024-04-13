# import random
from utils.dal import *
from models.vacations_model import *

class VacationsLogic:
    def __init__(self):
        self.dal  = DAL()
    
    def close(self):
        self.dal.close()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_vacations(self):
        sql = "select * from freedom.vacations" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = VacationsModel.dictionaries_to_objects_vacations(data_in_dictionary)
        return data_dict_to_object
        
    #fix and enter query for one result...
    def get_one_vacation(self):
        sql = "select * from freedom.vacations limit 1"
        data_in_dictionary = self.dal.get_scalar(sql)
        data_dict_to_object = VacationsModel.dictionary_to_one_object_vacation(data_in_dictionary)
        return data_dict_to_object

    @staticmethod
    def display_vacations(sql_result):
        for item in sql_result:
            print(item)

    # add raise or whatever if User is trying - because only Admin can
    # add raise if something incorrect
    def insert_new_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName): 
        sql = "INSERT INTO freedom.vacations (countryId, vacationInfo, startDate, endDate, price, photoFileName) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (countryId, vacationInfo, startDate, endDate, price, photoFileName)
        new_vacation = self.dal.insert(sql, (params))
        return f"New vacation was added successfully!\nNew vacation id: {new_vacation}"
    
    # def count_all_vacations(self):
    #     sql = "select count(vacationId) from freedom.vacations"
    #     data = self.dal.get_scalar(sql)
    #     return data



