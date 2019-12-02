class DestinationLL:
    def __init__(self):
        pass
 
    def getDestination(self):
        ''' Gets destination from Destination class'''
        pass



class Destination:
    def __init__(self,name,airport,distance,contact,emergency_phone_number,duration):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration
