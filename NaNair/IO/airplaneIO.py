import os
from ModelClasses.airplane_model import Airplane
import csv

class AirplaneIO:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__aircraft_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Aircraft.csv')
        self.__aircraft_type_filename = os.path.join(dirname,'../UPDATEDSTUDENTDATA/AircraftType.csv')


    def loadAirplaneFromFile(self):
        '''Reads file and returns a list of airplane instances'''
        aircraft_file = open(self.__aircraft_filename,'r')
        airplanes_list = []
        i = 0

        # Go through aircraft file with the airplanes NanAir owns
        for line_aircraft in aircraft_file:
            aircraft_type_file = open(self.__aircraft_type_filename, 'r')
            if i != 0:
                # Get information from aircraft file
                planeInsignia,planeTypeId_in_aircraft_file,manufacturer,seats = line_aircraft.strip().split(',')
                
                # Go through aircraft type file and match the Plane Type ID with 
                # the Plane Type ID from the aircraft file
                for line_aircraft_type in aircraft_type_file:
                    planeTypeId_in_aircraft_type_file,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan = line_aircraft_type.strip().split(',')
                    
                    # Make an airplane instance and add it to a list of airplane instances
                    if planeTypeId_in_aircraft_file == planeTypeId_in_aircraft_type_file:
                        airplane_instance = Airplane(planeInsignia, planeTypeId_in_aircraft_file,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan)
                        airplanes_list.append(airplane_instance)
            i += 1
            aircraft_type_file.close()

        return airplanes_list



    def addAirplaneToFile(self, planeInsignia,planeTypeId,manufacturer,seats):
        '''Adds an airplane to the airplane file'''
        aircraft_file = open(self.__aircraft_filename,'a')
        aircraft_file.write(planeInsignia+','+planeTypeId+','+manufacturer+','+seats)
        
        return aircraft_file


