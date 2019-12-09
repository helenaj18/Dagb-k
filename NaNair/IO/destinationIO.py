import os
from ModelClasses.destination_model import Destination
import csv 

class DestinationIO:

    def __init__(self):
        # Gets the filename of destination file
        dirname = os.path.dirname(__file__)
        self.__destination_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Destinations.csv')


    def loadDestinationFromFile(self):
        '''Reads file and returns a list
           of destination instances'''
        destination_file = open(self.__destination_filename,'r')
        destination_list = []
        i = 0
        for line in destination_file:
            # Skip the header in the file
            if i != 0:
                airport,name,duration,distance,contact,emergency_phone_number = line.strip().split(',')
                destination_instance = Destination(name,airport,duration,distance,contact,emergency_phone_number)
                destination_list.append(destination_instance)
            i += 1
        
        destination_file.close()
        return destination_list


    def changeDestinationFile(self,new_destination_instance):
        '''Updates the file with new changes (overwrites the old file)'''

        all_destinations = self.loadDestinationFromFile()

        file_object = open(self.__destination_filename,'w')

        with file_object:
            fieldnames = ['id','destination','flight_duration','distance',\
            'emergency_name','emergency_phone']
            writer = csv.DictWriter(file_object, fieldnames=fieldnames)
            writer.writeheader()
        
            for destination in all_destinations:
                dest_code = destination.getDestinationAirport()
                updated_destination = new_destination_instance.getDestinationAirport()

                if dest_code == updated_destination:
                    writer.writerow({
                        'id':new_destination_instance.getDestinationAirport(),
                        'destination':new_destination_instance.getDestinationName(),
                        'flight_duration':new_destination_instance.getDestinationDuration(),
                        'distance':new_destination_instance.getDestinationDistance(),
                        'emergency_name':new_destination_instance.getDestinationContact(),
                        'emergency_phone':new_destination_instance.getDestinationEmergencyPhoneNumber()
                    })
            
                else:

                    writer.writerow({
                        'id':destination.getDestinationAirport(),
                        'destination':destination.getDestinationName(),
                        'flight_duration':destination.getDestinationDuration(),
                        'distance':destination.getDestinationDistance(),
                        'emergency_name':destination.getDestinationContact(),
                        'emergency_phone':destination.getDestinationEmergencyPhoneNumber()
                    })



    def addDestinationToFile(self,destination):
        '''Adds the destination into file'''

        file_object = open(self.__destination_filename,'a')
        file_object.write(destination.getDestinationAirport()+\
            ','+destination.getDestinationName()+\
                ','+destination.getDestinationDistance()+\
                    ','+ destination.getDestinationDuration()+\
                        ','+destination.getDestinationContact()+\
                        ','+destination.getDestinationEmergencyPhoneNumber()+'\n')
        
        return file_object

