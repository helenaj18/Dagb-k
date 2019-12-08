from UI.voyageUI import VoyageUI
from UI.display_menu_voyage_time_frame import DisplayVoyageTimeFrame

class DisplayMenuVoyages: 
    def __init__(self, logic_layer):
        print('Display voyages')

    def startDisplayVoyages(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Voyages'))
        print('#'*20)
        print()


        while True: 
            print('What would you like to display?')
            print()
            print('1 - All voyages')
            print('2 - A single voyage by ID')
            print('m - Back to main menu')
            print()

            selection = input()

            if selection == '1':
                '''Goes to a new menu where the user
                   can choose a time frame or a 
                   specific day'''

                return DisplayVoyageTimeFrame().startDisplayVoyageTimeFrame()

            elif selection == '2':
                ''' Lists one voyage by ID'''
                # lista ákveðna ferð
                pass

            elif selection == 'm':
                '''Goes back to main menu'''
                return 
            
            else:
                print('Invalid selection')