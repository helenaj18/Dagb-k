from API.LL_API import LL_API
from ModelClasses.airplane_model import Airplane


class AirplaneUI:

    def showAllPlanes(self):
        '''Shows information about all airplanes NanAir owns'''
        
        header_str = '\n{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia',\
            'planeTypeId','Manufacturer','Model','Capacity')
        print(header_str)
        print('-'*len(header_str))

        # Gets a list of airplane instances
        airplanes_list = LL_API().showAllPlanes()

        # Goes through all airplane instances in the list and prints each one
        for airplane in airplanes_list:
            format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}'.format(airplane.get_planeInsignia(),\
                airplane.get_planeTypeID(),airplane.get_planeManufacturer(),\
                    airplane.get_planeModel(),airplane.get_planeCapacity())
            print(format_str)
        print()
    
    def showAllAirplaneTypes(self):
        '''Shows all airplane types and the number of 
        pilots that have a license for that type'''

        airplane_type_dict = LL_API().showAirplaneTypes()
        
        print()
        print('{:<20}{:<10}'.format('Airplane Type','Number of Licensed Pilots'))
        print('-'*45)

        for key,value in airplane_type_dict.items():
            print('{:<20}{:>15}'.format(key,value))
        
        print('-'*45)

    def showAirplanesByType(self,planeTypeID):
        '''Shows Airplanes by type'''

        # Gets a list of airplane instances of the same type
        airplanes_list = LL_API().showAirplanesByType(planeTypeID)

        header_str = '\n{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia',\
            'planeTypeId','Manufacturer','Model','Capacity')
        print(header_str)
        print('-'*len(header_str))

        # Goes through the list and prints all airplanes
        for airplane in airplanes_list:
            
            format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}'.format(airplane.get_planeInsignia(),\
                airplane.get_planeTypeID(),airplane.get_planeManufacturer(),\
                    airplane.get_planeModel(),airplane.get_planeCapacity())       
            print(format_str)
            
        print()
    

    def showAirplanesByDateTime(self,date_str):
        '''Shows airplanes availability by a date and time'''

        # Gets a tuple of available airplanes list and not available airplane list
        # Returns None if all airplanes are available
        airplane_tuple = LL_API().showAirplanesByDateTime(date_str)
        header_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format('PlaneInsignia',\
            'planeTypeId','Seats','Flight Number','Availability',\
                'Available again','Destination')
        print()
        print(header_str)
        print('-'*len(header_str))

        if airplane_tuple != None:
            not_available_airplanes_list,available_airplanes_list = airplane_tuple
            # Prints all available airplanes
            for airplane in available_airplanes_list:
                format_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format(airplane.get_planeInsignia(),\
                    airplane.get_planeTypeID(),airplane.get_planeCapacity(),\
                        'N/A','Available','N/A','N/A')       
                print(format_str)
            
            # Prints all not available airplanes
            for airplane,destination,arrival_time,flight_number in not_available_airplanes_list:
                format_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format(airplane.get_planeInsignia(),\
                    airplane.get_planeTypeID(),airplane.get_planeCapacity(),\
                        flight_number,'Not available',arrival_time,destination)       
                print(format_str)

            print()

        else:
            # All airplanes are available if there's no voyage on the date
            airplanes_list = LL_API().showAllPlanes()
            for airplane in airplanes_list:
                format_str = '{:<15}{:<15}{:<15}{:<15}{:<20}{:<25}{:<15}'.format(airplane.get_planeInsignia(),\
                    airplane.get_planeTypeID(),airplane.get_planeCapacity(),\
                        'N/A','Available','N/A','N/A')       
                print(format_str)
            print()


    def addAirplane(self):
        '''Gets information about a new airplane
           and adds it to the file'''

        planeInsignia = self.getAirplaneInsigniaInput()
        planeTypeID,manufacturer,seats = self.getPlaneTypeIDInput()

        LL_API().addAirplane(planeInsignia,planeTypeID,manufacturer,seats)
        print()
        print('~'*45)
        print('{:^45}'.format('Airplane successfully added!')) 
        print('~'*45)


    def getPlaneTypeIDInput(self):
        '''Gets plane type id input from user'''

        print('\nChoose planeTypeId:\n')

        while True:
                    
            print('1 - NAFokkerF100')
            print('2 - NABAE146')
            print('3 - NAFokkerF28')
            print()
            selection = input('Please choose one of the above (1/2/3): ').strip()
            
            if selection == '1':
                planeTypeId = 'NAFokkerF100'
                manufacturer = 'Fokker'
                seats = '100'
                return planeTypeId,manufacturer,seats

            elif selection == '2':
                planeTypeId = 'NABAE146'
                manufacturer = 'BAE'
                seats = '82'
                return planeTypeId,manufacturer,seats

            elif selection == '3':
                planeTypeId = 'NAFokkerF28'
                manufacturer = 'Fokker'
                seats = '65'
                return planeTypeId,manufacturer,seats

            else:
                print('\nInvalid selection!\n')


    def getAirplaneInput(self,departure_datetime, arrival_datetime):
        '''Shows a list of available airplanes and gets 
        airplane input from the user'''

        print('Available airplanes at time of departure:')
        print()

        airplanes_list = LL_API().showPlanesForNewVoyage(departure_datetime, arrival_datetime)
        print('{:<10}{:<15}'.format('Insignia', 'Type'))
        print('-'*25)

        for plane in airplanes_list:
            print('{:<10} {:<15}'.format(plane.get_planeInsignia(),\
                    plane.get_planeTypeID()))        

        print()
        plane_name = input('Enter Insignia of the plane (TF-XXX): ').upper().strip()
        check = LL_API().checkPlaneInput(plane_name, airplanes_list)

        while check == False:
            print('-'*45)
            print('{:^45}'.format('This plane is not available on this date,\
            please choose one of the listed planes.'))
            print('-'*45)
            
            plane_name = input().upper().strip()
            check = LL_API().checkPlaneInput(plane_name, airplanes_list)
        
        return plane_name

    def getAirplaneInsigniaInput(self):
        '''Gets plane insignia from user'''
        while True:
            planeInsignia = input('\nEnter Insignia of the new plane (TF-XXX): ').upper().strip()
            if len(planeInsignia) == 6 and planeInsignia[2] == '-' and planeInsignia[0:2]== 'TF':
                return planeInsignia
            else:
                print('Invalid Plane insignia! Please write it in this format (TF-XXX)')


    def getAirplaneInsigniaList(self):
        '''Gets a list of all airplane 
           insignias of airplanes that NanAir has'''
        return LL_API().getAirplaneInsigniaList()
