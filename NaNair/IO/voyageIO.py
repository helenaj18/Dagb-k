
class VoyageIO:

    def __init__(self):
        # Muna að breyta í rétt nöfn!
        self.__upcomingFlights_filename = '/Users/helenajonsdottir/Desktop/Verklegt1/Verklegt/UPDATEDSTUDENTDATA/UpcomingFlights.csv'
        self.__pastFlights_filename = '/Users/helenajonsdottir/Desktop/Verklegt1/Verklegt/UPDATEDSTUDENTDATA/PastFlights.csv'

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
        for i in range(len(self.flights_list)):
            voyage_list.append(self.flights_list[i:i+1])
            i += 2

        self.voyage_list = voyage_list

    def changeVoyageInFile(self):
        '''Changes an existing voyage in the file'''
        pass


    def addVoyageToFile(self,new_voyage_str):
        '''Adds a new voyage to the file'''

        file_object = open(self.__upcomingFlights_filename,'a')
        file_object.write(new_voyage_str+'\n')

        return file_object


a = VoyageIO()
a.loadVoyageFromFile()

a.addVoyageToFile('NA553,Keflavik,Longyearbyen,12122019,13122019')
