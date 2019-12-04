from ModelClasses.crew_model import Crew

class FlightAttendant(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', head_flight_att=False):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__head_flight_att = bool(int(head_flight_att))


    def getHeadFlightAtt(self):
        return self.__head_flight_att
    