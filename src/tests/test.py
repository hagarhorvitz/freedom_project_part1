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
            args = ("Yosef", "Gerama", "y@gmail.com", "yosef5151", 5)
            if len(args) != 5:
                raise ValueError("Please provide all required information")
            new_user = self.users_facade.register_new_user(*args)
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
            args = ("gali@gmail.com", "mona123")
            if len(args) != 2:
                raise ValueError("Please provide all required information")
            user_roleId, message = self.users_facade.login_exists_user(*args)
            print(message)
            return user_roleId
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
            args = ("startDate", )
            if len(args) != 1:
                raise ValueError("Please provide all required information")
            all_vacations = self.vacations_facade.all_vacations_ordered(*args)
            print(all_vacations)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.vacations_facade.close()
        
    def add_new_vacation_test(self):
        permission = self.login_user_test()
        if permission == False:
            print(f"{"*"*40}\nAccess denied!\nUser is not authorized for this action\n{"*"*40}")
        elif permission == True:
            try:
                args = (1, "vacationInfo", "startDate YYYY-MM-DD", "endDate YYYY-MM-DD",100,  "photoFileName")
                if len(args) != 6:
                    raise ValueError("Please provide all required information")
                new_vacation = self.vacations_facade.add_new_vacation(*args)
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
        permission = self.login_user_test()
        if permission == False:
            print(f"{"*"*40}\nAccess denied!\nUser is not authorized for this action\n{"*"*40}")
        elif permission == True:
            try:
                args = (1, "vacationInfo", "startDate YYYY-MM-DD", "endDate YYYY-MM-DD", 100, 2)
                if len(args) != 6:
                    raise ValueError("Please provide all required information")
                vacation = self.vacations_facade.update_exist_vacation(*args)
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
        permission = self.login_user_test()
        if permission == False:
            print(f"{"*"*40}\nAccess denied!\nUser is not authorized for this action\n{"*"*40}")
        elif permission == True:
            try:
                args = (4,)
                if len(args) != 1:
                    raise ValueError("Please provide all required information")
                delete_vacation = self.vacations_facade.delete_vacation(*args)
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
            args = (4, 8)
            if len(args) != 2:
                raise ValueError("Please provide all required information")
            like = self.likes_facade.add_new_like(*args)
            print(like)
        except ValueError as err:
            print("Value error:", err)
        except Exception as err:
            print("General error:", err)
        finally:
            self.likes_facade.close()

    def unlike_vacation_test(self):
        try:
            args = (4, 8)
            if len(args) != 2:
                raise ValueError("Please provide all required information")
            unlike = self.likes_facade.unlike_vacation(*args)
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

