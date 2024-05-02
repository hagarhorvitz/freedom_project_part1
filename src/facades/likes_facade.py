from logic.likes_logic import *

class LikesFacade:
    def __init__(self):
        self.logic = LikesLogic()

    def close(self):
        self.logic.close()

    def add_new_like(self, userId, vacationId):
        if not all((userId, vacationId)):
            raise ValueError ("Please provide all required information correctly")
        if not isinstance(userId, int):
            raise ValueError ("User ID must entered as number (integer)")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        new_like = self.logic.add_like(userId, vacationId)
        if new_like == True:
            return f"Thank you for liking the vacation 👍"
        else:
            raise Exception("We didn't get your like for some reason, please try again.\nMake sure userId and vacationId are correct")

    def unlike_vacation(self, userId, vacationId):
        if not all((userId, vacationId)):
            raise ValueError ("Please provide all required information correctly")
        if not isinstance(userId, int):
            raise ValueError ("User ID must entered as number (integer)")
        if not isinstance(vacationId, int):
            raise ValueError ("Vacation ID must entered as number (integer)")
        unlike = self.logic.delete_like(userId, vacationId)
        if unlike > 0:
            return f"Unlike successfully from user ID {userId} for vacation ID {vacationId}"
        else:
            raise Exception("Sorry, something is wrong...couldn't unlike for some reason, please try again.\nMake sure userId and vacationId are correct")




