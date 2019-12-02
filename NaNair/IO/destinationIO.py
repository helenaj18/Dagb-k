class DestinationIO:

    FLIGHTNUMBER = 0
    DEPARTINGFROM = 1
    ARRAVINGAT = 2
    DEPARTURE = 3
    ARRIVAL = 4

    def __init__(self):
        # Muna að breyta í upcomingflights.csv!!!
        self.__destination_filename = '/Users/kingamaris/Documents/GitHub/Dagbok/STUDENTDATA/UpcomingFlights.csv'

    def read_file(self):
        '''Reads file and returns employees list'''
        file_object = open(self.__destination_filename,'r')
        all_destination_list = []

        for line in file_object:
            line = line.strip().split(',')
            all_destination_list.append(line)
        
        self.all_destination_list = all_destination_list

    def find_destination(self):
        '''Finds all destinations in file and returns a list of them'''

        destination_list = []
        for i in range(1,len(self.all_destination_list)):
            destination_list.append(self.all_destination_list[i][1]) #ATH FASTAN
        
        destination_list = set(destination_list)
        self.destination_list = destination_list

    def loadDestinationFromFile(self):
        '''Fetches destination from a file'''
        self.read_file()
        self.find_destination()

        return self.destination_list

    def changeDestinationFromFile(self):
        '''Change the destination or other destination info in file'''
        pass

    def addDestinationFromFile(self,new_destination_str):
        '''Adds the destination into file'''
        file_object = open(self.__destination_filename,'a')
        file_object.write(new_destination_str+'\n')

        return file_object



a = DestinationIO()


b= a.loadDestinationFromFile()
print(b)
print(a)