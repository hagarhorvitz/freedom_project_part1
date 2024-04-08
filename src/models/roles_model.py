class RolesModel:
    def __init__(self, role_id, role_name) :
        self.roleId = role_id
        self.roleName = role_name

    def __str__(self):
        return f"Role info:\nId: {self.roleId} - Name: {self.roleName}\n{"="*12}"
    
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