from API.IO_API import IO_API
from IO.destinationIO import DestinationIO

DESTINATION_NAME_const = 1
EMERGENCY_CONTACT_NAME_const = 5
EMERGENCY_CONTACT_PHONE_const = 6

class DestinationLL:

    def getDestination(self): #skoða, þarf þetta að vera sér fall?
        ''' Gets destination from Destination class'''

        return IO_API().loadDestinationFromFile()

    def getAirport(self, dest_code):
        destinations_instances = self.getDestination()

        for destination in destinations_instances:
            if dest_code == destination.getDestinationName():
                return destination.getDestinationAirport()


# Geyma change þangað til við erum búin með get

    # def changeEmergencyContactName(self,destination_name,new_emergency_contact):
    #     '''Changes the Emergency Contact name for destination in file'''

    #     for i in range(len(self.__destination_list)):
    #         if destination_name == self.__destination_list[i][DESTINATION_NAME_const]:
    #             self.__destination_list[i][EMERGENCY_CONTACT_NAME_const] = new_emergency_contact
        
    #     DestinationIO().changeDestinationFile(self.__destination_list)
    

    # def changeEmergencyContactPhone(self,destination_name,new_emergency_phone):
    #     '''Changes the Emergency Contact Phone number for destination in file'''
        
    #     for i in range(len(self.__destination_list)):
    #         if destination_name == self.__destination_list[i][DESTINATION_NAME_const]:
    #             self.__destination_list[i][EMERGENCY_CONTACT_PHONE_const] = new_emergency_phone
        
    #     DestinationIO().changeDestinationFile(self.__destination_list)

    # LINKA VIÐ EDIT_MENU DESTINATION


