class CountriesModel:
    def __init__(self, country_id, country_name):
        self.countryId = country_id
        self.countryName = country_name

    def __str__(self):
        return f"Country Id: {self.__countryId} - Country: {self.__countryName}"
    
    @property
    def countryId(self):
        return self.__countryId
    @countryId.setter
    def countryId(self, value):
        self.__countryId = value

    @property
    def countryName(self):
        return self.__countryName
    @countryName.setter
    def countryName(self, value):
        self.__countryName = value

    @staticmethod
    def dictionary_to_one_object_country(dictionary):
        countryId = dictionary["countryId"]
        countryName = dictionary["countryName"]
        country_object = CountriesModel(countryId, countryName)
        return country_object
    
    @staticmethod
    def dictionaries_to_objects_countries(list_of_dictionaries):
        countries = []
        for item in list_of_dictionaries:
            country = CountriesModel.dictionary_to_one_object_country(item)
            countries.append(country)
        return countries



