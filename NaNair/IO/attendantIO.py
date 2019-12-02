class AttendantIO:

    def __init__(self):
        # Muna að breyta í crew.csv!!!
        self.__flight_att_filename = '/Users/helenajonsdottir/Desktop/Verklegt1/Verklegt/STUDENTDATA/Crew.csv'

    
    def read_file(self):
        '''Reads file and returns employees list'''
        file_object = open(self.__flight_att_filename,'r')
        employees_list = []

        for line in file_object:
            line = line.strip().split(',')
            employees_list.append(line)
        
        self.employees_list = employees_list


    def find_flight_att(self):
        '''Finds all flight attendants in file and returns a list of them'''

        flight_att_list = []

        for i in range(1,len(self.employees_list)):
            # Only pilots have licenses
            if self.employees_list[i][-1] == 'N/A':
                flight_att_list.append(self.employees_list[i])
        
        self.flight_att_list = flight_att_list


    def loadFlightAttFromFile(self):
        '''Gets info of flight attendant from file'''
        self.read_file()
        self.find_flight_att()

        return self.flight_att_list


    def addFlightAttToFile(self,new_employee_str):
        '''Adds flight attendant info into file'''

        file_object = open(self.__flight_att_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object


    def changeFlightAttInFile(self):
        '''Changes the info of flight attendant'''
        pass


a = AttendantIO()
a.addFlightAttToFile('3108982529,Helena,Pilot,Captain,123')

b= a.loadFlightAttFromFile()
print(b)
print(a)