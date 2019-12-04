#from NaNair import API
from API.LL_API import LL_API

class AirplaneUI:

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity','length','height','wingspan')
        print(header_str)
        print('-'*len(header_str))

        airplanes = LL_API().showAllPlanes()

        for elem in airplanes:
            print(elem)

        
    def showAirplanesByType(self):
        '''Shows information about one specific airplane'''
        print('What type would you like to list? Please type one of the following')
        print('NAFokkerF100')
        print('NAFokkerF28')
        print('NABAE146')
        print()
        planeTypeID = input()

        airplanes = LL_API().showAirplanesByType(planeTypeID)

        header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity','length','height','wingspan')
        print(header_str)
        print('-'*len(header_str))

        for elem in airplanes:
            print(elem)

        
    def addAirplane(self):
        
        return LL_API().AddAirplane()

