from logic.countries_logic import *

class CountriesFacade:
    def __init__(self):
        self.logic = CountriesLogic()
    
    def close(self):
        self.logic.close()


