from ModelClasses.crew_model import Crew

class FlightAttendant(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', head_flight_att=False):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__head_flight_att = bool(int(head_flight_att))

    def __str__(self):
        string = '{:<25}{:<20}'.format(self._Crew__name,self._Crew__crewID)

        if self.__head_flight_att:
            string += '{:<10}'.format('Head service manager')
        else:
            string += '{:<10}'.format('Flight attendant')

        return string


    def getHeadFlightAtt(self):
        return self.__head_flight_att

    def changeHeadFlightAtt(self):
        '''If flight attendant is a head service manager (and head_flight_att = True) this method will make him a
        flight attendant (captain = False) and reverse'''

        if self.__head_flight_att == True:
            self.__head_flight_att = False
        else:
            self.__head_flight_att = True
    