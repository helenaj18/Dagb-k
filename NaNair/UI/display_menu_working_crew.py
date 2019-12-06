from UI.crewUI import CrewUI
from LL.airplaneLL import AirplaneLL
import datetime

class DisplayMenuWorkingCrew:
    
    def startDisplayMenuWorkingCrew(self):

        while True:
            print('What would you like to see?')
            print('1 - Working crew on a specific day')
            print('2 - Nonworking crew on a specific day')
            print('3 - Back to Display Employee Menu')
            print()

            selection = input()
            print('Enter the date you want to display')
            year_str = input('Year: ')
            month_str = input('Month: ')
            day_str = input('Day: ')

            year_int,month_int,day_int = AirplaneLL().verifyDate(year_str,month_str,day_str)

            date_datetime = datetime.datetime(year_int,month_int,day_int,0,0,0).isoformat()

            if selection == '1':
                return CrewUI().showWorkingCrew(date_datetime)

            elif selection == '2':
                return CrewUI().showNotWorkingCrew(date_datetime)
            
            elif selection == '3':
                # Ath???
                #return
                pass

            else:
                print('Invalid selection')
