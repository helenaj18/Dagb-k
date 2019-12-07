import os
import csv
from ModelClasses.crew_model import Crew
from ModelClasses.flight_att_model import FlightAttendant
from IO.crewIO import CrewIO

# ATH á að vera inní klasa
SSN_const = 0
NAME_const = 1
ROLE_const = 2
RANK_const = 3
LICENSE_const = 4
ADDRESS_const = 5
PHONENUMBER_const = 6
EMAIL_const = 7


class AttendantIO:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__crew_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Crew.csv')
     
        self.read_file()
    
    def read_file(self):
        '''Reads file and returns flight attendant list'''
        '''list of all crewmembers'''
        flight_att_list = []

        crew_file= open(self.__crew_filename,'r')

        reader_crew= csv.DictReader(crew_file)

        for row in reader_crew:
            if row['role'] == CrewIO.CABINCREW:
                crewmember = FlightAttendant(row['name'],row['ssn'],row['address'],row['phonenumber'],row['email'],\
                    row['license'],row['captain/head_flight_attendant'],row['role'])
                flight_att_list.append(crewmember)
                
        return flight_att_list


    def find_flight_att(self):
        '''Finds all flight attendants in file and returns a list of them'''

        # flight_att_list = []

        # for i in range(1,len(self.employees_list)):
        #     # Only pilots have licenses
        #     if self.employees_list[i][LICENSE_const] == 'N/A':
        #         flight_att_list.append(self.employees_list[i])
        
        # self.flight_att_list = flight_att_list
        return self.read_file()


    def loadFlightAttFromFile(self):
        '''Gets flight attendant info from file, returns a list of pilots'''
        

        return self.find_flight_att()


    def addFlightAttToFile(self,new_employee_str):
        '''Adds flight attendant info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object


    # taka út?? föll í pilotIO geta breytt

    # def changeFlightAttInFile(self):
    #     '''Changes the info of flight attendant'''
    #     pass
    

    # def changeCrewFile(self):
    #     '''Updates the file with new changes'''
    #     a_str = ''
    #     for item in self.employees_list:
    #         a_str += ','.join(item) + '\n'

    #     file_object = open(self.__crew_filename,'w')
    #     file_object.write(a_str)

