class LikesModel:
    def __init__(self, user_id, vacation_id):
        self.userId = user_id
        self.vacationId = vacation_id

    def __str__(self):
        return f"Like info:\nUser Id: {self.__userId} - Vacation Id: {self.__vacationId}"
    
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, value):
        self.__userId = value

    @property
    def vacationId(self):
        return self.__vacationId
    @vacationId.setter
    def vacationId(self, value):
        self.__vacationId = value

    @staticmethod
    def dictionary_to_one_object_like(dictionary):
        userId = dictionary["userId"]
        vacationId = dictionary["vacationId"]
        like_object = LikesModel(userId, vacationId)
        return like_object
    
    @staticmethod
    def dictionaries_to_objects_likes(list_of_dictionaries):
        likes = []
        for item in list_of_dictionaries:
            like = LikesModel.dictionary_to_one_object_like(item)
            likes.append(like)
        return likes