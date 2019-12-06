from API.IO_API import IO_API
from IO.airplaneIO import AirplaneIO
from ModelClasses.airplane_model import Airplane
from LL.voyageLL import VoyageLL

class AirplaneLL:
    ''' LL class for airplane '''

    def getAirplanes(self):
        '''Returns a list of airplane instances'''
        return AirplaneIO().loadAirplaneFromFile()
    
    def getAirplanesByDate(self,datetime_str):
        airplane_list = AirplaneIO().loadAirplaneFromFile()
        date_str = datetime_str[:10]
        voyages_on_date = VoyageLL().getVoyageInDateRange(date_str,date_str)
        airplanes_on_date = []

        if voyages_on_date != None:
            for voyage in voyages_on_date:
                voyage_destination = voyage.getDestination().getDestinationName()
                voyage_departure_time = voyage.getDepartureTime()
                voyage_arrival_time_out = voyage.getArrivalTimeOut()
                voyage_arrival_time_home = voyage.getArrivalTimeHome()
                voyage_flight_numbers = voyage.getFlightNumbers()
                for airplane in airplane_list:
                    if voyage.getAircraftID() == airplane.get_planeInsignia():
                        airplanes_on_date.append((airplane,voyage_destination,voyage_departure_time,voyage_arrival_time_out,voyage_arrival_time_home,voyage_flight_numbers))
            
            return airplanes_on_date
        else:
            # All airplanes are free if there's no voyage at the date
            return None
    
    def getAirplanesByDateTime(self,datetime_str):
        airplanes_on_date = self.getAirplanesByDate(datetime_str)
        if airplanes_on_date != None:
            hour_int = int(datetime_str[11:13])
            not_available_airplanes_list = []
            available_airplanes_list = []

            for item in airplanes_on_date:
                airplane = item[0]
                destination = item[1]
                departure_time = item[2]
                arrival_time_out = item[3]
                arrival_time_home = item[4]
                flight_number_out,flight_number_home = item[5]

                departure_hour_int = int(departure_time[11:13])
                arrival_hour_out_int = int(arrival_time_out[11:13])
                arrival_hour_home_int = int(arrival_time_home[11:13])

                if departure_hour_int<=hour_int<=arrival_hour_home_int:
                    if departure_hour_int<=hour_int<=arrival_hour_out_int:
                        not_available_airplanes_list.append((airplane,destination,arrival_time_home,flight_number_out))
                    else:
                        not_available_airplanes_list.append((airplane,destination,arrival_time_home,flight_number_home))
                else:
                    available_airplanes_list.append((airplane))

            return not_available_airplanes_list,available_airplanes_list
        
        else:
            return None

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





