import csv

class AirplaneIO:

    def __init__(self):
        #self.__airplane_filename = 'Aircraft.csv'
        self.__airplane_filename = './NaNair/IO/UPDATEDSTUDENTDATA/Aircraft.csv'
        self.loadAirplaneFromFile()

    def loadAirplaneFromFile(self):
        '''Reads file and returns aircraft list'''
        file_object = open(self.__airplane_filename,'r')
        airplanes_list = []

        for line in file_object:
            line = line.strip().split(',')
            airplanes_list.append(line)
        
        self.airplanes_list = airplanes_list

        return self.airplanes_list

    def addAirplaneToFile(self, new_airplane_str):
        '''Adds a new airplane to the file'''
        
        file_object = open(self.__airplane_filename,'a')
        file_object.write(new_airplane_str+'\n')

        return file_object
