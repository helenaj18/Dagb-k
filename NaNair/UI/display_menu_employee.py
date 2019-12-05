from UI.crewUI import CrewUI
from UI.display_menu_attendants import DisplayMenuAttendants
from UI.display_menu_pilots import DisplayMenuPilots
from UI.display_menu_working_crew import DisplayMenuWorkingCrew
import datetime

# EMPLOYEE 

class DisplayMenuEmployee: 
    def __init__(self, logic_layer):
        print('Display employees')
        self.logic_layer = logic_layer

    def startDisplayMenu(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Employees'))
        print('#'*20)
        print()

        while True: 
          
            print('What would you like to display?') 
            print()

            print('1 - All employees')
            print('2 - Single employee')
            print('3 - Pilots')
            print('4 - Flight attendants')
            print('5 - Working status by date')
            print('6 - Work Schedule for employee by ID')
            print()
            selection = input()
            

            if selection == '1':
                return CrewUI().showCrew()

            elif selection =='2':
                #Setja inn villuboð - ath má vera svona mikið í try?
                while True:
                    crew_id = input('Enter the Crew members ID (SSN): ')
                    
                    try:
                        int(crew_id)
                        if len(crew_id) == 10:
                            return CrewUI().showOneCrewMember(crew_id)
                        else:
                            print('Invalid SSN')
                    except ValueError:
                        print('Invalid SSN')
            

            elif selection == '3':
                return DisplayMenuPilots(self.logic_layer).startDisplayPilots()

            elif selection == '4':
                return DisplayMenuAttendants(self.logic_layer).startDisplayAttendants()
            
            elif selection == '5':
                return DisplayMenuWorkingCrew().startDisplayMenuWorkingCrew()
            
            elif selection == '6':
                print('Enter the "From date" for work schedule')
                start_year_int = int(input('Year: '))
                start_month_int = int(input('Month: '))
                start_day_int = int(input('Day: '))
                start_date = datetime.datetime(start_year_int,start_month_int,start_day_int,0,0,0).isoformat()
                print('Enter the "To date" for work schedule')
                end_year_int = int(input('Year: '))
                end_month_int = int(input('Month: '))
                end_day_int = int(input('Day: '))
                end_date = datetime.datetime(end_year_int,end_month_int,end_day_int,0,0,0).isoformat()


            else: 
                print('Invalid selection')