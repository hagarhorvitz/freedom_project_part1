import random
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

    def register_new_user(self, firstname, lastname, email, password):
        if not firstname or not lastname or not email or not password:
            raise ValueError ("Please provide all required information")
        if "@" or "." not in email:
            raise ValueError ("Please enter valid email address")
        if len(password) < 4:
            raise ValueError ("Password length must me at least 4 characters") 
        # check_email = self.logic.check_if_user_exists(email)
        if self.logic.check_if_user_exists(email) == True:
            raise ValueError ("Can't register - email already exists in the system")
        else:
            new_user = self.logic.insert_new_user(firstname, lastname, email, password, 2)
            return f"Congratulations 🥳\nYour registration was successful!\nNew user id: {new_user}"
        
    def enter_existed_user(self, email, password):
        if not email or not password:
            raise ValueError ("Please provide all required information")
        if "@" or "." not in email:
            raise ValueError ("Please enter valid email address")
        if len(password) < 4:
            raise ValueError ("Password length must me at least 4 characters")
        if self.logic.get_user_by_email_and_password(email, password) == False:
            raise ValueError ("Invalid email or password. Please try again")
        else:
            user = self.logic.get_user_by_email_and_password(email, password)
            return "Login successfully!"


    ## generate random (copied what Asaf did in his example...)
    def get_random_user(self):
        all_users = self.logic.get_all_users()
        index = random.randint(1, len(all_users))
        random_user = all_users[index]
        return random_user