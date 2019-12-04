#from NaNair import API
from API.LL_API import LL_API

class AirplaneUI:

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        return LL_API().show_all_planes()
        

    def showAirplanesByType(self, planeTypeId = ''):
        '''Shows information about one specific airplane'''
        return LL_API().ShowAirplanesByType()
        
    def addAirplane(self):
        
        return LL_API().AddAirplane()

