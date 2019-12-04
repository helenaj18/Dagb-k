#from API.IO_API import IO_API
import os

# ATH á að vera inní klasa



class PilotIO:
    
    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__crew_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Crew.csv')
    

    # Er hægt að kalla í read file úr attendant????

    def read_file(self):
        '''Reads file and returns employees list'''
        file_object = open(self.__crew_filename,'r')
        employees_list = []

        for line in file_object:
            line = line.strip().split(',')
            employees_list.append(line)
        
        self.employees_list = employees_list
        return employees_list


    def find_pilots(self):
        '''Finds all pilots in file and returns a list of them'''

        pilot_list = []

        for i in range(1,len(self.employees_list)):
            # Only pilots have licenses
            if self.employees_list[i][LICENSE_const] != 'N/A': 
                pilot_list.append(self.employees_list[i])
        
        self.pilot_list = pilot_list   


    def loadPilotFromFile(self):
        '''Gets pilot info from file, returns a list of pilots'''

        self.read_file()
        self.find_pilots()

        return self.pilot_list


    def changeCrewFile(self, crew_list):
        '''Updates the file with new changes'''
        crew_str = ''
        for item in crew_list:
            crew_str += ','.join(item) + '\n'

        file_object = open(self.__crew_filename,'w')
        file_object.write(crew_str)

    def addPilotToFile(self, new_employee_str):
        '''Add pilot info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object

