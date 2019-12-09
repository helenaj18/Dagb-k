from UI.crewUI import CrewUI
from UI.display_menu_pilots import DisplayMenuPilots
from UI.display_menu_working_crew import DisplayMenuWorkingCrew
import datetime


class DisplayMenuEmployee: 
    def startDisplayMenu(self):
        # banner:
        print('-'*20)
        print('{:^20}'.format('DISPLAY - Employees'))
        print('-'*20)

        while True: 
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
            selection = input().strip()
            
            # All employees are displayed
            if selection == '1':
                return CrewUI().showCrew()

            # A single employee is displayed with more percise info
            elif selection =='2':
                while True:
                    crew_id = input('Enter the Crew members ID (SSN): ')
                    
                    # checks if the personal ID is 10 letters and an integer
                    try:
                        int(crew_id)
                        if len(crew_id) == 10:
                            # Prints information about one crew member
                            return CrewUI().showOneCrewMember(crew_id)
                        else:
                            print('Invalid SSN')
                    except ValueError:
                        print('Invalid SSN')
            
            # Goes to pilot display menu
            elif selection == '3':
                return DisplayMenuPilots().startDisplayPilots()

            # Shows all flight attendants
            elif selection == '4':
                return CrewUI().showAllFlightAtt()
            
            # allows user to choose date and see working status of crew on that date
            elif selection == '5':
                return DisplayMenuWorkingCrew().startDisplayMenuWorkingCrew()
            
            # allows user to see working schedule for a single crew member
            elif selection == '6':

                while True:
                    crew_id = input('Enter the Crew members ID (SSN): ')
                    
                    try:
                        # checks if personal ID is 10 letters and an integer
                        int(crew_id)
                        if len(crew_id) == 10:

                            # Prints a work schedule for a crew member if he exists
                            get_schedule = CrewUI().showSchedule(crew_id)
                            if get_schedule == False:
                                print('No employee with this ID')
                            else:
                                return
                        else:
                            print('Invalid SSN')
        
                    except ValueError:
                        print('Invalid SSN')
                
            # Goes back to main menu
            elif selection == 'm':
                return

            else: 
                print('Invalid selection')
                print()