from API.IO_API import IO_API
from IO.airplaneIO import AirplaneIO
from ModelClasses.airplane_model import Airplane


class AirplaneLL:
    ''' LL class for airplane '''

    def checkIfDateValid(self,year_int,month_int,day_int):
        '''Checks if date is valid, returns a tuple with the date if valid 
           else it returns None'''

        # Checks if the year is between 0 and 2020
        if 0<year_int<=2020:

            # Checks if the month is between 0 and 12
            if 0<month_int<=12:
                months_with_31_days_list = [1,3,5,7,8,10,12]

                # If it's a month with 30 days
                if month_int in months_with_31_days_list:
                    if 0<day_int<=31:
                        return year_int,month_int,day_int
                    else:
                        return None
                
                # If it's febuary
                elif month_int == 2:
                    if self.isLeapYear(year_int):
                        if 0<day_int<=29:
                            return year_int,month_int,day_int
                        else:
                            return None
                    else:
                        if 0<day_int<=28:
                            return year_int,month_int,day_int
                        else:
                            return None
               
                # If it's a month with 30 days
                else:
                    if 0<day_int<=30:
                        return year_int,month_int,day_int
                    else:
                        return None
            
            else:
                return None
        
        else:
            return None


    def isLeapYear(self,year_int):
        '''Checks if a year is a leap year,
           returns True if it's a leap year, else returns False'''

        if year_int%4==0:
            if year_int%100==0:
                if year_int%400==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


    def verifyDate(self,year_str,month_str,day_str):
        '''Verifies a date, waits for a correct input and then returns
           a tuple with the date'''

        while True:
            try:
                # Tries to change the strings to int, prints an error message and
                # asks for a new input if it doesn't work

                year_int = int(year_str)
                month_int = int(month_str)
                day_int = int(day_str)
                
                # Checks if the date is valid
                date_tuple = self.checkIfDateValid(year_int,month_int,day_int)

                # If the date is valid, returns a tuple with the date
                if date_tuple != None:
                    return date_tuple
                # Else asks for a new input
                else:
                    print('Invalid date! Try again: ')
                    year_str = input('Year: ')
                    month_str = input('Month: ')
                    day_str = input('Day: ')

            except ValueError:
                print('Invalid date! Try again: ')
                year_str = input('Year: ')
                month_str = input('Month: ')
                day_str = input('Day: ')
    

    def verifyTime(self,hour_str,minute_str):
        '''Verifies time, waits for a correct input and then returns
           a tuple with the time'''

        while True:
            try:
                # Tries to change the strings to int, prints an error message and
                # asks for a new input if it doesn't work

                hour_int = int(hour_str)
                minute_int = int(minute_str)

                # Checks if the time is valid
                time_tuple = self.checkIfTimeValid(hour_int,minute_int)

                # If the date is valid, return a tuple with the time
                if time_tuple != None:
                    return time_tuple

                # Else asks for a new input
                else:
                    print('Invalid time! Try again: ')
                    hour_str = input('Hour: ')
                    minute_str = input('Minute: ')

            except ValueError:
                print('Invalid time! Try again: ')
                hour_str = input('Hour: ')
                minute_str = input('Minute: ')


    def checkIfTimeValid(self,hour_int,minute_int):
        '''Checks if a time is valid, returns a tuple with the time if valid 
           else it returns None'''
        
        # Checks if the hour is between 0 and 23
        if 0<=hour_int<=23:
            # Checks if the minute is between 0 and 60
            if 0<=minute_int<60:
                return hour_int,minute_int
            else:
                return None
        else:
            return None


    def getAirplanes(self):
        '''Returns a list of airplane instances'''
        return AirplaneIO().loadAirplaneFromFile()
    

    def getAirplanesByDate(self,datetime_str):
        '''Returns a list with tuples with airplanes that are flying on a date
           and information about the voyage they're in.
           Returns None if there are no voyages on the date'''

        # Gets a list of all airplanes NanAir has
        airplane_list = self.getAirplanes()
        date_str = datetime_str[:10]

        # Returns a list of voyages on a date, returns None if there are
        # no voyages on that date
        voyages_on_date = VoyageLL().getVoyageInDateRange(date_str,date_str)
        airplanes_on_date_list = []

        if voyages_on_date != None:
            # Go through all voyages on the date and match it with an airplane
            for voyage in voyages_on_date:
                for airplane in airplane_list:
                    # If the voyage hasn't been assigned to an airplane, 
                    # break and go to the next voyage
                    if voyage.getAircraftID() != 'empty':
                        if voyage.getAircraftID() == airplane.get_planeInsignia():
                            # Add the airplane and information tuple to the list of airplanes 
                            # that are in use that day
                            airplanes_on_date_list.append((airplane,voyage.getDestination().getDestinationName(),\
                                voyage.getDepartureTime(),voyage.getArrivalTimeOut(),\
                                    voyage.getArrivalTimeHome(),voyage.getFlightNumbers()))
                    else:
                        break
            else:
                # All airplanes are free if the airplanes on date list is empty
                if len(airplanes_on_date_list) != 0:
                    return airplanes_on_date_list
                else:
                    return None
        else:
            # All airplanes are free if there's no voyage at the date
            return None


    def getAirplanesByDateTime(self,datetime_str):
        '''Gets a tuple of two lists, one with available airplanes 
        and one with not available. Returns None if all airplanes are 
        available'''

        # Gets a tuple of info about airplanes that are in use on a date
        # Returns None if there are no airplanes in use on this date
        airplanes_on_date = self.getAirplanesByDate(datetime_str)

        # Gets a list of all airplanes as instances
        all_airplanes = self.getAirplanes()

        not_available_airplaneInsignias_list = []
        not_available_airplanes_info_list = []
        available_airplanes_list = []

        if airplanes_on_date != None:
            # Gets the hour out of the datetime string
            hour_int = int(datetime_str[11:13])

            for item in airplanes_on_date:
                airplane = item[0]
                destination = item[1]
                departure_time_datetime_str = item[2]
                arrival_time_out_datetime_str  = item[3]
                arrival_time_home_datetime_str  = item[4]
                flight_number_out,flight_number_home = item[5]

                departure_hour_int = int(departure_time_datetime_str [11:13])
                arrival_hour_out_int = int(arrival_time_out_datetime_str [11:13])
                arrival_hour_home_int = int(arrival_time_home_datetime_str [11:13])

                if departure_hour_int<=hour_int<=arrival_hour_home_int:
                    # If the hours is between departure hour and arrival at destination,
                    # the flight number out is added
                    if departure_hour_int<=hour_int<=arrival_hour_out_int:
                        not_available_airplanes_info_list.append((airplane,destination,\
                            arrival_time_home_datetime_str,flight_number_out))
                    
                    # Else the flight number home is added
                    else:
                        not_available_airplanes_info_list.append((airplane,destination,\
                            arrival_time_home_datetime_str,flight_number_home))
                else:
                    available_airplanes_list.append(airplane)
        

            # Remove the extra information and get only plane insignias of not available airplanes
            for i in range(len(not_available_airplanes_info_list)):
                not_available_airplaneInsignias_list.append(not_available_airplanes_info_list[i][0].get_planeInsignia())

            # If the airplane is not in the not available airplanes list
            # add it to the available airplane list if it's not there already
            for airplane_instance in all_airplanes:
                if airplane_instance.get_planeInsignia() not in not_available_airplaneInsignias_list:
                    if airplane_instance not in available_airplanes_list:
                        available_airplanes_list.append(airplane_instance)
                    
            return not_available_airplanes_info_list,available_airplanes_list
        
        else:
            # All airplanes are available, returns None
            return None


    def getAirplanesByType(self, planeTypeID = ''):
        ''' Returns list of airplanes with same Id'''

        airplanes_type_list = []
        
        # Gets all airplanes
        airplane_list = self.getAirplanes()

        for airplane in airplane_list:

            if planeTypeID == airplane.get_planeTypeID():
                airplanes_type_list.append(airplane)

        return airplanes_type_list
 

    def addAirplane(self):
        ''' Adds new airplane'''
        
        while True:

            planeInsignia = input('Enter Insignia of the new plane (TF-XXX): ').upper()

            if len(planeInsignia) == 6 and planeInsignia[2] == '-' and planeInsignia[0:2]== 'TF':
                
                while True:
                    planeTypeId = input('Enter planeTypeId (NAFokkerF100/NABAE146/NAFokkerF28): ').lower()
                    
                    if planeTypeId == 'nafokkerf100':
                        manufacturer = 'Fokker'
                        seats = '100'
                        print('Airplane successfully added!')
                        return IO_API().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)
                    elif planeTypeId == 'nabae146':
                        manufacturer = 'BAE'
                        seats = '82'
                        print('Airplane successfully added!')
                        return IO_API().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)
                    elif planeTypeId == 'nafokkerf28':
                        manufacturer = 'Fokker'
                        seats = '65'
                        print('Airplane successfully added!')
                        return IO_API().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)
                    else:
                        print('Invalid Type ID!')
            else:
                print('Invalid Plane insignia!')


# BANNAÐ AÐ FÆRA, VERÐUR AÐ VERA NEÐST
from LL.voyageLL import VoyageLL

