from utils.dal import *
from models.users_model import *
from logic.users_logic import *
from models.vacations_model import *
from logic.vacations_logic import *
# from facades.vacations_facade import *

# ## utils.dal
# a = DAL()
# sql = "select * from freedom.countries"
# results = a.get_table(sql, )
# print(results)
# a.close()

# ## users_model
# data = DAL()
# sql = "select * from freedom.users"
# dict_results = data.get_table(sql)
# obj_results = UsersModel.dictionaries_to_objects_users(dict_results)
# for user in obj_results:
#     print(user)
# data.close()

# ## users_logic
# users = UsersLogic()
# all_users = users.get_all_users()
# users.display_users(all_users)
# ## users.display_users(users.get_all_users()) - another option ##
# users.close()

# ## vacations_model
# vacations = VacationsLogic()
# count_vacation = vacations.count_all_vacations()
# print(count_vacation)

# ## vacations_logic
## using the facade to perform the needed functionality of the system"
# with VacationsFacade() as facade:
#     ## get a random
#     random_vacation = facade.get_random_vacation()
#     print(random_vacation)

# ## users_logic
# user = UsersLogic()
# new_user = user.insert_new_user(Or, "B", "ori@gmail.com", "ori555", "2")
# print(new_user)
# user.close()

# ## users_logic
# user1 = UsersLogic()
# one_user = user1.get_one_user()
# one_user.display() #option 1
# print(one_user) #option 2
# user1.close()

# ## users_logic
# user_logic = UsersLogic()
# user = user_logic.get_user_by_email_and_password("gali@gmail.com", "mona123")
# print(user)
# user_logic.close()

# ## users_logic
# user_logic = UsersLogic()
# user = user_logic.check_if_user_exists("ga@gmail.com")
# print(user)
# user_logic.close()

# ## vacations_logic
# vacation_logic = VacationsLogic()
# all_vacations = vacation_logic.get_all_vacations()
# vacation_logic.display_vacations(all_vacations)
# vacation_logic.close()

# ## vacations_logic
# vacation_data = VacationsLogic()
# new_vacation = vacation_data.insert_new_vacation(5, "Want to have a perfect getaway from school and have the time of your life? We have special deals for winter break in sunny, exotic Cancun, Mexico!! Sun, amazing beaches, alcohol, party day and night!", "2024-12-19", "2024-12-29", 16900, "photo_of_beach_party")
# print(new_vacation)
# vacation_data.close()

# ## vacations_logic
# vacations = VacationsLogic()
# by_startDate = vacations.get_all_vacations_ordered("startDate")
# # by_startDate = vacations.get_all_vacations_ordered("user")
# vacations.display_vacations(by_startDate)
# vacations.close()

# ## vacations_logic
# vacations = VacationsLogic()
# check_date = vacations.check_vacation("2024-05-22", "2024-07-20")
# vacations.display_vacations(check_date)
# vacations.close()









