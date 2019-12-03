from API.IO_API import IO_API
from IO.voyageIO import VoyageIO

class VoyageLL:
    ''' LL class for voyage '''
    def __init__(self):
        self.voyage_list = IO_API().loadVoyageFromFile()
        self.upcoming_list = IO_API().read_file()
 
    def getVoyage(self,ID):
        for voyage in self.voyage_list:
            print(voyage) # þarf að formatta streng
 
    def addVoyage(self):
        pass



    def changeDateTimeOfVoyage(self,new_datetime_str,flight_number):
        print('In changeDateTimeofVoyage in VoyageLL.py')
        for i in range(len(self.upcoming_list)):
            if flight_number == self.upcoming_list[i][0]:
                self.upcoming_list[i][3] = new_datetime_str
        
        VoyageIO().changeVoyageFile(self.upcoming_list)

        return 'Change completed'



class Voyage:
    def __init__(self, airplane, pilot, flight_att, flight_route, voyage_id):
        self.__airplane = airplane
        self.__pilot = pilot
        self.__flight_att = flight_att
        self.__flight_route = flight_route
        self.__voyage_id = voyage_id
 