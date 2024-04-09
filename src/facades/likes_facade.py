import random
from logic.likes_logic import *

## performing the actual functionality needed by the system:
class LikesFacade:
    ## constructor - creating a business logic object:
    def __init__(self):
        self.logic = LikesLogic()

    ## generate random (copied what Asaf did in his example...)
    def get_random_like(self):
        all_likes = self.logic.get_all_likes()
        index = random.randint(1, len(all_likes))
        random_like = all_likes[index]
        return random_like
    
    ## close resources:
    def close(self):
        self.logic.close()

    ## enabling "with" keyword usage:
    def __enter__(self):
        return self
    
    ## disposing when existing "with" block:
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()
