# import random
from utils.dal import *
from models.vacations_model import *

# במערכת קיימים שני תפקידים (Roles):
# Admin - יכול לצפות בחופשות, להוסיף חופשה חדשה, לעדכן חופשה קיימת או למחוק חופשה.
# User משתמש רגיל - יכול לצפות בחופשות הקיימות במערכת, לבצע Like או Unlike לחופשה.

class VacationsLogic:
    def __init__(self):
        self.dal  = DAL()
    
    def close(self):
        self.dal.close()

    ## sql and data (above) - for functions with params, dont forget to write params and %s in the sql
    def get_all_vacations(self):
        sql = "select * from freedom.vacations" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = VacationsModel.dictionaries_to_objects_vacations(data_in_dictionary)
        return data_dict_to_object
        
    #fix and enter query for one result...
    def get_one_vacation(self):
        sql = "select * from freedom.vacations limit 1"
        data_in_dictionary = self.dal.get_scalar(sql)
        data_dict_to_object = VacationsModel.dictionary_to_one_object_vacation(data_in_dictionary)
        return data_dict_to_object

    @staticmethod
    def display_vacations(sql_result):
        for item in sql_result:
            print(item)

    # add raise or whatever if User is trying - because only Admin can
    # or just make sure only admins can see it, and users wont
    # add raise if something incorrect
    def insert_new_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName): 
        sql = "INSERT INTO freedom.vacations (countryId, vacationInfo, startDate, endDate, price, photoFileName) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (countryId, vacationInfo, startDate, endDate, price, photoFileName)
        new_vacation = self.dal.insert(sql, (params))
        return f"New vacation was added successfully!\nNew vacation id: {new_vacation}"
    
    # raise/if if vacationId is or not existed
    # only admin can
    def update_existing_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName, vacationId):
        sql = "UPDATE freedom.vacations SET countryId = %s, vacationInfo = %s, startDate = %s, endDate = %s, price = %s, photoFileName = %s WHERE vacationId = %s"
        params = (countryId, vacationInfo, startDate, endDate, price, photoFileName, vacationId)
        update_vacation_row = self.dal.update(sql, (params))
        if update_vacation_row > 0:
            return f"Vacation with ID {vacationId} updated successfully!"
        else:
            return f"Failed to update vacation with ID {vacationId}. Vacation ID not found or no changes made."

    # raise/if if vacationId is or not existed
    # only admin can
    def delete_vacation(self, vacationId):
        sql = "DELETE FROM freedom.vacations WHERE vacationId = %s"
        params = (vacationId,)
        deleted_vacation_row = self.dal.delete(sql, (params))
        if deleted_vacation_row > 0:
            return f"Vacation with ID {vacationId} deleted successfully!"
        else:
            return f"Failed to delete vacation with ID {vacationId}. Vacation ID not found."






      



    # def count_all_vacations(self):
    #     sql = "select count(vacationId) from freedom.vacations"
    #     data = self.dal.get_scalar(sql)
    #     return data



