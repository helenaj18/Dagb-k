import os
from ModelClasses.airplane_model import Airplane
from ModelClasses.aircraft_type_model import AircraftTypeModel
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
        for aircraft_line in aircraft_file:
            aircraft_type_file = open(self.__aircraft_type_filename, 'r')

            # Skip the header in aircraft file
            if i != 0:
                # Get information from aircraft file
                planeInsignia,planeTypeId_in_aircraft_file,manufacturer,seats = aircraft_line.strip().split(',')
                
                # Go through aircraft type file and match the Plane Type ID with 
                # the Plane Type ID from the aircraft file
                for aircraft_type_line in aircraft_type_file:
                    planeTypeId_in_aircraft_type_file,manufacturer,model,capacity,\
                        emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,\
                            wingspan = aircraft_type_line.strip().split(',')
                    
                    # Make an airplane instance and add it to a list of airplane instances
                    if planeTypeId_in_aircraft_file == planeTypeId_in_aircraft_type_file:
                        
                        airplane_instance = Airplane(planeInsignia, planeTypeId_in_aircraft_file,\
                            manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,\
                                serviceCeiling,length,height,wingspan)
                        
                        airplanes_list.append(airplane_instance)
            i += 1
            aircraft_type_file.close()
        
        aircraft_file.close()
        
        return airplanes_list


    def loadAircraftTypes(self):
        '''Reads file and returns a list of airplane instances'''
        i = 0 
        aircraft_type_filename = open(self.__aircraft_type_filename,'r')
        airplane_types_list = []
        
        for line in aircraft_type_filename:
            if i != 0:
                planeTypeId_in_aircraft_file,\
                    manufacturer,model,\
                        capacity,emptyWeight,\
                            maxTakeoffWeight,unitThrust,\
                                serviceCeiling,length,height,wingspan = line.strip().split(',')

                aircraft_type_instance = AircraftTypeModel(planeTypeId_in_aircraft_file,\
                    manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,\
                                    serviceCeiling,length,height,wingspan)

                airplane_types_list.append(aircraft_type_instance)
                
            i += 1
            
        aircraft_type_filename.close()

        return airplane_types_list

    def addAirplaneToFile(self, planeInsignia,planeTypeId,manufacturer,seats):
        '''Adds an airplane to the airplane file'''
        aircraft_file = open(self.__aircraft_filename,'a')
        aircraft_file.write(planeInsignia+','+planeTypeId+','+manufacturer+','+seats+'\n')
        
        return aircraft_file
    
    def addAirplaneType(self,planeTypeId,manufacturer,model,capacity,\
            emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan):
        aircraft_type_file = open(self.__aircraft_type_filename,'a')

        aircraft_type_file.write(planeTypeId+','+manufacturer+','+model+','+capacity+','\
            +emptyWeight+','+maxTakeoffWeight+','+unitThrust+','+serviceCeiling+','\
                +length+','+height+','+wingspan+'\n')
        
        return aircraft_type_file