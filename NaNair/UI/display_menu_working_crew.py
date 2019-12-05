from UI.crewUI import CrewUI
import datetime

class DisplayMenuWorkingCrew:
    
    def startDisplayMenuWorkingCrew(self):

        while True:
            print('What would you like to see?')
            print('1 - Working crew on a specific day')
            print('2 - Nonworking crew on a specific day')
            print()

            selection = input()
            print('Enter the date you want to display')
            year_int = int(input('Year: '))
            month_int = int(input('Month: '))
            day_int = int(input('Day: '))
            date_datetime = datetime.datetime(year_int,month_int,day_int,0,0,0).isoformat()
  
            if selection == '1':
                return CrewUI().showWorkingCrew(date_datetime)

            elif selection == '2':
                return CrewUI().showNotWorkingCrew(date_datetime)
            
            else:
                print('Invalid selection')
