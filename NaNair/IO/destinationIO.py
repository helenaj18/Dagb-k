class DestinationIO:

    def __init__(self):
        # Muna að breyta í upcomingflights.csv!!!
        self.__destination_filename = '/Users/kingamaris/Documents/GitHub/Dagbok/UPDATEDSTUDENTDATA/Destinations.csv'

    def read_file(self):
        '''Reads file and returns employees list'''
        file_object = open(self.__destination_filename,'r')
        destination_list = []

        for line in file_object:
            line = line.strip().split(',')
            destination_list.append(line)
        
        self.destination_list = destination_list

    # def find_destination(self):
    #     '''Finds all destinations in file and returns a list of them'''
    #     destination_list = []
    #     for i in range(1,len(self.all_destination_list)):
    #         destination_list.append(self.all_destination_list[i]) #ATH FASTAN
        
    #     self.destination_list = destination_list

    def loadDestinationFromFile(self):
        '''Fetches destination from a file'''
        self.read_file()

        return self.destination_list

    def ChangeEmergencyContact(self,destination_name,new_emergency_contact):
        '''Changes the Emergency Contact for destination in file'''
        self.__destination_name = destination_name
        for i in range(len(self.destination_list)):
            if destination_name == self.destination_list[i][1]:
                self.destination_list[i][-2] = new_emergency_contact
        
        self.changeDestinationFile()
    

    def changeDestinationFile(self):
        a_str = ''
        for item in self.destination_list:
            a_str += ','.join(item) + '\n'

        file_object = open(self.__destination_filename,'w')
        file_object.write(a_str)

    def ChangeEmergencyPhone(self,destination_name,new_emergency_phone):
        '''Changes the Emergency Contact for destination in file'''
        self.__destination_name = destination_name
        for i in range(len(self.destination_list)):
            if destination_name == self.destination_list[i][1]:
                self.destination_list[i][-1] = new_emergency_phone
        
        self.changeDestinationFile()


    def addDestinationFromFile(self,new_destination_str):
        '''Adds the destination into file'''
        file_object = open(self.__destination_filename,'a')
        file_object.write(new_destination_str+'\n')

        return file_object



a = DestinationIO()
b= a.loadDestinationFromFile()
a.ChangeEmergencyContact('Kulusuk','Kinga')
a.ChangeEmergencyPhone('Kulusuk','5812345')

print(b)
#print(a)