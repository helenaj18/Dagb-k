import os
import csv
from ModelClasses.crew_model import Crew
from ModelClasses.pilot_model import Pilot
from ModelClasses.flight_att_model import FlightAttendant


class CrewIO:
    SSN_const = 0
    NAME_const = 1
    ROLE_const = 2
    RANK_const = 3
    LICENSE_const = 4
    ADDRESS_const = 5
    PHONENUMBER_const = 6
    EMAIL_const = 7

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

    def find_pilots(self):
        '''Finds all pilots in file and returns a list of them'''

        pilot_list = []
        self.read_file()

        for i in range(len(self.employees_list)):
            # Only pilots have licenses
            if self.employees_list[i][CrewIO.LICENSE_const] != 'N/A':
                pilot_list.append(self.employees_list[i])

        self.pilot_list = pilot_list
        return self.pilot_list


    def find_flight_att(self):
        '''Finds all flight attendants in file and returns a list of them'''

        flight_att_list = []
        self.read_file()

        for i in range(len(self.employees_list)):
            # Only pilots have licenses
            if self.employees_list[i][CrewIO.LICENSE_const] == 'N/A':
                flight_att_list.append(self.employees_list[i])

        self.flight_att_list = flight_att_list
        return self.flight_att_list


    def loadPilotFromFile(self):
        '''Gets pilot info from file, returns a list of pilot instances'''

        self.read_file()
        pilot_list =self.find_pilots()
        pilot_instance_list = []

        for line in pilot_list:
            ssn,name,role,captain,pilot_license,address,phonenumber,email = line
            pilot_instance = Pilot(name,ssn,address,phonenumber,email,pilot_license,captain)
            pilot_instance_list.append(pilot_instance)

        return pilot_instance_list

    def loadFlightAttFromFile(self):
        '''Gets flight attendant info from file, returns a list of flight attendants'''
        flight_att_list = self.find_flight_att()

        flight_att_instance_list = []

        for line in flight_att_list:
            ssn,name,role,head_flight_att,licence,address,phonenumber,email = line
            flight_att_instance = FlightAttendant(name,ssn,address,phonenumber,email,head_flight_att)
            flight_att_instance_list.append(flight_att_instance)

        return flight_att_instance_list


    def changeCrewFile(self, new_employee_list):
        '''Updates the file with new changes'''
        file_object = open(self.__crew_filename,'w')
        with file_object:
            writer = csv.writer(file_object)
            for employee in new_employee_list:
                writer.writerow([employee.getCrewID(),employee.getName(),employee.getRole(),employee.getBool(),employee.getLicense(),employee.getAddress(),employee.getPhoneNumber(), employee.getEmail()])


    def addCrewToFile(self,new_employee_str):
        '''Adds new employee info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object


