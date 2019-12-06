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

    def checkIfDateValid(self,year_int,month_int,day_int):
        '''Checks if date is valid'''
        # Ath á kannski að vera eh year today? spyrja völu hún gerði þetta eh staðar
        if 0<year_int<=2020:
            if 0<month_int<=12:
                months_with_30_days = [1,3,5,7,8,10,12]
                if month_int in months_with_30_days:
                    if 0<day_int<=31:
                        return year_int,month_int,day_int
                    else:
                        return None
                elif month_int == 2:
                    if 0<day_int<=28:
                        return year_int,month_int,day_int
                    else:
                        return None
                else:
                    if 0<day_int<=30:
                        return year_int,month_int,day_int
                    else:
                        return None
            else:
                return None
        else:
            return None

    def VerifyDate(self,year_str,month_str,day_str,hour_str,minute_str):
        while True:
            try:
                year_int = int(year_str)
                month_int = int(month_str)
                day_int = int(day_str)
                
                date_tuple = self.checkIfDateValid(year_int,month_int,day_int)
                if date_tuple != None:
                    return date_tuple
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
    
    def VerifyTime(self,hour_str,minute_str):
        while True:
            try:
                hour_int = int(hour_str)
                minute_int = int(minute_str)

                hour_minute_tuple = self.checkIfTimeValid(hour_int,minute_int)
                if hour_minute_tuple != None:
                    
                    return hour_minute_tuple
                else:
                    print('Invalid time! Try again: ')
                    hour_int = input('Hour: ')
                    minute_int = input('Minute: ')

            except ValueError:
                print('Invalid time! Try again: ')
                hour_str = input('Hour: ')
                minute_str = input('Minute: ')

    def checkIfTimeValid(self,hour_int,minute_int):
        if 0<=hour_int<23:
            if 0<=minute_int<60:
                return hour_int,minute_int
            else:
                return None
        else:
            return None
    
    def showAirplanesByType(self,planeTypeID):
        '''Shows Airplanes by type'''

        airplanes = LL_API().showAirplanesByType(planeTypeID)

        header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity','length','height','wingspan')
        print(header_str)
        print('-'*len(header_str))

        for airplane in airplanes:
            
            format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(airplane.get_planeInsignia(),airplane.get_planeTypeID(),airplane.get_planeManufacturer(),airplane.get_planeModel(),airplane.get_planeCapacity(),airplane.get_planeLength(),airplane.get_planeHeight(),airplane.get_planeWingspan())       
            print(format_str)
            
        print()
    
    def showAirplanesByDateTime(self,date_str):
        return LL_API().showAirplanesByDateTime()

        
    def addAirplane(self):
        
        return LL_API().AddAirplane()

