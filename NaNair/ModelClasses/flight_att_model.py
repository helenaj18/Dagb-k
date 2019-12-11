from ModelClasses.crew_model import Crew

class FlightAttendant(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', head_flight_att=0, license = '',role = ''):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__head_flight_att = bool(int(head_flight_att))
        self.__license = 'N/A'
        self.__role = 'Cabincrew'

    # GET METHODS

    def getHeadFlightAtt(self):
        '''Gets head flight attendant'''
        return self.__head_flight_att
    
    def getRole(self):
        '''Gets role of attendant'''
        return self.__role
    
    def getBool(self):
        '''Gets the bool that returns True if the
        flight attendant is a head flight attendant'''
        return self.__head_flight_att
    
    def getLicense(self):
        '''Gets license of a flight attendant '''
        return self.__license

    # SET METHODS
    
    def setRank(self,new_rank):
        '''Sets rank of a head flight attendant'''
        self.__head_flight_att= new_rank
        return self.__head_flight_att