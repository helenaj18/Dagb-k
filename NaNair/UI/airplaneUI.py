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
        print()

        
    def showAirplanesByType(self,planeTypeID):
        '''Shows Airplanes by type'''

        airplanes = LL_API().showAirplanesByType(planeTypeID)

        header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity','length','height','wingspan')
        print(header_str)
        print('-'*len(header_str))

        for airplane in airplanes:
            planeInsignia = airplane.get_planeInsignia()
            planeTypeID = airplane.get_planeTypeID()
            manufacturer = airplane.get_planeManufacturer()
            model = airplane.get_planeModel()
            capacity = airplane.get_planeCapacity()
            length = airplane.get_planeCapacity()
            height = airplane.get_planeHeight()
            wingspan = airplane.get_planeWingspan()
            
            format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(planeInsignia,planeTypeID,manufacturer,model,capacity,length,height,wingspan)       
            print(format_str)
            
        print()

        
    def addAirplane(self):
        
        return LL_API().AddAirplane()

