from utils.dal import *
from models.countries_model import *

class CountriesLogic:
    def __init__(self):
        self.dal  = DAL()
    
    def close(self):
        self.dal.close()

    @staticmethod
    def display_countries(sql_result):
        for item in sql_result:
            print(item)

    def get_all_countries(self):
        sql = "select * from freedom.countries" 
        countries_data_dictionary = self.dal.get_table(sql)
        countries_data_dict_to_obj = CountriesModel.dictionaries_to_objects_countries(countries_data_dictionary)
        return countries_data_dict_to_obj
    
    def get_one_country(self):
        sql = "select * from freedom.countries limit 1"
        country_data_dictionary = self.dal.get_scalar(sql)
        country_data_dict_to_obj = CountriesModel.dictionary_to_one_object_country(country_data_dictionary)
        return country_data_dict_to_obj


