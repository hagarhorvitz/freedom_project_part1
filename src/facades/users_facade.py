# import random
from logic.users_logic import *
from models.users_model import *

## performing the actual functionality needed by the system:
class UsersFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = UsersLogic()

    ## close resources:
    def close(self):
        self.logic.close()

    ## enabling "with" keyword usage:
    def __enter__(self):
        return self
    
    ## disposing when existing "with" block:
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()

    # make sure it works #
    ### 1. add raise if roleId = 1 (Admin) or to set roleId as 2 in the params/values? - for now, i did raise... ###
    def register_new_user(self, firstname, lastname, email, password, roleId):
        if not firstname or not lastname or not email or not password or not roleId:
            raise ValueError ("Please provide all required information")
        if not isinstance(firstname, str):
            raise TypeError ("User's first name must entered as text letters (string)")
        if not isinstance(lastname, str):
            raise TypeError ("User's last name must entered as text letters (string)")
        if not isinstance(email, str):
            raise TypeError ("User's email must entered as text letters (string)")
        if not isinstance(password, str):
            raise TypeError ("User's password must entered as text letters (string)")
        if not isinstance(roleId, int):
            raise TypeError ("User's role ID must entered as number (integer)")
        if "@" or "." not in email:
            raise ValueError ("Please enter valid email address")
        if len(password) < 4:
            raise ValueError ("Password's length must me at least 4 characters")
        if roleId == 1:
            raise ValueError("New user's role ID can't be 1 = Admin (Admin must entered manually only).\nPlease enter valid role ID")
        check_email = self.logic.check_if_email_exists(email)
        if check_email == True:
            raise ValueError ("Can't register this email address - email is already exists in the system")
        else:
            new_user_id = self.logic.insert_new_user(firstname, lastname, email, password, roleId)
            if new_user_id == False:
                raise ValueError("Unfortunately something went wrong...Please try again and make sure all provided information is valid")
            else:
                return f"Congratulations! Your registration was successful🥳\nNew user ID: {new_user_id}"

    # make sure it works #
    ### 1. add raise if roleId = 1 (Admin) or to set roleId as 2 in the params/values? - for now, i did raise... ###
    ### 2. in the return successful, do a return just "login successfully" or also return user info? ###
    ### 3. should we add raise if password wrong? and then we need function fot it... ###
    def login_exists_user(self, email, password):
        if not email or not password:
            raise ValueError ("Please provide all required information")
        if not isinstance(email, str):
            raise TypeError ("User's email must entered as text letters (string)")
        if not isinstance(password, str):
            raise TypeError ("User's password must entered as text letters (string)")
        if "@" or "." not in email:
            raise ValueError ("Please enter valid email address")
        if len(password) < 4:
            raise ValueError ("Password's length must me at least 4 characters")
        check_email = self.logic.check_if_email_exists(email)
        if check_email == False:
            raise ValueError ("Email is not in the system, please try again")
        if self.logic.get_user_by_email_and_password(email, password) == False:
            raise ValueError ("Invalid email or password. Please try again")
        else:
            user = self.logic.get_user_by_email_and_password(email, password)
            if user == False:
                raise ValueError("Unfortunately something went wrong...Please try again and make sure all provided information is valid")
            else:
                return "You just logged in successfully!👌"
                # return f"You just logged in successfully!👌\n{user}"


    # ## generate random (copied what Asaf did in his example...)
    # def get_random_user(self):
    #     all_users = self.logic.get_all_users()
    #     index = random.randint(1, len(all_users))
    #     random_user = all_users[index]
    #     return random_user