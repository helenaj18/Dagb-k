#from API.IO_API import IO_API

# ATH á að vera inní klasa
SSN_const = 0
NAME_const = 1
ROLE_const = 2
RANK_const = 3
LICENSE_const = 4
ADDRESS_const = 5
PHONENUMBER_const = 6
EMAIL_const = 7

class PilotIO:
    
    def __init__(self):
        # Muna að breyta í crew.csv!!!
        self.__crew_filename = '/Users/kingamaris/Documents/GitHub/Dagbok/UPDATEDSTUDENTDATA/Crew.csv'
    

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
        
        info_to_edit = IO_API().getPilotInputToEdit()

        # Tékka á völu og marinellu hvernig þetta yrði gert
        if info_to_edit[0] == 'e':
            self.ChangeEmailAddress(info_to_edit[0],info_to_edit[1])
        elif info_to_edit[0] == 'h':
            self.ChangeHomeAddress(info_to_edit[0],info_to_edit[1])
        elif info_to_edit[0] == 'p':
            self.ChangePhoneNumber(info_to_edit[0],info_to_edit[1])
        elif info_to_edit[0] == 'l':
            self.ChangeLicense(info_to_edit[0],info_to_edit[1])


    def ChangeEmailAddress(self,personal_id,new_email_address):
        '''Changes the Emergency Contact for destination in file'''
        self.__personal_id = personal_id
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][EMAIL_const] = new_email_address  
        self.changeCrewFile()


    def ChangeHomeAddress(self,personal_id,new_home_address):
        '''Changes the Emergency Contact for destination in file'''
        self.__personal_id = personal_id
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][ADDRESS_const] = new_home_address  
        self.changeCrewFile()

    def ChangePhoneNumber(self,personal_id,new_phone_number):
        '''Changes the Emergency Contact for destination in file'''
        self.__personal_id = personal_id
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][PHONENUMBER_const] = new_phone_number
        self.changeCrewFile()
    
    def ChangeLicense(self,personal_id,new_license):
        '''Changes the License of the pilot in file'''
        self.__personal_id = personal_id
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][LICENSE_const] = new_license
        self.changeCrewFile()


    def changeCrewFile(self):
        '''Updates the file with new changes'''
        a_str = ''
        for item in self.employees_list:
            a_str += ','.join(item) + '\n'

        file_object = open(self.__crew_filename,'w')
        file_object.write(a_str)

    def addPilotToFile(self, new_employee_str):
        '''Add pilot info into file'''


        file_object = open(self.__crew_filename,'a')
        file_object.write(new_employee_str+'\n')

        return file_object

