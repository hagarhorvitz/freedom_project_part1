class VacationsModel:
    def __init__(self, vacation_id,country_id, vacation_info, start_date, end_date, price, photo_file_name):
        self.vacationId = vacation_id
        self.countryId = country_id
        self.vacationInfo = vacation_info
        self.startDate = start_date
        self.endDate = end_date
        self.price = price
        self.photoFileName = photo_file_name

    def __str__(self):
        return f"Vacation Id: # {self.__vacationId} / Country Id: # {self.__countryId}\nVacation description: {self.__vacationInfo}\nStart & end dates: {self.__startDate} - {self.__endDate}\nTotal price: {self.__price}\nPhoto file: {self.__photoFileName}"
    
    def display (self): #without photo file name
        print(f"Vacation Id: # {self.__vacationId} / Country Id: # {self.__countryId}\nVacation description: {self.__vacationInfo}\nStart & end dates: {self.__startDate} - {self.__endDate}\nTotal price: {self.__price}")

    @property  
    def vacationId(self):
        return self.__vacationId
    @vacationId.setter
    def vacationId(self, value):
        self.__vacationId = value
    
    @property
    def countryId(self):
        return self.__countryId  
    @countryId.setter
    def countryId(self, value):
        self.__countryId = value

    @property
    def vacationInfo(self):
        return self.__vacationInfo   
    @vacationInfo.setter
    def vacationInfo(self, value):
        self.__vacationInfo = value

    @property
    def startDate(self):
        return self.__startDate   
    @startDate.setter
    def startDate(self, value):
        self.__startDate = value

    @property
    def endDate(self):
        return self.__endDate    
    @endDate.setter
    def endDate(self, value):
        self.__endDate = value

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def photoFileName(self):
        return self.__photoFileName  
    @photoFileName.setter
    def photoFileName(self, value):
        self.__photoFileName = value
    
    @staticmethod
    def dictionary_to_one_object_vacation(dictionary):
        vacationId = dictionary["vacationId"]
        countryId = dictionary["countryId"]
        vacationInfo = dictionary["vacationInfo"]
        startDate = dictionary["startDate"]
        endDate = dictionary["endDate"]
        price = dictionary["price"]
        photoFileName = dictionary["photoFileName"]
        vacation_object = VacationsModel(vacationId, countryId, vacationInfo, startDate, endDate, price, photoFileName)
        return vacation_object
    
    @staticmethod
    def dictionaries_to_objects_vacations(list_of_dictionaries):
        vacations = []
        for item in list_of_dictionaries:
            vacation = VacationsModel.dictionary_to_one_object_vacation(item)
            vacations.append(vacation)
        return vacations

