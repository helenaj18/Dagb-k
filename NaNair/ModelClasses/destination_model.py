class Destination:
    def __init__(self,name,airport,duration,distance,contact_name,emergency_phone_number):
        self.__name = name
        self.__airport = airport # 3 digit code
        self.__distance = distance
        self.__duration = duration
        self.__emergency_contact_name = contact_name
        self.__emergency_phone_number = emergency_phone_number

    # GET METHODS
    
    def getDestinationName(self):
        '''Gets destination name'''
        return self.__name

    def getDestinationAirport(self):
        '''Gets destination airport'''
        return self.__airport

    def getDestinationDistance(self):
        '''Gets destination distance'''
        return self.__distance
    
    def getDestinationContact(self):
        '''Gets destination emergency contact name'''
        return self.__emergency_contact_name

    def getDestinationEmergencyPhoneNumber(self):
        '''Gets destination emergency contact phone number'''
        return self.__emergency_phone_number
    
    def getDestinationDuration(self):
        '''Gets destination duration'''
        return self.__duration

    # SET METHODS

    def setEmergencyContactName(self, new_name):
        '''Sets new emergency contact's name'''
        self.__emergency_contact_name = new_name
    
    def setEmergencyContactPhone(self, new_phone_number):
        '''Sets emergency contact's new phone number'''
        self.__emergency_phone_number = new_phone_number





