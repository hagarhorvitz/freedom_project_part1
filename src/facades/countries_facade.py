from logic.countries_logic import *

class CountriesFacade:
    def __init__(self):
        self.logic = CountriesLogic()
    
    def close(self):
        self.logic.close()

    def add_new_country(self, countryName):
        if not all((countryName, )):
            raise ValueError("Please provide all required information correctly")
        if not isinstance(countryName, str):
            raise TypeError ("Country's name must entered as text letters (string)")
        new_country_id = self.logic.insert_new_county(countryName)
        if new_country_id > 0:
            return f"Congratulations! New country just added🥳\nNew country's ID: {new_country_id}\nNew country's name: {countryName}"
        else:
            raise Exception("Unfortunately something went wrong...Please try again and make sure all provided information is valid")
