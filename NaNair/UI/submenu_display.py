from UI.display_menu_airplanes import DisplayMenuAirplanes
from UI.display_menu_voyages import DisplayMenuVoyages
from UI.destinationUI import DestinationUI
from UI.display_menu_employee import DisplayMenuEmployee
from API.LL_API import LL_API

class SubMenuDisplay: 
    def __init__(self, logic_layer):
        print('sub menu Display')
        self.logic_layer = logic_layer
    
    def startSubMenuDisplay(self):
        # Header
        print('#'*20)
        print('{:^20}'.format('DISPLAY'))
        print('#'*20)
        print()

        while True:
            print('What would you like to display? ')
            print()

            print('1 - Airplanes')
            print('2 - Destinations')
            print('3 - Voyages')
            print('4 - Employees')
            print('m - Main menu')
            print()

            selection = input()

            if selection == '1': 
                # Display Menu Airplanes
                return DisplayMenuAirplanes(self.logic_layer).startDisplayAirplanes()
            
            elif selection == '2':
                # Display Destination
                return DestinationUI().showAllDestinations()

            elif selection == '3':
                # Display Menu Voyages
                return DisplayMenuVoyages(self.logic_layer).startDisplayVoyages()

            elif selection == '4':
                # Display Menu Employees
                return DisplayMenuEmployee(self.logic_layer).startDisplayMenu()
        
            elif selection == 'm':
                # Back to main menu
                return 
            else:
                print("Invalid selection")