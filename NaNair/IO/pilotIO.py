
class PilotIO:

    SSN = 0
    NAME = 1
    ROLE = 2
    RANK = 3
    LICENSE = 4
    
    def __init__(self):
        # Muna að breyta í crew.csv!!!
        self.__crew_filename = '/Users/helenajonsdottir/Desktop/Verklegt1/Verklegt/STUDENTDATA/Crew.csv'
    

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
            if self.employees_list[i][-1] != 'N/A': # ATH virkar ekki að gera license fastann??
                pilot_list.append(self.employees_list[i])
        
        self.pilot_list = pilot_list    


    def loadPilotFromFile(self):
        '''Gets pilot info from file, returns a list of pilots'''

        self.read_file()
        self.find_pilots()

        return self.pilot_list

    def changePilotInFile(self):
        '''Change pilot info in file'''
        pass


    def addPilotToFile(self,new_employee_str):
        '''Add pilot info into file'''

        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object


a = PilotIO()
a.addPilotToFile('3108982529,Helena,Pilot,Captain,123')

b= a.loadPilotFromFile()
print(b)
print(a)