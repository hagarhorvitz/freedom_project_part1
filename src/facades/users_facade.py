from logic.users_logic import *

class UsersFacade:
    def __init__(self):
        self.logic = UsersLogic()

    def close(self):
        self.logic.close()

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
        if self.logic.check_if_email_exists(email) == True:
            raise ValueError ("Can't register this email address - email is already exists in the system")
        new_user_id = self.logic.insert_new_user(firstname, lastname, email, password, roleId)
        if new_user_id == False:
            raise ValueError("Unfortunately something went wrong...Please try again and make sure all provided information is valid")
        else:
            return f"Congratulations! Your registration was successful🥳\nNew user ID: {new_user_id}"

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
