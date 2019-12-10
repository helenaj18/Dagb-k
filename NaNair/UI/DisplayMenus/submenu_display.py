from UI.DisplayMenus.display_menu_airplanes import DisplayMenuAirplanes
from UI.DisplayMenus.display_menu_voyages import DisplayMenuVoyages
from UI.destinationUI import DestinationUI
from UI.DisplayMenus.display_menu_employee import DisplayMenuEmployee
from API.LL_API import LL_API

class SubMenuDisplay: 
    def startSubMenuDisplay(self):
        # Header
        print()
        print('#'*28)
        print('{:^28}'.format('DISPLAY'))
        print('#'*28)
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
                return DisplayMenuAirplanes().startDisplayAirplanes()
            
            elif selection == '2':
                # Display Destination
                return DestinationUI().showAllDestinations()

            elif selection == '3':
                # Display Menu Voyages
                return DisplayMenuVoyages().startDisplayVoyages()

            elif selection == '4':
                # Display Menu Employees
                return DisplayMenuEmployee().startDisplayMenuEmployee()
        
            elif selection == 'm':
                # Back to main menu
                return 
            else:
                print("Invalid selection")
                print()