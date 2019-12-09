from API.IO_API import IO_API
from IO.destinationIO import DestinationIO
from ModelClasses.destination_model import Destination
from LL.airplaneLL import AirplaneLL

class DestinationLL:

    def getDestination(self): 
        ''' Gets destination from Destination class'''

        return IO_API().loadDestinationFromFile()

    def addDestination(self,new_destination):
        '''Gets information about a new destination
           and adds it to destination file'''
        IO_API().addDestinationToFile(new_destination)


    def checkIfInt(self,a_str):
        try:
            int(a_str)
            return True
        except ValueError:
            return False


    def changeEmergencyContactName(self,destination_name,new_emergency_contact):
        '''Changes the Emergency Contact name for destination in file'''
        destination_list = IO_API().loadDestinationFromFile()
        new_destination_list = []

        #Reads every line until it finds the same name of the airport as the input (destinantion_name)
        #and then changes the airports emergency contact to the same as the input (new_emergency_contact)
        for destination in destination_list:
            if destination_name == destination.getDestinationAirport():
                destination.setEmergencyContactName(new_emergency_contact)
            new_destination_list.append(destination)

        #Sends destination list to DestinationIO to overwrite the file with new information       
        DestinationIO().changeDestinationFile(new_destination_list)
    

    def changeEmergencyContactPhone(self,destination_name,new_emergency_phone):
        '''Changes the Emergency Contact Phone number for destination in file'''
        destination_list = IO_API().loadDestinationFromFile()
        new_destination_list = []

        #Reads every line until it finds the same name of the airport as the input (destinantion_name)
        #and then changes the airports emergency phone number to the same as the input (new_emergency_phone)
        for destination in destination_list:
            if destination_name == destination.getDestinationAirport():
                destination.setEmergencyContactPhone(new_emergency_phone)
            new_destination_list.append(destination)
        
        #Sends destination list to DestinationIO to overwrite the file with new information
        DestinationIO().changeDestinationFile(new_destination_list)
        





