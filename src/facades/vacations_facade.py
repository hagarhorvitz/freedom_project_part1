import datetime
from datetime import date
from logic.vacations_logic import *

class VacationsFacade:
    def __init__(self):
        self.logic = VacationsLogic()

    def close(self):
        self.logic.close()

    def all_vacations_ordered(self, order_by):
        if not all((order_by, )):
            raise ValueError ("Please provide all required information correctly")
        if not isinstance(order_by, str):
            raise TypeError ("Column's type to order by must entered as text letters (string)")
        allowed_columns_as_parameter = ["vacationId", "countryId", "vacationInfo", "startDate", "endDate", "price", "photoFileName"]
        if order_by not in allowed_columns_as_parameter:
            raise ValueError("Invalid column name to order by")
        else:
            vacations_by_startDate = self.logic.get_all_vacations_ordered(order_by)
            vacations = self.logic.display_vacations(vacations_by_startDate)
            return vacations

    def add_new_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName):
        if not all((countryId, vacationInfo, startDate, endDate, price, photoFileName)):
            raise ValueError ("Please provide all required information correctly")
        if not isinstance(countryId, int):
            raise TypeError ("Country Id must entered as number (integer)")
        if not isinstance(price, int):
            raise TypeError ("Price must entered as number (integer)")
        if not isinstance(vacationInfo, str):
            raise TypeError ("Vacation information must entered as text letters (string)")
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
            raise ValueError ("Start date can't be in the past")
        if end < today:
            raise ValueError ("End date can't be in the past")
        if len(vacationInfo) > 250:
            raise ValueError ("Vacation description can be up to 250 characters")
        else:
            new_vacation_id = self.logic.insert_new_vacation(countryId, vacationInfo, startDate, endDate, price, photoFileName)
            if new_vacation_id > 0:
                return f"New vacation just added successfully!\nNew vacation ID: {new_vacation_id}"
            else:
                raise Exception("Unfortunately something went wrong...Please try again and make sure all provided information is valid (F)")

    def update_exist_vacation(self, countryId, vacationInfo, startDate, endDate, price, vacationId):
        if not all((countryId, vacationInfo, startDate, endDate, price, vacationId)):
            raise ValueError ("Please provide all required information correctly")
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
        if price > 10000:
            raise ValueError ("Vacation's price must be up to 10,000")
        start = datetime.datetime.strptime(startDate,"%Y-%m-%d").date()
        end = datetime.datetime.strptime(endDate,"%Y-%m-%d").date()
        if end <= start:
            raise ValueError ("End date can't be before start date")
        if len(vacationInfo) > 250:
            raise ValueError ("Vacation description can be up to 250 characters")
        else:
            update_vacation = self.logic.update_vacation(countryId, vacationInfo, startDate, endDate, price, vacationId)
            if update_vacation > 0:
                return f"Vacation ID {vacationId} updated successfully!"
            else:
                raise Exception(f"Unfortunately failed to update vacation ID {vacationId} - ID was not found and/or no changes was made")

    def delete_vacation(self, vacationId):
        if not all((vacationId, )):
            raise ValueError ("Please provide all required information correctly")
        if not isinstance(vacationId, int):
            raise TypeError ("Vacation ID must entered as number (integer)")
        else:
            delete_vacation = self.logic.delete_vacation(vacationId)
            if delete_vacation > 0:
                return f"Vacation ID {vacationId} deleted successfully included all likes!"
            else:
                raise Exception(f"Unfortunately failed to delete vacation ID {vacationId} (and likes).\nID was not found and/or no changes was made")
        




    
