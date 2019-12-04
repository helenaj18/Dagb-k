from API.IO_API import IO_API
from IO.destinationIO import DestinationIO

DESTINATION_NAME_const = 1
EMERGENCY_CONTACT_NAME_const = 5
EMERGENCY_CONTACT_PHONE_const = 6

class DestinationLL:
    def __init__(self):
        self.__destination_list = IO_API().loadDestinationFromFile()
 

    def getDestination(self): #skoða, þarf þetta að vera sér fall?
        ''' Gets destination from Destination class'''

        return self.__destination_list


    def changeEmergencyContactName(self,destination_name,new_emergency_contact):
        '''Changes the Emergency Contact name for destination in file'''

        for i in range(len(self.__destination_list)):
            if destination_name == self.__destination_list[i][DESTINATION_NAME_const]:
                self.__destination_list[i][EMERGENCY_CONTACT_NAME_const] = new_emergency_contact
        
        DestinationIO().changeDestinationFile(self.__destination_list)
    

    def changeEmergencyContactPhone(self,destination_name,new_emergency_phone):
        '''Changes the Emergency Contact Phone number for destination in file'''
        
        for i in range(len(self.__destination_list)):
            if destination_name == self.__destination_list[i][DESTINATION_NAME_const]:
                self.__destination_list[i][EMERGENCY_CONTACT_PHONE_const] = new_emergency_phone
        
        DestinationIO().changeDestinationFile(self.__destination_list)

    # LINKA VIÐ EDIT_MENU DESTINATION


class Destination:
    def __init__(self,name,airport,distance,contact,emergency_phone_number,duration):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration