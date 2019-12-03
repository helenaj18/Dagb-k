from API.IO_API import IO_API #ath?

class AirplaneLL:
    ''' LL class for airplane '''
    def __init__(self):
        self.airplane = IO_API().loadAirplaneFromFile()
 
    def getAirplanes(self):
        '''Fetches list of airplanes and returns a list'''
        
        return print('get airplanes UI - LL í gegn um API')
        
    def getOneAirplane(self, plane_ID = ''):
        ''' Returns information on one airplane'''
        return print('get one airplane UI - LL í gegn um API ')

    def addAirplane(self):
        ''' Adds new airplane'''
        return print('add airplane UI - LL í gegn um API')



class Airplane:
    def __init__(self, name, seats, airplane_type):
        self.name = name
        self.seats = seats
        self.airplane_type = airplane_type