import os
import csv
from ModelClasses.crew_model import Crew
from ModelClasses.pilot_model import Pilot
from ModelClasses.flight_att_model import FlightAttendant


class CrewIO:
    # SSN_const = 0
    # NAME_const = 1
    # ROLE_const = 2
    # RANK_const = 3
    # LICENSE_const = 4
    # ADDRESS_const = 5
    # PHONENUMBER_const = 6
    # EMAIL_const = 7
    PILOT = 'Pilot'
    CABINCREW = 'Cabincrew'

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__crew_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Crew.csv')

    def loadCrewFromFile(self):
        '''list of all crewmembers'''
        crew_list = []

        crew_file= open(self.__crew_filename,'r')

        reader_crew= csv.DictReader(crew_file)

        for row in reader_crew:
            if row['role'] == CrewIO.PILOT:
                
                pilot = Pilot(row['name'],row['ssn'],row['address'],row['phonenumber'],row['email'],\
                    row['license'],row['captain/head_flight_attendant'],row['role'])
                crew_list.append(pilot)
                
            elif row['role'] == CrewIO.CABINCREW:
                crewmember = FlightAttendant(row['name'],row['ssn'],row['address'],row['phonenumber'],row['email'],\
                    row['license'],row['captain/head_flight_attendant'],row['role'])
                crew_list.append(crewmember)
                
        return crew_list


    def changeCrewFile(self, updated_employee):
        '''Updates the file with new changes'''
        allEmps = self.loadCrewFromFile()

        file_object = open(self.__crew_filename,'w')
        with file_object:
            #header
            fieldnames = ['ssn','name','role','captain/head_flight_attendant','license', 'address','phonenumber','email']
            writer = csv.DictWriter(file_object, fieldnames=fieldnames)
            writer.writeheader()
            
            for emp in allEmps:
                if emp.getCrewID() == updated_employee.getCrewID():
                    #writer.writerow(updated_employee)
                    writer.writerow({'ssn':updated_employee.getCrewID(),'name':updated_employee.getName(),'role':updated_employee.getRole(),\
                        'captain/head_flight_attendant':updated_employee.getBool(),'license':updated_employee.getLicense(),\
                            'address':updated_employee.getAddress(),'phonenumber':updated_employee.getPhoneNumber(),'email':updated_employee.getEmail()})
                    # writer.writerow([updated_employee.getCrewID(),updated_employee.getName(),updated_employee.getRole(),\
                    #     updated_employee.getBool(),updated_employee.getLicense(),updated_employee.getAddress(),\
                    #         updated_employee.getPhoneNumber(), updated_employee.getEmail()])
                else:
                    writer.writerow({'ssn':emp.getCrewID(),'name':emp.getName(),'role':emp.getRole(),\
                        'captain/head_flight_attendant':updated_employee.getBool(),'license':updated_employee.getLicense(),\
                            'address':emp.getAddress(),'phonenumber':emp.getPhoneNumber(),'email':emp.getEmail()})

                    # writer.writerow([emp.getCrewID(),emp.getName(),emp.getRole(),\
                    #     emp.getBool(),emp.getLicense(),emp.getAddress(),emp.getPhoneNumber(), emp.getEmail()])
                
            #self.addCrewToFile(emp)
        
        
            
        #gamalt
        #for employee in new_employee_list:
            #writer.writerow([employee.getCrewID(),employee.getName(),employee.getRole(),employee.getBool(),employee.getLicense(),employee.getAddress(),employee.getPhoneNumber(), employee.getEmail()])


    def addCrewToFile(self,new_employee_str):
        '''Adds new employee info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object


