#from NaNair import API
from API.LL_API import LL_API

class AirplaneUI:

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity','length','height','wingspan')
        print(header_str)
        print('-'*len(header_str))

        airplanes = AirplaneUI().showAllPlanes()

        for elem in airplanes:
            print(elem)

        return LL_API().showAllPlanes()
        

    def showAirplanesByType(self, planeTypeId = ''):
        '''Shows information about one specific airplane'''
        return LL_API().showAirplanesByType(planeTypeId)
        
    def addAirplane(self):
        
        return LL_API().AddAirplane()

