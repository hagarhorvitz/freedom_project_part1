import datetime
from datetime import date
from logic.vacations_logic import *

## performing the actual functionality needed by the system:
class VacationsFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = VacationsLogic()

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
    #################################################
    def get_all_vacations_by_startDate(self):
        vacations_by_startDate = self.logic.get_all_vacations_ordered("startDate")
        vacations = self.logic.display_vacations(vacations_by_startDate)
        return f"All vacation ordered by start date:\n{vacations}"
    #################################################

    # make sure it works #
    ### 1. should we add if to check countryId existed, and then we need to write function... ###
    ### 2. add raise if User is trying? - because only Admin can ###
    ### 3. or just make sure only admins can see it, and users wont - and how ###
    def add_new_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName):
        if not countryId or not vacationInfo or not startDate or not endDate or not price or not photoFileName:
            raise ValueError ("Please provide all required information")
        if not isinstance(countryId, int):
            raise TypeError ("Country Id must entered as number (integer)")
        if not isinstance(price, int):
            raise TypeError ("Price must entered as number (integer)")
        if not isinstance(vacationInfo, str):
            raise TypeError ("Vacation Information must entered as text letters (string)")
        if not isinstance(photoFileName, str):
            raise TypeError ("Photo file's name must entered as text letters (string)")
        if not isinstance(startDate, str):
            raise TypeError ("Start date must entered in the format 'YYYY-MM-DD' as text letters (string)")
        if not isinstance(endDate, str):
            raise TypeError ("End date must entered in the format 'YYYY-MM-DD' as text letters (string)")
        if price < 0:
            raise ValueError ("Vacation's price can't be negative")
        if price > 10000 :
            raise ValueError ("Vacation's price must be up to 10000")
        start = datetime.datetime.strptime(startDate,"%Y-%m-%d").date()
        end = datetime.datetime.strptime(endDate,"%Y-%m-%d").date()
        if end <= start:
            raise ValueError ("End date can't be before start date")
        today = date.today()
        if start < today:
            raise ValueError ("Start date must be tomorrow and up (future date only)")
        if end < today:
            raise ValueError ("End date must be tomorrow and up (future date only)")
        else:
            new_vacation_id = self.logic.insert_vacation(countryId, vacationInfo, startDate, endDate, price, photoFileName)
            if new_vacation_id == False:
                raise ValueError ("Unfortunately something went wrong...Please try again and make sure all provided information is valid")
            else:
                return f"New vacation just added successfully!\nNew vacation ID: {new_vacation_id}"

    # make sure it works
    ### 1. should we add if vacationId not exist, and then we need to write function... ###
    ### 2. should we add if countryId not exist, and then we need to write function... ###
    ### 3. add raise if User is trying - because only Admin can ###
    ### 4. or just make sure only admins can see it, and users wont - and how ###
    def update_exist_vacation(self, countryId, vacationInfo, startDate, endDate, price, vacationId):
        if not countryId or not vacationInfo or not startDate or not endDate or not price or not vacationId:
            raise ValueError ("Please provide all required information")
        if not isinstance(countryId, int):
            raise TypeError ("Country Id must entered as number (integer)")
        if not isinstance(vacationId, int):
            raise TypeError ("Vacation Id must entered as number (integer)")
        if not isinstance(price, int):
            raise TypeError ("Price must entered as number (integer)")
        if not isinstance(vacationInfo, str):
            raise TypeError ("Vacation Information must entered as text letters (string)")
        if not isinstance(startDate, str):
            raise TypeError ("Start date must entered in the format 'YYYY-MM-DD' as text letters (string)")
        if not isinstance(endDate, str):
            raise TypeError ("End date must entered in the format 'YYYY-MM-DD' as text letters (string)")
        if price < 0:
            raise ValueError ("Vacation's price can't be negative")
        if price > 10000 :
            raise ValueError ("Vacation's price must be up to 10000")
        start = datetime.datetime.strptime(startDate,"%Y-%m-%d").date()
        end = datetime.datetime.strptime(endDate,"%Y-%m-%d").date()
        if end <= start:
            raise ValueError ("End date can't be before start date")
        else:
            update_vacation = self.logic.update_vacation(countryId, vacationInfo, startDate, endDate, price, vacationId)
            if update_vacation == True:
                return f"Vacation ID {vacationId} updated successfully!"
            elif update_vacation == False:
                raise ValueError(f"Unfortunately failed to update vacation ID {vacationId} - ID was not found and/or no changes was made")


    ## make sure like was deleted and the function works ##
    ### 1. should we add if vacationId not exist, and then we need to write function... ###
    ### 2. add raise if User is trying - because only Admin can ###
    ### 3. or just make sure only admins can see it, and users wont - and how ###
    def delete_vacation(self, vacationId):
        if not vacationId:
            raise ValueError ("Please provide all required information")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        else:
            delete_vacation = self.logic.delete_vacation(vacationId)
            if delete_vacation == True:
                return f"Vacation ID {vacationId} deleted successfully included all likes!"
            elif delete_vacation == False:
                raise ValueError(f"Unfortunately failed to delete vacation ID {vacationId} (and likes) - ID was not found and/or no changes was made")
        
    # ## generate random (copied what Asaf did in his example...)
    # def get_random_vacation(self):
    #     all_vacations = self.logic.get_all_vacations()
    #     index = random.randint(1, len(all_vacations))
    #     random_vacation = all_vacations[index]
    #     return random_vacation




    
