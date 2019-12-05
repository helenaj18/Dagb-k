import os
from ModelClasses.crew_model import Crew
from ModelClasses.pilot_model import Pilot
from ModelClasses.flight_att_model import FlightAttendant

SSN_const = 0
NAME_const = 1
ROLE_const = 2
RANK_const = 3
LICENSE_const = 4
ADDRESS_const = 5
PHONENUMBER_const = 6
EMAIL_const = 7


class CrewIO:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__crew_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Crew.csv')


    def read_file(self):
        '''Reads file and returns employees list'''
        file_object = open(self.__crew_filename,'r')
        employees_list = []

        i = 0
        for line in file_object:
            if i != 0:
                line = line.strip().split(',')
                employees_list.append(line)
            i += 1
        
        self.employees_list = employees_list
        return employees_list

    def find_pilots(self):
        '''Finds all pilots in file and returns a list of them'''

        pilot_list = []

        for i in range(len(self.employees_list)):
            # Only pilots have licenses
            if self.employees_list[i][LICENSE_const] != 'N/A': 
                pilot_list.append(self.employees_list[i])
        
        self.pilot_list = pilot_list
        return self.pilot_list  


    def find_flight_att(self):
        '''Finds all flight attendants in file and returns a list of them'''

        flight_att_list = []

        for i in range(len(self.employees_list)):
            # Only pilots have licenses
            if self.employees_list[i][LICENSE_const] == 'N/A':
                flight_att_list.append(self.employees_list[i])
        
        self.flight_att_list = flight_att_list


    def loadPilotFromFile(self):
        '''Gets pilot info from file, returns a list of pilot instances'''

        self.read_file()
        pilot_list =self.find_pilots()
        pilot_class = []

        for line in pilot_list:
            ssn,name,role,captain,pilot_license,address,phonenumber,email = line
            pilot_instance = Pilot(name,ssn,address,phonenumber,email,pilot_license,captain)
            pilot_class.append(pilot_instance)

        return pilot_class

    def loadFlightAttFromFile(self):
        '''Gets flight attendant info from file, returns a list of flight attendants'''
        flight_att_list = self.find_flight_att()

        flight_att_class = []

        for line in flight_att_list:
            ssn,name,role,head_flight_att,licence,address,phonenumber,email = line
            flight_att_instance = FlightAttendant(name,ssn,address,phonenumber,email,head_flight_att)
            flight_att_class.append(pilot_instance)

        return flight_att_class
        

    def changeCrewFile(self, crew_list):
        '''Updates the file with new changes'''
        crew_str = ''
        for item in crew_list:
            crew_str += ','.join(item) + '\n'

        file_object = open(self.__crew_filename,'w')
        file_object.write(crew_str)


    def addFlightAttToFile(self,new_employee_str):
        '''Adds flight attendant info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object

    def addPilotToFile(self, new_employee_str):
        '''Add pilot info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object