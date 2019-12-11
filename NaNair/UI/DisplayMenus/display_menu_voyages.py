from UI.voyageUI import VoyageUI
from UI.DisplayMenus.display_menu_voyage_time_frame import DisplayVoyageTimeFrame

class DisplayMenuVoyages: 
    '''Main display menu for voyages'''

    def startDisplayVoyages(self):
        print()
        print('-'*45)
        print('{:^45}'.format('DISPLAY - Voyages'))
        print('-'*45)
        print()

        while True: 
            print('What would you like to display?')
            print()
            print('1 - All voyages')
            print('2 - A single voyage by ID')
            print('m - Back to main menu')
            print()

            selection = input('Please choose one of the above (1/2/m): ').strip()

            if selection == '1':
                #Goes to a new menu where the user can choose a time frame or a 
                #specific day

                return DisplayVoyageTimeFrame().startDisplayVoyageTimeFrame()

            elif selection == '2':
                # Lists one voyage by ID

                if VoyageUI().showOneVoyage() != None:
                    return
                else:
                    print('No voyage with this ID\n')


            elif selection == 'm':
                #Goes back to main menu
                return
            
            else:
                print('\nInvalid selection\n')