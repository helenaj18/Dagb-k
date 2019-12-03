from API.LL_API import LL_API

class AirplaneUI:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        LL_API().show_all_planes()
        

    def showOnePlane(self, plane_ID = ''):
        '''Shows information about one specific airplane'''
        LL_API().show_one_plane()
        
    def addAirplane(self):
        
        LL_API().add_airplane()