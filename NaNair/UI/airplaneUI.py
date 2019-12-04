#from NaNair import API
from API.LL_API import LL_API

class AirplaneUI:

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        return print(LL_API().show_all_planes())
        
    # ATH KRAFA???
    def showOnePlane(self, plane_ID = ''):
        '''Shows information about one specific airplane'''
        return LL_API().show_one_plane()
        
    def addAirplane(self):
        
        return LL_API().add_airplane()


    def showPlanesByType(self):
        pass