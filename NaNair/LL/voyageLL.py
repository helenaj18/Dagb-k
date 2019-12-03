class VoyageLL:
    ''' LL class for voyage '''
    def __init__(self, voyage,voyageIO):
        self.voyage = voyage
        self.voyageIO = voyageIO
        pass
 
    def getVoyage(self, ID):
        pass
 
    def addVoyage(self):
        pass
 
    def changeVoyage(self, ID):
        pass



class Voyage:
    def __init__(self, airplane, pilot, flight_att, flight_route, voyage_id):
        self.__airplane = airplane
        self.__pilot = pilot
        self.__flight_att = flight_att
        self.__flight_route = flight_route
        self.__voyage_id = voyage_id
 