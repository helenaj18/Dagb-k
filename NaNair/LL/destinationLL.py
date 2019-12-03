from API.IO_API import IO_API

class DestinationLL:
    def __init__(self):
        pass
 
    def getDestination(self):
        ''' Gets destination from Destination class'''
        destinations_set = IO_API().loadDestinationFromFile()
        
        return destinations_set

    def changeDestination(self,destination_name, new_emergency_phone):
        pass 
    # ÞARF AÐ VERA ANNAÐ HVORT NAME EÐA PHONE 
    # LINKA VIÐ EDIT_MENU DESTINATION


class Destination:
    def __init__(self,name,airport,distance,contact,emergency_phone_number,duration):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration


