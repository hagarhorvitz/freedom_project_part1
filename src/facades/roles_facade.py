from logic.roles_logic import *

class RolesFacade:
    def __init__(self):
        self.logic = RolesLogic()
    
    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()
