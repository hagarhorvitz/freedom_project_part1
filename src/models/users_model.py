class UsersModel:
    def __init__(self, user_id, first_name, last_name, email, password, role_id):
        self.userId = user_id
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.password = password
        self.roleId = role_id

    def __str__(self):
        return f"User Id: {self.__userId}\nFull name: {self.__firstname} {self.__lastname}\nEmail: {self.__email}\nPassword: {self.__password}\nRole Id: ({self.__roleId})"

    def display(self): # without password and roleId
        print(f"User Id: {self.__userId}\nFull name: {self.__firstname} {self.__lastname}\nEmail: {self.__email}")

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, value):
        self.__userId = value

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname 
    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def roleId(self):
        return self.__roleId
    @roleId.setter
    def roleId(self, value):
        self.__roleId = value

    @staticmethod
    def dictionary_to_one_object_user(dictionary):
        userId = dictionary["userId"]
        firstname = dictionary["firstname"]
        lastname = dictionary["lastname"]
        email = dictionary["email"]
        password = dictionary["password"]
        roleId = dictionary["roleId"]
        user_object = UsersModel(userId, firstname, lastname, email, password, roleId)
        return user_object
    
    @staticmethod
    def dictionaries_to_objects_users(list_of_dictionaries):
        users = []
        for item in list_of_dictionaries:
            user = UsersModel.dictionary_to_one_object_user(item)
            users.append(user)
        return users
    
    

    

    





    






