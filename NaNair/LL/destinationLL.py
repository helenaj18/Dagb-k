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
        '''Checks if given str is an int'''
        try:
            int(a_str)
            return True
        except ValueError:
            return False


    def changeDestinationFile(self, new_dest_instance):
        ''' Updates Destination file with new information '''
        return IO_API().changeDestinationFile(new_dest_instance)
