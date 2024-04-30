from utils.dal import *
from models.vacations_model import *

class VacationsLogic:
    def __init__(self):
        self.dal = DAL()
    
    def close(self):
        self.dal.close()

    @staticmethod
    def display_vacations(sql_result):
        for item in sql_result:
            print(f"{item}\n{"="*40}")

    def get_all_vacations(self):
        sql = "select * from freedom.vacations" 
        vacations_data_dictionary = self.dal.get_table(sql)
        vacations_data_dict_to_obj = VacationsModel.dictionaries_to_objects_vacations(vacations_data_dictionary)
        return vacations_data_dict_to_obj

    def get_one_vacation(self):
        sql = "select * from freedom.vacations limit 1"
        vacation_data_dictionary = self.dal.get_scalar(sql)
        vacation_data_dict_to_obj = VacationsModel.dictionary_to_one_object_vacation(vacation_data_dictionary)
        return vacation_data_dict_to_obj

    def get_all_vacations_ordered(self, order_by):
        allowed_columns_as_parameter = ["vacationId", "countryId", "vacationInfo", "startDate", "endDate", "price", "photoFileName"]
        if order_by not in allowed_columns_as_parameter:
            raise ValueError("Invalid column name to order by")
        else:
            sql = f"select * from freedom.vacations order by {order_by}" 
            vacations_data_dictionary = self.dal.get_table(sql)
            vacations_data_dict_to_obj = VacationsModel.dictionaries_to_objects_vacations(vacations_data_dictionary)
            return vacations_data_dict_to_obj
    #################################################
    # def get_all_vacations_ordered(self, order_by):
    #     sql = "SELECT * FROM freedom.vacations ORDER BY %s"
    #     params = (order_by, )
    #     vacations_data_dictionary = self.dal.get_table(sql, (params))
    #     vacations_data_dict_to_obj = VacationsModel.dictionaries_to_objects_vacations(vacations_data_dictionary)
    #     return vacations_data_dict_to_obj
    ### didn't work the way above, something between the sql... ###
    #################################################

    def insert_new_vacation(self, countryId, vacationInfo, startDate, endDate, price, photoFileName): 
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







