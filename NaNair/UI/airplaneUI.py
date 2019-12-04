#from NaNair import API
from API.LL_API import LL_API

class AirplaneUI:

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        return LL_API().showAllPlanes()
        

    def showAirplanesByType(self, planeTypeId = ''):
        '''Shows information about one specific airplane'''
        return LL_API().showAirplanesByType(planeTypeId)
        
    def addAirplane(self):
        
        return LL_API().AddAirplane()

