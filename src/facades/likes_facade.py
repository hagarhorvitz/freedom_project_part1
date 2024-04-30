from logic.likes_logic import *

class LikesFacade:
    def __init__(self):
        self.logic = LikesLogic()

    def close(self):
        self.logic.close()

    ### 1. add raise/if if userid/vacationid not existed? - then need to write function for it... ###
    def add_new_like(self, userId, vacationId):
        if not userId or not vacationId:
            raise ValueError ("Please provide all required information")
        if not isinstance(userId, int):
            raise ValueError ("User ID must entered as number (integer)")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        new_like = self.logic.add_like(userId, vacationId)
        if new_like == True:
            return f"Thank you for liking the vacation 👍"
        elif new_like == False: 
            raise ValueError("We didn't get your like for some reason, please try again.\nMake sure userId and vacationId are correct")

    ### 1. add raise/if if userid/vacationid not existed? - then need to write function for it... ###
    def unlike_vacation(self, userId, vacationId):
        if not userId or not vacationId:
            raise ValueError ("Please provide all required information")
        if not isinstance(userId, int):
            raise ValueError ("User ID must entered as number (integer)")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        unlike = self.logic.delete_like(userId, vacationId)
        if unlike == True:
            return f"Unlike successfully from user ID {userId} for vacation ID {vacationId}"
        elif unlike == False:
            raise ValueError("Sorry, something is wrong...couldn't unlike for some reason, please try again.\nMake sure userId and vacationId are correct")




