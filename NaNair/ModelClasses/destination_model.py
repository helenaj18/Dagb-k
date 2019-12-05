class Destination:
    def __init__(self,name,airport,distance,duration,contact,emergency_phone_number,):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration

    def getDestinationName(self):
        return self.__name

    def getDestinationAirport(self):
        return self.__airport

    def getDestinationDistnace(self):
        return self.__distance
    
    def getDestinationContact(self):
        return self.__contact

    def getDestinationEmergencyPhoneNumber(self):
        return self.__emergency_phone_number
    
    def getDestinationDuration(self):
        return self.__duration





