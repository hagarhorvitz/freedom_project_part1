from logic.users_logic import *

class UsersFacade:
    def __init__(self):
        self.logic = UsersLogic()

    def close(self):
        self.logic.close()

    def register_new_user(self, firstname, lastname, email, password, roleId):
        if not all((firstname, lastname, email, password, roleId)):
            raise ValueError("Please provide all required information correctly")
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
        if "@" not in email or "." not in email:
            raise ValueError ("Please enter valid email address")
        if len(password) < 4:
            raise ValueError ("Password's length must me at least 4 characters")
        if roleId == 1:
            raise ValueError("New user's role ID can't be 1 = Admin (Admin must entered manually only).\nPlease enter valid role ID")
        if self.logic.check_if_email_exists(email) == True:
            raise ValueError ("Can't register this email address - email is already exists in the system")
        new_user_id = self.logic.insert_new_user(firstname, lastname, email, password, roleId)
        if new_user_id > 0:
            return f"Congratulations! Your registration was successful🥳\nNew user ID: {new_user_id}"
        else:
            raise Exception("Unfortunately something went wrong...Please try again and make sure all provided information is valid (F)")

    def login_exists_user(self, email, password):
        if not all((email, password)):
            raise ValueError ("Please provide all required information correctly")
        if not isinstance(email, str):
            raise TypeError ("User's email must entered as text letters (string)")
        if not isinstance(password, str):
            raise TypeError ("User's password must entered as text letters (string)")
        if "@" not in email or "." not in email:
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
                raise Exception("Unfortunately something went wrong...Please try again and make sure all provided information is valid")
            else:
                if user.roleId == 1:
                    return (True, "Login successfully! Welcome back 😎")
                elif user.roleId != 1:
                    return (False, "Login successfully! Enjoy your visit 🤩")

