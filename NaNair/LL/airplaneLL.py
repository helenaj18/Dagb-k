from API.IO_API import IO_API
from IO.airplaneIO import AirplaneIO
from ModelClasses.airplane_model import Airplane
from LL.voyageLL import VoyageLL

class AirplaneLL:
    ''' LL class for airplane '''

    def getAirplanes(self):
        '''Returns a list of airplane instances'''
        return AirplaneIO().loadAirplaneFromFile()
    
    def getAirplanesByDate(self,date_str):
        airplane_list = AirplaneIO().loadAirplaneFromFile()
        voyages_on_date = VoyageLL().getVoyageInDateRange(date_str,date_str)
        airplanes_on_date = []

        for voyage in voyages_on_date:
            duration = voyage.getDestination().getDestinationDuration()
            destination = voyage.getDestinationName()
            for airplane in airplane_list:
                if voyage.getAircraftID() == airplane.get_planeInsignia():
                    airplanes_on_date.append((airplane,duration,destination))
        
        return airplanes_on_date
    
    def getAirplanesByDateTime(self,date_str):
        airplanes_on_date = self.getAirplanesByDate(date_str)

        pass


    def getAirplanesByType(self, planeTypeID = ''):
        ''' Returns list of airplanes with same Id'''
        airplanes_type_list = []
        airplane_list = AirplaneIO().loadAirplaneFromFile()

        for airplane in airplane_list:

            if planeTypeID == airplane.get_planeTypeID():
                airplanes_type_list.append(airplane)

        return airplanes_type_list
 
    def addAirplane(self,planeInsignia,planeTypeId,manufacturer,seats):
        ''' Adds new airplane'''
        return IO_API().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)





