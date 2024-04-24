import random
from datetime import date
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

    # make sure it works
    def get_vacations_order_by_startDate(self, startDate):
        if startDate != "startDate":
            raise ValueError ("You must write the argument correctly")
        else:
            vacations_by_startDate = self.logic.get_all_vacations_by_order(startDate)
            return f"All vacation ordered by start date:\n{vacations_by_startDate}"

    def add_new_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName):
        if not countryId or not vacationInfo or not startDate or not endDate or not price or not photoFileName:
            raise ValueError ("Please provide all required information")
        if price < 0:
            raise ValueError ("Vacation's price can't be negative")
        if price > 10000 :
            raise ValueError ("Vacation's price must be up to 10000")
        if endDate <= startDate: ########### handle the dates ###########
            raise ValueError ("End date can't be before start date")
        today = date.today()
        if startDate < today or endDate < today: ########### handle the dates ###########
            raise ValueError ("Start or and dates can't be in the past")
        else:
            new_vacation_id = self.logic.insert_new_vacation(countryId, vacationInfo, startDate, endDate, price, photoFileName)
            return f"New vacation was added successfully!\nNew vacation id: {new_vacation_id}"
        
    def update_exist_vacation(self, countryId, vacationInfo, startDate, endDate, price, vacationId, photoFileName=None):
        if not countryId or not vacationInfo or not startDate or not endDate or not price or not vacationId:
            raise ValueError ("Please provide all required information")
        if price < 0:
            raise ValueError ("Vacation's price can't be negative")
        if price > 10000 :
            raise ValueError ("Vacation's price must be up to 10000")
        if endDate <= startDate: ########### handle the dates ###########
            raise ValueError ("End date can't be before start date")
        ## add if: vacationid and countryid not exist ##
        else:
            update_vacation = self.logic.update_existing_vacation(countryId, vacationInfo, startDate, endDate, price, vacationId, photoFileName=None)
            if update_vacation == True:
                return f"Vacation ID {vacationId} updated successfully!"
            else:
                return f"Failed to update vacation ID {vacationId}. ID not found or no changes made."

    ## make sure like was deleted ##
    def delete_vacation(self, vacationId):
        if not vacationId:
            raise ValueError ("Please provide all required information")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        else:
            delete_vacation = self.logic.delete_vacation(vacationId)
            if delete_vacation == True:
                return f"Vacation ID {vacationId} deleted successfully included all likes!"
            else:
                return f"Failed to delete vacation ID {vacationId} and likes - ID not found."
        






    
