from API.LL_API import LL_API
from ModelClasses.airplane_model import Airplane


class AirplaneUI:

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        
        header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity')
        print(header_str)
        print('-'*len(header_str))

        # Gets a list of airplane instances
        airplanes = LL_API().showAllPlanes()

        # Goes through all airplane instances in the list and prints each one
        for airplane in airplanes:
            format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}'.format(airplane.get_planeInsignia(),airplane.get_planeTypeID(),airplane.get_planeManufacturer(),airplane.get_planeModel(),airplane.get_planeCapacity())
            print(format_str)
        print()
    
    def showAirplanesByType(self,planeTypeID):
        '''Shows Airplanes by type'''

        # Gets a list of airplane instances
        airplanes = LL_API().showAirplanesByType(planeTypeID)

        header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity')
        print(header_str)
        print('-'*len(header_str))

        # Goes through the list and prints all airplanes
        for airplane in airplanes:
            
            format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}'.format(airplane.get_planeInsignia(),airplane.get_planeTypeID(),airplane.get_planeManufacturer(),airplane.get_planeModel(),airplane.get_planeCapacity())       
            print(format_str)
            
        print()
    
    def showAirplanesByDateTime(self,date_str):
        '''Shows airplanes availability by a date and time'''

        # Gets a tuple of available airplanes list and not available airplane list
        # Returns None if all airplanes are available
        airplane_tuple = LL_API().showAirplanesByDateTime(date_str)
        header_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format('PlaneInsignia','planeTypeId','Seats','Flight Number','Availability','Available again','Destination')
        print()
        print(header_str)
        print('-'*len(header_str))

        if airplane_tuple != None:
            not_available_airplanes_list,available_airplanes_list = airplane_tuple
            # Prints all available airplanes
            for airplane in available_airplanes_list:
                format_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format(airplane.get_planeInsignia(),airplane.get_planeTypeID(),airplane.get_planeCapacity(),'N/A','Available','N/A','N/A')       
                print(format_str)
            
            # Prints all not available airplanes
            for airplane,destination,arrival_time,flight_number in not_available_airplanes_list:
                format_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format(airplane.get_planeInsignia(),airplane.get_planeTypeID(),airplane.get_planeCapacity(),flight_number,'Not available',arrival_time,destination)       
                print(format_str)

            print()

        else:
            # All airplanes available if there's no voyage on the date
            airplanes = LL_API().showAllPlanes()
            for airplane in airplanes:
                format_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format(airplane.get_planeInsignia(),airplane.get_planeTypeID(),airplane.get_planeCapacity(),'N/A','Available','N/A','N/A')       
                print(format_str)
            print()

    def addAirplane(self):
        '''Adds a new Airplane to the airplane file'''
        return LL_API().addAirplane()

