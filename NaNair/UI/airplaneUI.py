from API.LL_API import LL_API
from ModelClasses.airplane_model import Airplane
from ModelClasses.aircraft_type_model import AircraftTypeModel

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

        # Goes through the list and prints all airplanes of the type
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


    def addAirplaneType(self):
        '''Gets information about a new airplane
        type and adds it to the file'''
        print()
        print('-'*45)
        print('{:^45}'.format('Please fill in the following information.'))
        print('-'*45)
        print()
        planeTypeId = input('Enter plane type id: ').strip()
        manufacturer = input('Enter manufacturer: ').strip()
        model = input('Enter model: ').strip()
        capacity = self.getNumberOfSeats()
        emptyWeight = self.getEmptyWeight()
        maxTakeoffWeight = self.getMaxTakeOffWeight()
        unitThrust = self.getUnitThrust()
        serviceCeiling = self.getServiceCeiling()
        length = self.getLength()
        height = self.getHeight()
        wingspan = self.getWingspan()

        LL_API().addAirplaneType(planeTypeId,manufacturer,model,capacity,\
            emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan)

        print()
        print('~'*45)
        print('{:^45}'.format('Airplane type successfully added!')) 
        print('~'*45)


    def getWingspan(self):
        '''Gets wingspan input from user'''

        # Checks if the input is a float
        while True:
            wingspan = input('Enter the wingspan (m): ').strip()
            try:
                float(wingspan)
                return wingspan
            except ValueError:
                print('\nYou have to enter a float!\n')


    def getHeight(self):
        '''Gets length input from user'''

        # Checks if the input is a float
        while True:
            height = input('Enter the height (m): ').strip()
            try:
                float(height)
                return height
            except ValueError:
                print('\nYou have to enter a float!\n')


    def getLength(self):
        '''Gets length input from user'''

        # Checks if the input is a float
        while True:
            length = input('Enter the length (m): ').strip()
            try:
                float(length)
                return length
            except ValueError:
                print('\nYou have to enter a float!\n')


    def getServiceCeiling(self):
        '''Gets service ceiling input from user'''

        # Checks if the input is an int
        while True:
            serviceCeiling = input('Enter service ceiling (m): ').strip()
            try:
                int(serviceCeiling)
                return serviceCeiling
            except ValueError:
                print('\nYou have to enter a integer!\n')


    def getUnitThrust(self):
        '''Gets unit thrust input from user'''
        
        # Checks if the input is an int
        while True:
            unitThrust = input('Enter unit thrust (N): ').strip()
            try:
                float(unitThrust)
                return unitThrust
            except ValueError:
                print('\nYou have to enter a float!\n')
    

    def getMaxTakeOffWeight(self):
        '''Gets max take off weight input from user'''

        # Checks if the input is an int
        while True:
            maxTakeoffWeight = input('Enter max take off weight (kg): ').strip()
            try:
                int(maxTakeoffWeight)
                return maxTakeoffWeight
            except ValueError:
                print('\nYou have to enter an integer!\n')
    

    def getNumberOfSeats(self):
        '''Gets number of seats input from user'''

        # Checks if the input is an int
        while True:
            seats = input('Enter number of seats: ').strip()
            try:
                int(seats)
                return seats
            except ValueError:
                print('\nYou have to enter an integer!\n')
    

    def getEmptyWeight(self):
        '''Gets empty weight input from user'''

        # Checks if the input is an int
        while True:
            emptyWeight = input('Enter empty weight (kg): ').strip()
            try:
                int(emptyWeight)
                return emptyWeight
            except ValueError:
                print('\nYou have to enter an integer!\n')
    

    def getAirplaneTypes(self):
        '''Gets a list or airplane type instances'''

        return LL_API().loadAirplaneTypes()


    def getPlaneTypeIDInput(self):
        '''Gets plane type id input from user'''

        success = False
        airplane_types = self.getAirplaneTypes()

        while True:
            print('\nChoose planeTypeId:\n')
            counter = 1

            # Goes through all the airplane types 
            # and prints options for the user
            for airplane_type in airplane_types:
                print('{} - {}'.format(counter,airplane_type))
                counter += 1

            selection = input('\nPlease choose one of the above: ').strip()

            # Goes through all the options and returns 
            # information about one airplane type
            for i in range(1,counter+1):
                if selection == str(i):
                    planeTypeId = airplane_types[i-1].getplaneTypeID()
                    manufacturer = airplane_types[i-1].getManufacturer()
                    seats = airplane_types[i-1].getCapacity()
                    success = True
                    return planeTypeId,manufacturer,seats
            
            # If the user picks something else
            if not success:
                print('\nInvalid selection!\n')


    def getAirplaneInput(self,departure_datetime, arrival_datetime):
        '''Shows a list of available airplanes and gets 
        airplane input from the user'''

        print('Available airplanes at time of departure:')
        print()

        # Gets a list of available planes
        airplanes_list = LL_API().showPlanesForNewVoyage(departure_datetime, arrival_datetime)
        print('{:<10}{:<15}'.format('Insignia', 'Type'))
        print('-'*25)

        for plane in airplanes_list:
            print('{:<10} {:<15}'.format(plane.get_planeInsignia(),\
                    plane.get_planeTypeID()))        

        
        plane_name = input('\nEnter Insignia of the plane (TF-XXX): ').upper().strip()

        # Checks if an airplane already exists
        check = LL_API().checkPlaneInput(plane_name, airplanes_list)

        while check == False:
            print('\n'+'-'*45)
            print('{:^45}'.format('This plane is not available on this date'))
            print('{:^45}'.format('please choose one of the listed planes.'))
            print('-'*45+'\n')

            plane_name = input('Please try again: ').upper().strip()
            check = LL_API().checkPlaneInput(plane_name, airplanes_list)
        
        return plane_name

    def getAirplaneInsigniaInput(self):
        '''Gets plane insignia from user'''

        while True:
            planeInsignia = input('\nEnter Insignia of the new plane (TF-XXX): ').upper().strip()
            if len(planeInsignia) == 6 and planeInsignia[2] == '-' and planeInsignia[0:2]== 'TF':
                return planeInsignia
            else:
                print('\nInvalid Plane insignia!') 
                print('Please write it in this format (TF-XXX)\n')


    def getAirplaneInsigniaList(self):
        '''Gets a list of all airplane 
           insignias of airplanes that NanAir has'''

        return LL_API().getAirplaneInsigniaList()
