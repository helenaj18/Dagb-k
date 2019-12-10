from API.IO_API import IO_API
from IO.airplaneIO import AirplaneIO
from ModelClasses.airplane_model import Airplane
import datetime


class AirplaneLL:
    ''' LL class for airplane '''

    AIRPLANE_const = 0
    DESTINATION_const = 1
    FLIGHT_NUMBERS_const = 5
    DEPARTURE_DATETIME_const = 2
    ARRIVAL_DATETIME_OUT_const = 3
    ARRIVAL_DATETIME_HOME_const = 4


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
                    year_str = input('Year: ').strip()
                    month_str = input('Month: ').strip()
                    day_str = input('Day: ').strip()

            except ValueError:
                print('Invalid date! Try again: ')
                year_str = input('Year: ').strip()
                month_str = input('Month: ').strip()
                day_str = input('Day: ').strip()
    

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
                    hour_str = input('Hour: ').strip()
                    minute_str = input('Minute: ').strip()

            except ValueError:
                print('Invalid time! Try again: ')
                hour_str = input('Hour: ').strip()
                minute_str = input('Minute: ').strip()


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
    

    def getAirplanesByDate(self,datetime_object):
        '''Returns a list with tuples with airplanes that are flying on a date
           and information about the voyage they're in.
           Returns None if there are no voyages on the date'''

        # Gets a list of all airplanes NanAir has
        airplane_list = self.getAirplanes()

        # Returns a list of voyages on a date, returns None if there are
        # no voyages on that date
        voyages_on_date_list = VoyageLL().getVoyageInDateRange(datetime_object,datetime_object)
        airplanes_on_date_info_list = []

        if voyages_on_date_list != None:
            # Go through all voyages on the date and match it with an airplane
            for voyage in voyages_on_date_list:
                for airplane in airplane_list:
                    # If the voyage hasn't been assigned to an airplane, 
                    # break and go to the next voyage
                    if voyage.getAircraftID() != 'empty':
                        if voyage.getAircraftID() == airplane.get_planeInsignia():
                            # Add the airplane and information tuple to the list of airplanes 
                            # that are in use that day
                            airplanes_on_date_info_list.append((airplane,\
                                voyage.getDestination().getDestinationName(),\
                                    voyage.getDepartureTime(),voyage.getArrivalTimeOut(),\
                                        voyage.getArrivalTimeHome(),voyage.getFlightNumbers()))
                    else:
                        break
            else:
                # All airplanes are free if the airplanes on date info list is empty
                if len(airplanes_on_date_info_list) != 0:
                    return airplanes_on_date_info_list
                else:
                    return None
        else:
            # All airplanes are free if there's no voyage at the date
            return None

    def seperateDatetimeString(self, datetime_str):   
        '''Seperates a datetime string and 
           returns the date part and time part in a tuple'''

        return datetime_str[:10],datetime_str[-8:]

    def revertDatetimeStrtoDatetime(self,datetime_str):   
        '''Reverts a string object with a date string
           to a datetime object'''
        datetime_str_date, datetime_str_time = self.seperateDatetimeString(datetime_str)
        year,month,day = datetime_str_date.split('-')
        hour,mins,secs = datetime_str_time.split(':')
        datetime_object = datetime.datetime(int(year),int(month),int(day),int(hour),int(mins),int(secs))

        return datetime_object


    def getAirplanesByDateTime(self,datetime_object):
        '''Gets a tuple of two lists, one with available airplanes 
        and one with not available. Returns None if all airplanes are 
        available'''

        # Gets a tuple of info about airplanes that are in use on a date
        # Returns None if there are no airplanes in use on this date
        airplanes_on_date_info_list = self.getAirplanesByDate(datetime_object)

        # Gets a list of all airplanes as instances
        all_airplanes = self.getAirplanes()

        not_available_airplane_insignias_list = []
        not_available_airplanes_info_list = []
        available_airplanes_list = []

        if airplanes_on_date_info_list != None:
            # Gets the hour out of the datetime string
            hour_int = datetime_object.hour

            for item in airplanes_on_date_info_list:
                airplane_instance = item[AirplaneLL.AIRPLANE_const]
                destination_name = item[AirplaneLL.DESTINATION_const]
                flight_number_out,flight_number_home = item[AirplaneLL.FLIGHT_NUMBERS_const]

                departure_datetime_object = self.revertDatetimeStrtoDatetime(item[AirplaneLL.DEPARTURE_DATETIME_const])
                arrival_time_out_datetime_object = self.revertDatetimeStrtoDatetime(item[AirplaneLL.ARRIVAL_DATETIME_OUT_const])
                arrival_time_home_datetime_object = self.revertDatetimeStrtoDatetime(item[AirplaneLL.ARRIVAL_DATETIME_HOME_const])

                departure_hour_int = departure_datetime_object.hour
                arrival_hour_out_int = arrival_time_out_datetime_object.hour
                arrival_hour_home_int =  arrival_time_home_datetime_object.hour

                if departure_hour_int <= hour_int <= arrival_hour_home_int:
                    # If the hours is between departure hour and arrival at destination,
                    # the flight number out is added
                    if departure_hour_int <= hour_int <= arrival_hour_out_int:
                        not_available_airplanes_info_list.append((
                            airplane_instance,destination_name,
                            arrival_time_home_datetime_object.isoformat(),
                            flight_number_out
                        ))
                    
                    # Else the flight number home is added
                    else:
                        not_available_airplanes_info_list.append((
                            airplane_instance,destination_name,
                            arrival_time_home_datetime_object.isoformat(),
                            flight_number_home
                        ))
                else:
                    available_airplanes_list.append(airplane_instance)
        

            # Remove the extra information and get only plane 
            # insignias of not available airplanes
            for i in range(len(not_available_airplanes_info_list)):
                not_available_airplane_insignia_str = not_available_airplanes_info_list[i][AirplaneLL.AIRPLANE_const].get_planeInsignia()
                not_available_airplane_insignias_list.append(not_available_airplane_insignia_str)

            # If the airplane is not in the not available airplanes list
            # add it to the available airplane list if it's not there already
            for airplane_instance in all_airplanes:
                if airplane_instance.get_planeInsignia() not in not_available_airplane_insignias_list:
                    if airplane_instance not in available_airplanes_list:
                        available_airplanes_list.append(airplane_instance)
                    
            return not_available_airplanes_info_list,available_airplanes_list
        
        else:
            # All airplanes are available, returns None
            return None


    def getAirplanebyInsignia(self, planeInsignia_input):
        ''''Gets an airplane by its insignia,
            returns the airplane if it's in the file,
            else returns None'''

        airplane_list = self.getAirplanes()
        while True:
            for airplane in airplane_list:
                if airplane.get_planeInsignia() == planeInsignia_input:
                    return airplane
            else:
                # Returns None if the airplane doesn't exist
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
        '''Gets information about a new airplane
           and adds it to the file'''

        planeInsignia = self.getAirplaneInsigniaInput()
        planeTypeID,manufacturer,seats = self.getPlaneTypeIDInput()

        return IO_API().addAirplaneToFile(planeInsignia,planeTypeID,manufacturer,seats)


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
                print('\nInvalid Type ID!\n')


    def getAirplaneInsigniaInput(self):
        '''Gets plane insignia from user'''
        while True:
            planeInsignia = input('Enter Insignia of the new plane (TF-XXX): ').upper()
            if len(planeInsignia) == 6 and planeInsignia[2] == '-' and planeInsignia[0:2]== 'TF':
                return planeInsignia
            else:
                print('Invalid Plane insignia! Please write it in this format (TF-XXX)')




    def getAirplaneInsigniaList(self):
        '''Gets a list of all airplane
           insignias '''
           
        airplane_insignia_list = []
        airplanes = IO_API().loadAirplaneFromFile()
        for airplane in airplanes:
            airplane_insignia_list.append(airplane.get_planeInsignia())

        return airplane_insignia_list



# BANNAÐ AÐ FÆRA, VERÐUR AÐ VERA NEÐST
from LL.voyageLL import VoyageLL

