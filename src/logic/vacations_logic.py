import datetime
from datetime import date
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

    @staticmethod
    def display_vacations(sql_result):
        for item in sql_result:
            print(item)

    def get_all_vacations(self):
        sql = "select * from freedom.vacations" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = VacationsModel.dictionaries_to_objects_vacations(data_in_dictionary)
        return data_dict_to_object
    
    #################################################
    #fix and enter query for one result...
    def get_one_vacation(self):
        sql = "select * from freedom.vacations limit 1"
        data_in_dictionary = self.dal.get_scalar(sql)
        data_dict_to_object = VacationsModel.dictionary_to_one_object_vacation(data_in_dictionary)
        return data_dict_to_object
    #################################################

    #################################################
    # this function should be specific by startDate or to get any parameter?
    # in the future, to do a list they can choose order by
    def get_all_vacations_by_order(self, order_by):
        sql = f"select * from freedom.vacations order by {order_by}" 
        data_in_dictionary = self.dal.get_table(sql)
        data_dict_to_object = VacationsModel.dictionaries_to_objects_vacations(data_in_dictionary)
        return data_dict_to_object
    # def get_all_vacations_by_order(self, order_by):
    #     sql = f"select * from freedom.vacations order by %s" 
    #     # params = (order_by, ) - didnt work with params....
    #     data_in_dictionary = self.dal.get_table(sql)
    #     data_dict_to_object = VacationsModel.dictionaries_to_objects_vacations(data_in_dictionary)
    #     return data_dict_to_object
    #################################################

    def insert_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName): 
        sql = "INSERT INTO freedom.vacations (countryId, vacationInfo, startDate, endDate, price, photoFileName) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (countryId, vacationInfo, startDate, endDate, price, photoFileName)
        new_vacation_id = self.dal.insert(sql, (params))
        if new_vacation_id > 0:
            return new_vacation_id
        else:
            return False
    
    def update_vacation(self, countryId, vacationInfo, startDate, endDate, price, vacationId):
        sql = "UPDATE freedom.vacations SET countryId = %s, vacationInfo = %s, startDate = %s, endDate = %s, price = %s WHERE vacationId = %s"
        params = (countryId, vacationInfo, startDate, endDate, price, vacationId)
        update_vacation_row = self.dal.update(sql, (params))
        if update_vacation_row > 0:
            return True
        else:
            return False

    def delete_vacation(self, vacationId):
        sql = "DELETE FROM freedom.vacations WHERE vacationId = %s"
        params = (vacationId,)
        deleted_vacation_row = self.dal.delete(sql, (params))
        if deleted_vacation_row > 0:
            return True
        else:
            return False


#################################################
    # def check_vacation(self, startDate, endDate): 
    #     today = date.today()
    #     start = datetime.datetime.strptime(startDate,"%Y-%m-%d").date()
    #     end = datetime.datetime.strptime(endDate,"%Y-%m-%d").date()
    #     if start < today:
    #         raise ValueError ("Start date can't be in the past")
    #     if end < today:
    #         raise ValueError ("End date can't be in the past")
    #     else:
    #         sql = "select * from freedom.vacations WHERE startDate = %s or endDate = %s"
    #         params = (startDate, endDate)
    #         vacation_dictionary = self.dal.get_table(sql, (params))
    #         vacations_dict_to_obj = VacationsModel.dictionaries_to_objects_vacations(vacation_dictionary)
    #         return vacations_dict_to_obj




      



    # def count_all_vacations(self):
    #     sql = "select count(vacationId) from freedom.vacations"
    #     data = self.dal.get_scalar(sql)
    #     return data



