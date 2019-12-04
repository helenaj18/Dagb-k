from API.IO_API import IO_API
from IO.airplaneIO import AirplaneIO

class AirplaneLL:
    ''' LL class for airplane '''

    def getAirplanes(self):
        '''Fetches list of airplanes and returns a list'''
        return AirplaneIO().loadAirplaneFromFile()
        
    def getOneAirplane(self, planeInsignia = ''):
        ''' Returns information on one airplane'''
        airplane_list = AirplaneIO().loadAirplaneFromFile()
        for airplane in airplane_list:
            if planeInsignia == airplane.planeInsignia:
                print(airplane)

        return print('get one airplane UI - LL í gegn um API ')

    def addAirplane(self):
        ''' Adds new airplane'''
        return print('add airplane UI - LL í gegn um API')





