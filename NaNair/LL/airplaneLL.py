from API.IO_API import IO_API
from IO.airplaneIO import AirplaneIO
from ModelClasses.airplane_model import Airplane

class AirplaneLL:
    ''' LL class for airplane '''

    def getAirplanes(self):
        '''Fetches list of airplanes and returns a list'''
        return AirplaneIO().loadAirplaneFromFile()
        
    def getAirplanesByType(self, planeTypeID = ''):
        ''' Returns list of airplanes with same Id'''
        airplanes_type_list = []
        airplane_list = AirplaneIO().loadAirplaneFromFile()

        for airplane in airplane_list:

            if planeTypeID == airplane.get_planeTypeID():
                airplanes_type_list.append(airplane)

        return airplanes_type_list
 
    def addAirplane(self,planeInsignia,planeTypeId,manufacturer,seats):
        ''' Adds new airplane'''
        return IO_API().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)





