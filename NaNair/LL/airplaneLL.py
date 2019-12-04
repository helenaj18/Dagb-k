from API.IO_API import IO_API
from IO.airplaneIO import AirplaneIO

class AirplaneLL:
    ''' LL class for airplane '''

    def getAirplanes(self):
        '''Fetches list of airplanes and returns a list'''
        return AirplaneIO().loadAirplaneFromFile()
        
    def getOneAirplane(self, plane_ID = ''):
        ''' Returns information on one airplane'''
        
        return print('get one airplane UI - LL í gegn um API ')

    def addAirplane(self):
        ''' Adds new airplane'''
        return print('add airplane UI - LL í gegn um API')





