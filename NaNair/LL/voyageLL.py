class VoyageLL:
    ''' LL class for voyage '''
    def __init__(self, voyage,voyageIO):
        self.voyage_list = IO_API().loadVoyageFromFile()
 
    def getVoyage(self,ID):
        for voyage in self.voyage_list:
            print(voyage)
 
    def addVoyage(self):
        pass



    def changeDepartureDateTimeOfVoyage(self,new_datetime_str,flight_number):
        for i in range(len(self.voyage_list)):
            if flight_number == self.voyage_list[i][0]:
                self.voyage_list[i][3] = new_datetime_str
            elif flight_number == self.voyage_list[i][11]:
                self.voyage_list[i][14] = new_datetime_str
        
        VoyageIO().changeVoyageFile(self.voyage_list)

        return 'Change completed'


    def changeArrivalDateTimeOfVoyage(self,new_datetime_str,flight_number):
        for i in range(len(self.voyage_list)):
            if flight_number == self.voyage_list[i][0]:
                self.voyage_list[i][4] = new_datetime_str
            elif flight_number == self.voyage_list[i][11]:
                self.voyage_list[i][15] = new_datetime_str
        
        VoyageIO().changeVoyageFile(self.voyage_list)

        return 'Change completed'


class Voyage:
    def __init__(self, airplane, pilot, flight_att, flight_route, voyage_id):
        self.__airplane = airplane
        self.__pilot = pilot
        self.__flight_att = flight_att
        self.__flight_route = flight_route
        self.__voyage_id = voyage_id
 