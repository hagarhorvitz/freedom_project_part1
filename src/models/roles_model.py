class RolesModel:
    def __init__(self, role_id, role_name) :
        self.roleId = role_id
        self.roleName = role_name

    def __str__(self):
        return f"Role info:\nId: {self.__roleId} - Name: {self.__roleName}"
    
    @property
    def roleId(self):
        return self.__roleId
    @roleId.setter
    def roleId(self, value):
        self.__roleId = value
    
    @property
    def roleName(self):
        return self.__roleName
    @roleName.setter
    def roleName(self, value):
        self.__roleName = value

    @staticmethod
    def dictionary_to_one_object_role(dictionary):
        roleId = dictionary["roleId"]
        roleName = dictionary["roleName"]
        role_object = RolesModel(roleId, roleName)
        return role_object
    
    @staticmethod
    def dictionaries_to_objects_roles(list_of_dictionaries):
        roles = []
        for item in list_of_dictionaries:
            role = RolesModel.dictionary_to_one_object_role(item)
            roles.append(role)
        return roles