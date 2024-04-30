class UsersModel:
    def __init__(self, user_id, first_name, last_name, email, password, role_id):
        self.userId = user_id
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.password = password
        self.roleId = role_id

    def __str__(self):
        return f"User Id: {self.userId}\nFull name: {self.firstname} {self.lastname}\nEmail: {self.email}\nPassword: {self.password}\nRole Id: ({self.roleId})"

    def display(self): # without password and roleId
        print(f"User Id: {self.userId}\nFull name: {self.firstname} {self.lastname}\nEmail: {self.email}")

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

    

    





    






