import random
from logic.countries_logic import *

## performing the actual functionality needed by the system:
class CountriesFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = CountriesLogic()

    ## generate random (copied what Asaf did in his example...)
    def get_random_country(self):
        all_countries = self.logic.get_all_countries()
        index = random.randint(1, len(all_countries))
        random_country = all_countries[index]
        return random_country
    
    ## close resources:
    def close(self):
        self.logic.close()

    ## enabling "with" keyword usage:
    def __enter__(self):
        return self
    
    ## disposing when existing "with" block:
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()