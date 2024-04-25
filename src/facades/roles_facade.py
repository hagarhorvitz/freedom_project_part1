import random
from logic.roles_logic import *

## performing the actual functionality needed by the system:
class RolesFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = RolesLogic()
    
    ## close resources:
    def close(self):
        self.logic.close()

    ## enabling "with" keyword usage:
    def __enter__(self):
        return self
    
    ## disposing when existing "with" block:
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()

    ## generate random (copied what Asaf did in his example...)
    def get_random_role(self):
        all_roles = self.logic.get_all_roles()
        index = random.randint(1, len(all_roles))
        random_role = all_roles[index]
        return random_role
