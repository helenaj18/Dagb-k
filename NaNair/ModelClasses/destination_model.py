class Destination:
<<<<<<< HEAD
    def __init__(self,name,airport,distance,duration,contact_name,emergency_phone_number):
        self.__name = name # 3 stafa kodi
        self.__airport = airport #
=======
    def __init__(self,name,airport,duration,distance,contact_name,emergency_phone_number):
        self.__name = name
        self.__airport = airport #3 digit code
>>>>>>> 38648b3b03c01c882f5db0317e64e72792356ac7
        self.__distance = distance
        self.__duration = duration
        self.__emergency_contact_name = contact_name
        self.__emergency_phone_number = emergency_phone_number

    def getDestinationName(self):
        return self.__name

    def getDestinationAirport(self):
        return self.__airport

    def getDestinationDistance(self):
        return self.__distance
    
    def getDestinationContact(self):
        return self.__emergency_contact_name

    def getDestinationEmergencyPhoneNumber(self):
        return self.__emergency_phone_number
    
    def getDestinationDuration(self):
        return self.__duration


    def setEmergencyContactName(self, new_name):
        self.__emergency_contact_name = new_name
    
    def setEmergencyContactPhone(self, new_phone_number):
        self.__emergency_phone_number = new_phone_number





