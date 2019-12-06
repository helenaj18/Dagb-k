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

    def changeEmergencyContactName(self,destination_name,new_emergency_contact):
        '''Changes the Emergency Contact name for destination in file'''
        destination_list = IO_API().loadDestinationFromFile()
        new_destination_list = []

        for destination in destination_list:
            if destination_name == destination.getDestinationName():
                destination.setEmergencyContactName(new_emergency_contact)
            new_destination_list.append(destination)
        
        DestinationIO().changeDestinationFile(new_destination_list)
    

    def changeEmergencyContactPhone(self,destination_name,new_emergency_phone):
        '''Changes the Emergency Contact Phone number for destination in file'''
        destination_list = IO_API().loadDestinationFromFile()
        new_destination_list = []

        for destination in destination_list:
            if destination_name == destination.getDestinationName():
                destination.setEmergencyContactPhone(new_emergency_phone)
            new_destination_list.append(destination)
            
        DestinationIO().changeDestinationFile(new_destination_list)
        


    # LINKA VIÐ EDIT_MENU DESTINATION


