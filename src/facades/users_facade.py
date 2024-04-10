import random
from logic.users_logic import *
from models.users_model import *

## performing the actual functionality needed by the system:
class UsersFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = UsersLogic()

    ## generate random (copied what Asaf did in his example...)
    def get_random_user(self):
        all_users = self.logic.get_all_users()
        index = random.randint(1, len(all_users))
        random_user = all_users[index]
        return random_user

    ## close resources:
    def close(self):
        self.logic.close()

    ## enabling "with" keyword usage:
    def __enter__(self):
        return self
    
    ## disposing when existing "with" block:
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()