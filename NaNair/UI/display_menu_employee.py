from UI.crewUI import CrewUI
from UI.display_menu_attendants import DisplayMenuAttendants
from UI.display_menu_pilots import DisplayMenuPilots
from UI.display_menu_working_crew import DisplayMenuWorkingCrew
from UI.display_menu_workschedule import DisplayMenuWorkSchedule
import datetime


class DisplayMenuEmployee: 
    def __init__(self, logic_layer):
        print('Display employees')
        self.logic_layer = logic_layer

    def startDisplayMenu(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Employees'))
        print('#'*20)

        while True: 
            print()
            print('What would you like to display?') 
            print()

            print('1 - All employees')
            print('2 - Single employee')
            print('3 - Pilots')
            print('4 - Flight attendants')
            print('5 - Working status by date')
            print('6 - Work Schedule for employee by ID')
            print('m - Back to main menu')
            print()
            selection = input()
            

            if selection == '1':
                return CrewUI().showCrew()

            elif selection =='2':
                # Checks if the crew ID input is valid,
                # checks if its 10 letters and an integer

                while True:
                    crew_id = input('Enter the Crew members ID (SSN): ')
                    
                    try:
                        int(crew_id)
                        if len(crew_id) == 10:
                            # Prints information about one Crew member
                            return CrewUI().showOneCrewMember(crew_id)
                        else:
                            print('Invalid SSN')
                    except ValueError:
                        print('Invalid SSN')
            

            elif selection == '3':
                # Goes to the next menu where the user can pick how he wants
                # to display the pilots
                return DisplayMenuPilots(self.logic_layer).startDisplayPilots()


            elif selection == '4':
                # Shows all flight attendants
                return CrewUI().showAllFlightAtt()
            

            elif selection == '5':
                return DisplayMenuWorkingCrew().startDisplayMenuWorkingCrew()
            
            
            elif selection == '6':
                # Checks if the crew ID input is valid,
                # checks if its 10 letters and an integer,
                # and if the crew ID belongs to a crew member

                while True:
                    crew_id = input('Enter the Crew members ID (SSN): ')
                    
                    try:
                        int(crew_id)
                        if len(crew_id) == 10:

                            # Prints a work schedule for a crew member
                            get_schedule = CrewUI().showSchedule(crew_id)
                            if get_schedule == False:
                                print('No employee with this ID')
                            else:
                                return
                        else:
                            print('Invalid SSN')
        
                    except ValueError:
                        print('Invalid SSN')
                
                
            elif selection == 'm':
                # Goes back to main menu
                return

            else: 
                print('Invalid selection')