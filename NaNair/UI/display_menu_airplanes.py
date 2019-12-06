from UI.airplaneUI import AirplaneUI
from UI.display_menu_airplane_type import DisplayMenuAirplaneType
import datetime

class DisplayMenuAirplanes: 
    def __init__(self, logic_layer):
        print('Display airplanes')

    def startDisplayAirplanes(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Airplanes'))
        print('#'*20)
        print()

        while True: 
            print('What would you like to display?')
            print()
            print('1 - List all airplanes')
            print('2 - List airplanes by type')
            print('3 - List airplanes by date and time')
            print('m - Go back to display menu')
            print()

            selection = input()

            if selection == '1':
                '''Gets all airplanes'''
                AirplaneUI().showAllPlanes()

            elif selection == '2':
                '''Gets all airplanes by type'''
                DisplayMenuAirplaneType().startDisplayAirplaneType()
            
            elif selection == '3':
                '''Gets status on airplanes by date and time'''
                print('Enter the date you want to display')
                year_str = input('Year: ')
                month_str = input('Month: ')
                day_str = input('Day: ')
                hour_str = input('Hour: ')
                minute_str = input('Minute: ')

                year_int,month_int,day_int = AirplaneUI().VerifyDate(year_str,month_str,day_str)

                hour_int,minute_int = AirplaneUI().VerifyTime(hour_str,minute_str)

                datetime_str = datetime.datetime(year_int,month_int,day_int,hour_int,minute_int).isoformat()

                AirplaneUI().showAirplanesByDateTime(datetime_str)

            elif selection == 'm':
                '''Goes back to main menu'''
                return
            else: 
                print('Invalid selection')