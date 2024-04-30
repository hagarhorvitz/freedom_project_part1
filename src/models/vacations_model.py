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
        return f"Vacation Id: # {self.vacationId} / Country Id: # {self.countryId}\nVacation description: {self.vacationInfo}\nStart & end dates: {self.startDate} - {self.endDate}\nTotal price: {self.price}\nPhoto file: {self.photoFileName}"
    
    def display (self): #without photo file name
        print(f"Vacation Id: # {self.vacationId} / Country Id: # {self.countryId}\nVacation description: {self.vacationInfo}\nStart & end dates: {self.startDate} - {self.endDate}\nTotal price: {self.price}")

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

