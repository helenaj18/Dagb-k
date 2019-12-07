#from API.IO_API import IO_API
import os
import csv
from ModelClasses.crew_model import Crew
from ModelClasses.pilot_model import Pilot
from IO.crewIO import CrewIO

# ATH á að vera inní klasa



class PilotIO:
    
    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__crew_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Crew.csv')
    
        SSN_const = 0
        NAME_const = 1
        ROLE_const = 2
        RANK_const = 3
        LICENSE_const = 4
        ADDRESS_const = 5
        PHONENUMBER_const = 6
        EMAIL_const = 7

    # Er hægt að kalla í read file úr attendant????

    def read_file(self):

        '''list of all pilots'''
        pilot_list = []

        crew_file= open(self.__crew_filename,'r')

        reader_crew= csv.DictReader(crew_file)

        for row in reader_crew:
            if row['role'] == CrewIO.PILOT:
                
                pilot = Pilot(row['name'],row['ssn'],row['address'],row['phonenumber'],row['email'],\
                    row['license'],row['captain/head_flight_attendant'],row['role'])
                pilot_list.append(pilot)
                
        return pilot_list


    def find_pilots(self):
        '''Finds all pilots in file and returns a list of them'''

        pilot_list = []
        self.loadPilotFromFile()
        for i in range(1,len(self.employees_list)):
            # Only pilots have licenses
            print(self.employees_list[i])
            if self.employees_list[i]["LICENSE_const"] != 'N/A': 
                pilot_list.append(self.employees_list[i])
        
        self.pilot_list = pilot_list  


    def loadPilotFromFile(self):
        '''Gets pilot info from file, returns a list of pilots'''
        return self.read_file()


    def changeCrewFile(self, crew_list):
        '''Updates the file with new changes'''
        crew_str = ''
        for item in crew_list:
            crew_str += ','.join(item) + '\n'

        file_object = open(self.__crew_filename,'w')
        file_object.write(crew_str)


    def changePilotFile(self, pilot_list):
        self.pilot_list = pilot_list

    def addPilotToFile(self, new_employee_str):
        '''Add pilot info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object

