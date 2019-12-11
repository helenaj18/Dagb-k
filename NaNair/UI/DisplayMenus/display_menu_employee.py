from UI.crewUI import CrewUI
from UI.DisplayMenus.display_menu_pilots import DisplayMenuPilots
from UI.DisplayMenus.display_menu_working_crew import DisplayMenuWorkingCrew
import datetime


class DisplayMenuEmployee: 
    def startDisplayMenuEmployee(self):
        '''Main display for employees'''    
        # banner:
        print()
        print('-'*45)
        print('{:^45}'.format('DISPLAY - Employees'))
        print('-'*45)
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
            print('m - Back to main menu')

            selection = input('\nPlease choose one of the above (1-6 or m): ').strip()
            
            # All employees are displayed
            if selection == '1':
                return CrewUI().showCrew()

            # A single employee is displayed with more percise info
            elif selection =='2':
                print()
                while True:
                    crew_id = input('Enter the Crew members ID (SSN): ').strip()
                    
                    # checks if the personal ID is 10 letters and an integer
                    try:
                        int(crew_id)
                        if len(crew_id) == 10:
                            # Prints information about one crew member
                            return CrewUI().showOneCrewMember(crew_id)
                        else:
                            print('\nInvalid SSN!\n')
                    except ValueError:
                        print('\nInvalid SSN!\n')
            
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
                print()
                crew_id = CrewUI().getPersonalID()
                
                # Prints a work schedule for a crew member if he exists
                get_schedule = CrewUI().showSchedule(crew_id)
                if get_schedule == False:
                    print('\nNo employee with this ID\n')
                else:
                    return 
                
            # Goes back to main menu
            elif selection == 'm':
                return

            else: 
                print('Invalid selection')
                print()