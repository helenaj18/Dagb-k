import os
from ModelClasses.voyage_model import Voyage
from ModelClasses.destination_model import Destination
import csv

class VoyageIO:

    def __init__(self):
        # Muna að breyta í rétt nöfn!

        dirname = os.path.dirname(__file__)
        #self.__upcomingVoyages_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/UpcomingVoyages.csv')
        #self.__pastVoyages_filename = os.path.join(dirname,'../UPDATEDSTUDENTDATA/PastVoyages.csv')
        self.__allVoyages_filename = os.path.join(dirname,'../UPDATEDSTUDENTDATA/allvoyages.csv')
        self.__destinations_filename = os.path.join(dirname,'../UPDATEDSTUDENTDATA/Destinations.csv')


        #self.loadVoyageFromFile()

    def get_info(self,file_object):
        a_list = []

        for line in file_object:
            line = line.strip().split(',')
            a_list.append(line)

        a_list = a_list[1:]

        return a_list



    def loadVoyageFromFile(self):
        '''Loads existing voyages from the file'''
        voyage_list = []

        voyage_file = open(self.__allVoyages_filename)
        
        
        reader_voyage = csv.DictReader(voyage_file)
        #reader_dest = csv.DictReader(destination_file)

        for row in reader_voyage: 
            destination_file = open(self.__destinations_filename)
            reader_dest = csv.DictReader(destination_file)
            for dest_row in reader_dest:
                if dest_row['id'] == row['arrivingAt_out']:

                    destination_instance = Destination(dest_row['destination'],dest_row['id'],dest_row['distance'],\
                         dest_row['flight_duration'],dest_row['emergency_name'], dest_row['emergency_phone'])

                    voyage_instance = Voyage(row['voyageIDnumber'],row['flightNumber_out'],row['flightNumber_home'],row['departingFrom_home'],\
                        destination_instance ,row['departure_time_home'],row['arrival_time_home'], row['aircraftID'],\
                            row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])

                    voyage_list.append(voyage_instance)

        return voyage_list

     


    def changeVoyageFile(self, upcoming_list):
        '''Updates the file with new changes'''
        voyage_str = ''
        for item in upcoming_list:
            voyage_str += ','.join(item) + '\n'
        
        file_object = open(self.__upcomingVoyages_filename,'w')
        file_object.write(voyage_str)
        pass


    def addVoyageToFile(self,new_voyage_str):
        '''Adds a new voyage to the file'''

        file_object = open(self.__upcomingVoyages_filename,'a')
        file_object.write(new_voyage_str+'\n')

        #return file_object
        pass



    def getOneVoyage(self, voyage_to_get_ID):
        voyage_list = VoyageIO().loadVoyageFromFile()
        for voyage in voyage_list:
            voyage_ID = Voyage.getVoyageID
            if voyage_ID == voyage_to_get_ID: 
                return voyage