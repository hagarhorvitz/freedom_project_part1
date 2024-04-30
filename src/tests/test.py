from facades.users_facade import *
from facades.vacations_facade import *
from facades.likes_facade import *
from facades.countries_facade import *
from facades.roles_facade import *

#################################################
### do try and except ### ✅
### change "with" move to the app.py and exit/enter to all here ### ✅
### enter hard-coded info as "test" (new, update, delete) ###
#################################################

class Test:
    def __init__(self):
        self.users_facade = UsersFacade()
        self.vacations_facade = VacationsFacade()
        self.likes_facade = LikesFacade()
        self.countries_facade = CountriesFacade()
        self.roles_facade = RolesFacade()
    
    def add_new_user_test(self):
        try:
            new_user = self.users_facade.register_new_user("Shraga", "Horvitz", "shragi@gmail.com", "mylove111", 2)
            print(new_user)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.users_facade.close()

    def login_user_test(self):
        try:
            user = self.users_facade.login_exists_user("gali@gmail.com", "mona123")
            print(user)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.users_facade.close()

    def get_all_vacations_by_startDate_test(self):
        try:
            all_vacations = self.vacations_facade.get_all_vacations_by_startDate()
            print(all_vacations)
        except Exception as err:
            print("General error:", err)
        finally:
            self.vacations_facade.close()
        
    def add_new_vacation_test(self):
        try:
            new_vacation = self.vacations_facade.add_new_vacation(1, "vacationInfo", "startDate YYYY-MM-DD", "endDate YYYY-MM-DD", 100, "photoFileName")
            print(new_vacation)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.vacations_facade.close()

    def update_vacation_test(self):
        try:
            vacation = self.vacations_facade.update_exist_vacation(1, "vacationInfo", "startDate YYYY-MM-DD", "endDate YYYY-MM-DD", 100, 2)
            print(vacation)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.vacations_facade.close()

    def delete_vacation_test(self):
        try:
            delete_vacation = self.vacations_facade.delete_vacation(4)
            print(delete_vacation)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.vacations_facade.close()

    def add_like_test(self):
        try:
            like = self.likes_facade.add_new_like(4, 8)
            print(like)
        except ValueError as err:
            print("Value error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.likes_facade.close()

    def unlike_vacation_test(self):
        try:
            unlike = self.likes_facade.unlike_vacation(4, 8)
            print(unlike)
        except ValueError as err:
            print("Value error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.likes_facade.close()

#################################################
    def test_all(self):
        self.add_new_user_test()
        self.login_user_test()
        self.get_all_vacations_by_startDate_test()
        self.add_new_vacation_test()
        self.update_vacation_test()
        self.delete_vacation_test()
        self.add_like_test()
        self.unlike_vacation_test()
#################################################

    def close(self):
        self.users_facade.close()
        self.vacations_facade.close()
        self.likes_facade.close()
        self.countries_facade.close()
        self.roles_facade.close()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()


# def test_all(self):
#         try:
#             self.add_user_test()
#         except ValueError as e:
#             print(e)

#         try:
#             self.get_user_test()
#         except ValueError as e:
#             print(e)

#         try:
#             self.get_all_vacations_test()
#         except ValueError as e:
#             print(e)

#         try:
#             self.add_vacation_test()
#         except ValueError as e:
#             print(e)

#         try:
#             self.del_vacation_test()
#         except ValueError as e:
#             print(e)

#         try:
#             self.add_like_test()
#         except ValueError as e:
#             print(e)

#         try:
#             self.del_like_test()
#         except ValueError as e:
            # print(e)

