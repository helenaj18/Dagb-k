from API.IO_API import IO_API

# ATH á að vera inní klasa
SSN_const = 0
NAME_const = 1
ROLE_const = 2
RANK_const = 3
LICENSE_const = 4

class PilotIO:
    
    def __init__(self):
        # Muna að breyta í crew.csv!!!
        self.__crew_filename = '/Users/erlaarnalds/Documents/GitHub/Dagbok/UPDATEDSTUDENTDATA/Crew.csv'
    

    # Er hægt að kalla í read file úr attendant????

    def read_file(self):
        '''Reads file and returns employees list'''
        file_object = open(self.__crew_filename,'r')
        employees_list = []

        for line in file_object:
            line = line.strip().split(',')
            employees_list.append(line)
        
        self.employees_list = employees_list


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

    def changePilotInFile(self):
        '''Change pilot info in file'''
        
        info_to_edit = IO_API().gefPilotInputToEdit()

        


    def addPilotToFile(self):
        '''Add pilot info into file'''

        new_employee_str = IO_API().getPilotInputToAdd()

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object

