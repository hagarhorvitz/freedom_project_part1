import random
from logic.vacations_logic import *

## performing the actual functionality needed by the system:
class VacationsFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = VacationsLogic()

    ## generate random (copied what Asaf did in his example...)
    def get_random_vacation(self):
        all_vacations = self.logic.get_all_vacations()
        index = random.randint(1, len(all_vacations))
        random_vacation = all_vacations[index]
        return random_vacation
    
    ## close resources:
    def close(self):
        self.logic.close()

    ## enabling "with" keyword usage:
    def __enter__(self):
        return self
    
    ## disposing when existing "with" block:
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()






    