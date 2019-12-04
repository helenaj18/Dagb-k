import os
from ModelClasses.voyage_model import Voyage

class VoyageIO:

    def __init__(self):
        # Muna að breyta í rétt nöfn!

        dirname = os.path.dirname(__file__)
        self.__upcomingVoyages_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/UpcomingVoyages.csv')
        self.__pastVoyages_filename = os.path.join(dirname,'../UPDATEDSTUDENTDATA/PastVoyages.csv')


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

        upcomingVoyages_file_object = open(self.__upcomingVoyages_filename,'r')
        pastVoyages_file_object = open(self.__pastVoyagesfilename,'r')
        
        upcoming_list = self.get_info(upcomingVoyages_file_object)
        past_list = self.get_info(pastVoyages_file_object)

        self.flights_list = upcoming_list + past_list

        return upcoming_list

    def loadVoyageFromFile(self):
        '''Loads existing voyages from the file'''
        file_object = open(self.__upcomingVoyages_filename)


        # self.read_file()
        # voyage_list = []
        
        # for i in range(len(self.flights_list)-2):
        #     voyage_list.append(self.flights_list[i]+self.flights_list[i+1])
        #     i += 2

        # self.voyage_list = voyage_list


        # return self.voyage_list


    def changeVoyageFile(self, upcoming_list):
        '''Updates the file with new changes'''
        voyage_str = ''
        for item in upcoming_list:
            voyage_str += ','.join(item) + '\n'
        
        file_object = open(self.__upcomingFlights_filename,'w')
        file_object.write(voyage_str)


    def addVoyageToFile(self,new_voyage_str):
        '''Adds a new voyage to the file'''

        file_object = open(self.__upcomingFlights_filename,'a')
        file_object.write(new_voyage_str+'\n')

        return file_object



a = VoyageIO()
a.loadVoyageFromFile()