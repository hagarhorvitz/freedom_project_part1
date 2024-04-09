from utils.dal import *
from models.countries_model import *

class CountriesLogic:
    def __init__(self):
        self.dal  = DAL()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_countries(self):
        sql = "select * from freedom.countries" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = CountriesModel.dictionaries_to_objects_countries(data_in_dictionary)
        return data_dict_to_object
    
    def get_one_country(self):
        sql = "select * from freedom.countries limit 1" #enter query for one result...
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = CountriesModel.dictionary_to_one_object_country(data_in_dictionary)
        return data_dict_to_object
    
    @staticmethod
    def display_countries(sql_result):
        for item in sql_result:
            print(item)

    def close(self):
        self.dal.close()
