from ModelClasses.crew_model import Crew

class FlightAttendant(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', head_flight_att=False, license = '',role = ''):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__head_flight_att = bool(head_flight_att)
        self.__license = 'N/A'
        self.__role = 'Cabincrew'

    def __str__(self):
        pass
        # flight_att_string = '{},{},{}'.format(self.__role,self.__head_flight_att,\
        #     self.__license)
        
        # return Crew(__str__(self) + flight_att_string+ super(__str__().b_string()

        # #return super().__str__().a_string() + flight_att_string+ super().__str__().b_string()
        # return 'ÞETTA ER FLIGHT ATTENDANT'

    def getHeadFlightAtt(self):
        return self.__head_flight_att

    def changeHeadFlightAtt(self):
        '''If flight attendant is a head service manager (and head_flight_att = True) this method will make him a
        flight attendant (captain = False) and reverse'''

        if self.__head_flight_att == True:
            self.__head_flight_att = False
        else:
            self.__head_flight_att = True
    
    def getRole(self):
        return self.__role
    
    def getBool(self):
        return self.__head_flight_att
    
    def getLicense(self):
        return 'N/A'

    def setRank(self,new_rank):
        self.__head_flight_att = new_rank
        return self.__head_flight_att
        #á eftir gera þetta fall