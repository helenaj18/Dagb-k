
class VoyageIO:

    def __init__(self):
        # Muna að breyta í rétt nöfn!
        self.__upcomingFlights_filename = '/Users/helenajonsdottir/Desktop/Verklegt1/Verklegt/UpcomingFlights.csv'
        self.__pastFlights_filename = '/Users/helenajonsdottir/Desktop/Verklegt1/Verklegt/PastFlights.csv'
        self.loadVoyageFromFile()

    def get_info(self,file_object):
        a_list = []

        for line in file_object:
            line = line.strip().split(',')
            a_list.append(line)

        a_list = a_list[1:]

        return a_list


    def read_file(self):
        '''Reads two files and adds them to a list,returns the list'''

        upcomingFlights_file_object = open(self.__upcomingFlights_filename,'r')
        pastFlights_file_object = open(self.__pastFlights_filename,'r')
        
        upcoming_list = self.get_info(upcomingFlights_file_object)
        past_list = self.get_info(pastFlights_file_object)

        self.flights_list = upcoming_list + past_list



    def loadVoyageFromFile(self):
        '''Loads existing voyages from the file'''
        self.read_file()
        voyage_list = []
        
        for i in range(len(self.flights_list)-2):
            voyage_list.append(self.flights_list[i]+self.flights_list[i+2])
            i += 2

        self.voyage_list = voyage_list

# miðað við að það sé slegið inn flugnúmer á leið út
    def changeDepartureDateTimeOfVoyage(self, new_datetime_str,flight_number):
        '''Changes the departure date and time of an existing voyage in the file'''
        for i in range(len(self.flights_list)):
            if flight_number == self.flights_list[i][0]:
                self.flights_list[i][3] = new_datetime_str

        self.changeVoyageFile()

    
    def changeArrivalDateTimeOfVoyage(self, new_datetime_str,flight_number):
        '''Changes the departure date and time of an existing voyage in the file'''
        for i in range(len(self.flights_list)):
            if flight_number == self.flights_list[i][0]:
                self.flights_list[i][4] = new_datetime_str
        
        self.changeVoyageFile()


    def changeVoyageFile(self):
        '''Updates the file with new changes'''
        voyage_str = ''
        for item in self.flights_list:
            voyage_str += ','.join(item) + '\n'
        
        file_object = open(self.__upcomingFlights_filename,'w')
        file_object.write(voyage_str)


    def addVoyageToFile(self,new_voyage_str):
        '''Adds a new voyage to the file'''

        file_object = open(self.__upcomingFlights_filename,'a')
        file_object.write(new_voyage_str+'\n')

        return file_object


a = VoyageIO()
a.changeArrivalDateTimeOfVoyage('prufa','NA1111')


