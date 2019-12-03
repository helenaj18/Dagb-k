 
class AirplaneLL:
    ''' LL class for airplane '''
    def __init__(self, airplane = '', airplaneIO = ''):
        self.airplane = airplane
        self.airplaneIO = airplaneIO
 
    def getAirplanes(self):
        '''Fetches list of airplanes and returns a list'''
        return print('get airplanes UI - LL í gegn um API')
        
    def getOneAirplane(self, plane_ID = ''):
        ''' Returns information on one airplane'''
        return print('get one airplane UI - LL í gegn um API ')

    def addAirplane(self):
        pass



class Airplane:
    def __init__(self, name, seats, airplane_type):
        self.name = name
        self.seats = seats
        self.airplane_type = airplane_type