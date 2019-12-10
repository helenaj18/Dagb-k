from UI.crewUI import CrewUI
from UI.DisplayMenus.display_menu_licensed_pilots import DisplayMenuAirplaneType

class DisplayMenuPilots: 
    def startDisplayPilots(self):
        '''Main display menu for pilots'''
        print()
        print('-'*40)
        print('{:^40}'.format('DISPLAY - Pilots'))
        print('-'*40)
        print()

        while True: 
            print('What would you like to display?')
            print()
            print('1 - Pilots with a license for a specific airplane')
            print('2 - All pilots sorted by license')
            print('m - Back to main menu')
            print()

            selection = input('Please choose one of the above (1/2/m): ').strip()

            if selection == '1':
                # Goes to another menu where the user can pick a license to list
                
                return DisplayMenuAirplaneType().startDisplayLicensedPilots()


            elif selection == '2':
                # List up pilots by license

                return CrewUI().showSortedByLicense()

            elif selection == 'm':
                # Goes back to main menu
                return

            # if none of the possible options were chosen
            else: 
                print('Invalid selection')