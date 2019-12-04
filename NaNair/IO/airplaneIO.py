import os
from ModelClasses.airplane_model import Airplane
import csv

class AirplaneIO:

    def __init__(self):
        
        dirname = os.path.dirname(__file__)
        self.__aircraft_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Aircraft.csv')
        self.__aircraft_type_filename = os.path.join(dirname,'../UPDATEDSTUDENTDATA/AircraftType.csv')

    def loadAirplaneFromFile(self):
        '''Reads file and returns aircraft list'''
        aircraft_file = open(self.__aircraft_filename,'r')
        aircraft_type_file = open(self.__aircraft_type_filename, 'r')
        airplanes_list = []
        i = 0


        for line_aircraft in aircraft_file:
            aircraft_type_file = open(self.__aircraft_type_filename, 'r')
            if i != 0:
                planeInsignia,planeTypeId_1 = line_aircraft.strip().split(',')
                for line_aircraft_type in aircraft_type_file:
                    planeTypeId_2,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan = line_aircraft_type.strip().split(',')
                    if planeTypeId_1 == planeTypeId_2:
                        airplane_instance = Airplane(planeInsignia, planeTypeId_1,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan)
                        airplanes_list.append(airplane_instance)
            i += 1
            aircraft_type_file.close()

        return airplanes_list


    def addAirplaneToFile(self, planeInsignia,planeTypeId):
        aircraft_file = open(self.__aircraft_filename,'a')
        aircraft_file.write(planeInsignia+','+planeTypeId)
        return aircraft_file


