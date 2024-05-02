from logic.users_logic import *
from logic.vacations_logic import *
from logic.roles_logic import *
from logic.likes_logic import *
from logic.countries_logic import *
from tests.test import *

# # using the facade to perform the needed functionality of the system"
# with VacationsFacade() as facade:
#     ## get a random
#     random_vacation = facade.get_random_vacation()
#     print(random_vacation)

## vacations_logic
# vacation = VacationsLogic()
# all_vacations = vacation.get_all_vacations()
# vacation.display_vacations(all_vacations)
# vacation.close()

# vacations_ordered = VacationsLogic()
# by_startDate = vacations_ordered.get_all_vacations_ordered("startDate")
# vacations_ordered.display_vacations(by_startDate)
# # by_order = vacations_ordered.get_all_vacations_ordered("user")
# # vacations_ordered.display_vacations(by_order)
# vacations_ordered.close()

# vacation = VacationsLogic()
# new_vacation = vacation.insert_new_vacation(5, "Want to have a perfect getaway from school and have the time of your life? We have special deals for winter break in sunny, exotic Cancun, Mexico!! Sun, amazing beaches, alcohol, party day and night!", "2024-12-19", "2024-12-29", 16900, "photo_of_beach_party")
# print(new_vacation)
# vacation.close()



## users_logic
# users = UsersLogic()
# all_users = users.get_all_users()
# users.display_users(all_users)
# users.close()

# user = UsersLogic()
# new_user = user.insert_new_user("Shraga", "Horvitz", "shragi@gmail.com", "mylove111", 2)
# print(new_user)
# user.close()

# user = UsersLogic()
# check_email = user.check_if_email_exists("gali@gmail.com")
# print(check_email)
# user.close()

# user = UsersLogic()
# user_by_email_and_password = user.get_user_by_email_and_password("gali@gmail.com", "mona123")
# print(user_by_email_and_password)
# print(f"user role id3: {user_by_email_and_password.userId}")
# user.close()



## roles_logic
# roles = RolesLogic()
# all_roles = roles.get_all_roles()
# roles.display_roles(all_roles)
# roles.close()

# role = RolesLogic()
# by_id = role.get_one_role_by_id(2)
# print(by_id)
# role.close()

# role = RolesLogic()
# by_name = role.get_one_role_by_name("Admin")
# print(by_name)
# role.close()



## likes_logic
# likes = LikesLogic()
# all_likes = likes.get_all_likes()
# likes.display_likes(all_likes)
# likes.close()

# like = LikesLogic()
# add_like = like.add_like(3, 7)
# print(add_like)
# like.close()

# delete = LikesLogic() 
# unlike = delete.delete_like(3,7)
# print(unlike)
# delete.close()



## countries_logic
# countries = CountriesLogic()
# all_countries = countries.get_all_countries()
# countries.display_countries(all_countries)
# countries.close()

# country = CountriesLogic()
# by_id = country.get_one_country_by_id(5)
# print(by_id)
# country.close()

# country = CountriesLogic()
# by_name = country.get_one_country_by_name("Panama")
# print(by_name)
# country.close()


# ## test
# test = Test()
# test.add_new_vacation_test()
# test.close()

