class AirplaneIO:
    def read_file(self):
        '''Reads file and returns aircraft list'''
        file_object = open(self.__airplane_filename,'r')
        airplanes_list = []

        for line in file_object:
            line = line.strip().split(',')
            airplanes_list.append(line)
        
        self.airplanes_list = airplanes_list

    def __init__(self, airplaneID):
        self.__airplane_filename = '/Users/erlaarnalds/Documents/GitHub/Dagbok/STUDENTDATA/Aircraft.csv'
        self.__airplaneID = '' #búa til aðferð til að gefa flugvélum id

    def load_airplane_from_file(self):
        '''Loads existing airplanes from the file'''

        self.read_file()
        return self.airplanes_list

    def change_airplane_in_file(self):
        '''Changes an existing airplane in the file'''
        pass

    def add_airplane_to_file(self, new_airplane_str):
        '''Adds a new airplane to the file'''
        
        file_object = open(self.__airplane_filename,'a')
        file_object.write(new_airplane_str+'\n')

        return file_object

