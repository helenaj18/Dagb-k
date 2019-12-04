import os

class DestinationIO:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.__destination_filename = os.path.join(dirname, '../UPDATEDSTUDENTDATA/Destinations.csv')

        
        self.loadDestinationFromFile()

    def loadDestinationFromFile(self):
        '''Reads file and returns destination list'''
        file_object = open(self.__destination_filename,'r')
        destination_list = []
        i = 0
        for line in file_object:
            if i != 0:
                name,airport,distance,contact,emergency_phone_number,duration = line.strip().split(',')
                destination_instance = Destination(name,airport,distance,contact,emergency_phone_number,duration)
                destination_list.append(destination_instance)
            i += 1
        return destination_list


    def changeDestinationFile(self,destination_list):
        '''Updates the file with new changes'''
        a_str = ''
        for item in destination_list:
            a_str += ','.join(item) + '\n'

        file_object = open(self.__destination_filename,'w')
        file_object.write(a_str)


    def addDestinationToFile(self,new_destination_str):
        '''Adds the destination into file'''
        file_object = open(self.__destination_filename,'a')
        file_object.write(new_destination_str+'\n')

        return file_object

class Destination:
    def __init__(self,name,airport,distance,contact,emergency_phone_number,duration):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration

    def __str__(self):
        
        return str(self.__name) +','+str(self.__airport) + ','+str(self.__distance)+','+str(self.__contact)+','+str(self.__emergency_phone_number)+','+str(self.__duration)

