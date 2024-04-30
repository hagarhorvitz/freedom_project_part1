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
            print(f"{item}\n{"="*32}")

    def get_all_countries(self):
        sql = "select * from freedom.countries" 
        countries_data_dictionary = self.dal.get_table(sql)
        countries_data_dict_to_obj = CountriesModel.dictionaries_to_objects_countries(countries_data_dictionary)
        return countries_data_dict_to_obj
    
    def get_one_country_by_id(self, countryId):
        sql = "select * from freedom.countries where countryId = %s"
        params = (countryId, )
        country_data_dictionary = self.dal.get_scalar(sql, (params))
        if country_data_dictionary == None:
            raise ValueError("No county by this ID")
        else:
            country_data_dict_to_obj = CountriesModel.dictionary_to_one_object_country(country_data_dictionary)
            return country_data_dict_to_obj
        
    def get_one_country_by_name(self, countryName):
        sql = "select * from freedom.countries where countryName = %s"
        params = (countryName, )
        country_data_dictionary = self.dal.get_scalar(sql, (params))
        if country_data_dictionary == None:
            raise ValueError("No county by this name")
        else:
            country_data_dict_to_obj = CountriesModel.dictionary_to_one_object_country(country_data_dictionary)
            return country_data_dict_to_obj
        
    def add_new_county(self, countryName):
        sql = "INSERT INTO freedom.countries (countryName) VALUES (%s)"
        params = (countryName, )
        new_country_id = self.dal.insert(sql, (params))
        if new_country_id > 0:
            return new_country_id
        else:
            raise ValueError ("Could'n add new country, ")


