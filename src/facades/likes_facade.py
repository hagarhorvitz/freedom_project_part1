from logic.likes_logic import *

## performing the actual functionality needed by the system:
class LikesFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = LikesLogic()

    ## close resources:
    def close(self):
        self.logic.close()

    ## enabling "with" keyword usage:
    def __enter__(self):
        return self
    
    ## disposing when existing "with" block:
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()

    def add_new_like(self, userId, vacationId):
        if not userId or not vacationId:
            raise ValueError ("Please provide all required information")
        if not isinstance(userId, int):
            raise ValueError ("User ID must entered as number (integer)")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        else:
            new_like = self.logic.add_like(userId, vacationId)
            if new_like == True:
                return f"Thank you for liking the vacation 👍"
            else:
                return f"We didn't get your like for some reason, please try again.\nMake sure userId and vacationId are correct"

    def unlike_vacation(self, userId, vacationId):
        if not userId or not vacationId:
            raise ValueError ("Please provide all required information")
        if not isinstance(userId, int):
            raise ValueError ("User ID must entered as number (integer)")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        else:
            unlike = self.logic.delete_like(userId, vacationId)
            if unlike == True:
                return f"Unlike successfully from user ID {userId} for vacation ID {vacationId}"
            else:
                return f"Couldn't do unlike for some reason, please try again.\nMake sure userId and vacationId are correct"


