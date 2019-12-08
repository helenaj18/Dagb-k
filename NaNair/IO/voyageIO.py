import os
from ModelClasses.voyage_model import Voyage
from ModelClasses.destination_model import Destination
import csv
from datetime import timedelta

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

                    destination_instance = Destination(dest_row['destination'],dest_row['id'],\
                         dest_row['flight_duration'],dest_row['distance'],dest_row['emergency_name'], dest_row['emergency_phone'])

                    voyage_instance = Voyage(row['voyageIDnumber'],row['flightNumber_out'],row['flightNumber_home'],row['departingFrom_home'],\
                        destination_instance ,row['departure_time_home'],row['arrival_time_out'],row['arrival_time_home'], row['aircraftID'],\
                            row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])

                    voyage_list.append(voyage_instance)

        return voyage_list

     


    def changeVoyageFile(self, updated_voyage):
        '''Updates the file with new changes'''
        allvoyages = self.loadVoyageFromFile()

        file_object = open(self.__allVoyages_filename,'w')
        with file_object:
            # header 
            fieldnames = ['voyageIDnumber','flightNumber_out','departingFrom_home',\
                'arrivingAt_out','departure_time_home','arrival_time_out','flightNumber_home',\
                    'departingFrom_out','arrivingAt_home','departure_time_out','arrival_time_home',\
                        'aircraftID','captain','opilot','fsm','fa1','fa2']


            writer = csv.DictWriter(file_object,fieldnames=fieldnames)
            writer.writeheader()

            for voyage in allvoyages:
                voyage_id = voyage.getVoyageID()
                updated_voyage_id = updated_voyage.getVoyageID()
                if voyage_id == updated_voyage_id:
                    
                    writer.writerow({
                        'voyageIDnumber':updated_voyage.getVoyageID(),
                        'flightNumber_out':updated_voyage_id.getFlightNumbers()[0],
                        'departingFrom_home':updated_voyage.getDepartureLocation(),
                        'arrivingAt_out':updated_voyage.getDestination().getDestinationAirport(),
                        'departure_time_home':updated_voyage.getDepartureTime(),
                        'arrival_time_out':updated_voyage.getArrivalTimeOut(),
                        'flightNumber_home':updated_voyage.getFlightNumbers()[1],
                        'departingFrom_out':updated_voyage.getDestination().getDestinationAirport(),
                        'arrivingAt_home':updated_voyage.getDepartureLocation(),
                        'departure_time_out':updated_voyage.getArrivalTimeOut()+ timedelta(hours = 1),
                        'arrival_time_home':updated_voyage.getArrivaltimeHome(),
                        'aircraftID':updated_voyage.getAircraftID(),
                        'captain':updated_voyage.getCaptain(),
                        'copilot':updated_voyage.getCopilot(),
                        'fsm':updated_voyage.getHeadFlightAtt(),
                        'fa1':updated_voyage.getFlightAttOne(),
                        'fa2':updated_voyage.getFlightAttTwo()
                    })

                else:

                    writer.writerow({
                        'voyageIDnumber':voyage.getVoyageID(),
                        'flightNumber_out':voyage.getFlightNumbers()[0],
                        'departingFrom_home':voyage.getDepartureLocation(),
                        'arrivingAt_out':voyage.getDestination().getDestinationAirport(),
                        'departure_time_home':voyage.getDepartureTime(),
                        'arrival_time_out':voyage.getArrivalTimeOut(),
                        'flightNumber_home':voyage.getFlightNumbers()[1],
                        'departingFrom_out':voyage.getDestination().getDestinationAirport(),
                        'arrivingAt_home':voyage.getDepartureLocation(),
                        'departure_time_out':voyage.getArrivalTimeOut()+ timedelta(hours = 1),
                        'arrival_time_home':voyage.getArrivaltimeHome(),
                        'aircraftID':voyage.getAircraftID(),
                        'captain':voyage.getCaptain(),
                        'copilot':voyage.getCopilot(),
                        'fsm':voyage.getHeadFlightAtt(),
                        'fa1':voyage.getFlightAttOne(),
                        'fa2':voyage.getFlightAttTwo()

                    })


        


    def addVoyageToFile(self, new_voyage_str):
        '''Adds a new voyage to the file'''

        file_object = open(self.__allVoyages_filename,'a')
        file_object.write(new_voyage_str+'\n')

        #return file_object
        pass
