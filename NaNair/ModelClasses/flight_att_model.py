from ModelClasses.crew_model import Crew

class FlightAttendant(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', head_flight_att=0, license = '',role = ''):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__head_flight_att = bool(int(head_flight_att))
        self.__license = 'N/A'
        self.__role = 'Cabincrew'

    # def __str__(self):
    #     return 'FLIGHT ATTENDANT'

    def setRank(self,new_rank):
        self.__head_flight_att= new_rank
        return self.__head_flight_att

    def getHeadFlightAtt(self):
        return self.__head_flight_att
    
    def getRole(self):
        return self.__role
    
    def getBool(self):
        return self.__head_flight_att
    
    def getLicense(self):
        return self.__license

    # def getCrewID(self):
    #     return Crew.__crewID

