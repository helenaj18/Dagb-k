import os
from ModelClasses.destination_model import Destination
import csv 

class DestinationIO:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__destination_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Destinations.csv')

        
        self.loadDestinationFromFile()

    def loadDestinationFromFile(self):
        '''Reads file and returns destination list'''
        destination_file = open(self.__destination_filename,'r')
        destination_list = []
        i = 0
        for line in destination_file:
            if i != 0:
                airport,name,duration,distance,contact,emergency_phone_number = line.strip().split(',')
                destination_instance = Destination(name,airport,duration,distance,contact,emergency_phone_number)
                destination_list.append(destination_instance)
            i += 1
        
        destination_file.close()
        return destination_list


    def changeDestinationFile(self,new_destination_list):
        '''Updates the file with new changes (overwrites the old file)'''

        file_object = open(self.__destination_filename,'w')

        with file_object:
            writer = csv.writer(file_object)
            writer.writerow(['id','destination','flight_duration','distance','emergency_name','emergency_phone'])
        
            for destination in new_destination_list:
                writer.writerow([destination.getDestinationAirport(),destination.getDestinationName(),destination.getDestinationDuration(),destination.getDestinationDistance(),destination.getDestinationContact(),destination.getDestinationEmergencyPhoneNumber()])


    def addDestinationToFile(self,destination):
        '''Adds the destination into file'''
        file_object = open(self.__destination_filename,'a')
        file_object.write(destination.getDestinationAirport()+','+destination.getDestinationName()+\
            ','+destination.getDestinationDistance()+','+ destination.getDestinationDuration()+\
                ','+destination.getDestinationContact()+','+destination.getDestinationEmergencyPhoneNumber())
        
        print('Destination successfully added!')
        return file_object

