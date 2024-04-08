class CountriesModel:
    def __init__(self, country_id, country_name):
        self.countryId = country_id
        self.countryName = country_name

    def __str__(self):
        return f"Country info:\nId: {self.countryId} - Name: {self.countryName}\n{"="*12}"
    
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



