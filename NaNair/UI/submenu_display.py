from UI.display_menu_airplanes import DisplayMenuAirplanes
from UI.display_menu_voyages import DisplayMenuVoyages
from UI.display_menu_pilots import DisplayMenuPilots
from API.LL_API import LL_API

class SubMenuDisplay: 
    def __init__(self, logic_layer):
        print('sub menu Display')
        self.logic_layer = logic_layer
    
    def startSubMenuDisplay(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY'))
        print('#'*20)
        print()

        print('What would you like to display? ')
        print()

        print('1 - Airplanes')
        print('2 - Destinations')
        print('3 - Voyages')
        print('4 - Flight Attendants')
        print('5 - Pilots')
        print('m - Main menu')
        print()

        selection = input()

        if selection == '1': 
            next_menu = DisplayMenuAirplanes(self.logic_layer).startDisplayAirplanes()
        elif selection == '2':
            dests = LL_API().get_destinations()
            for elem in dests:
                print(elem)
        elif selection == '3':
            next_menu = DisplayMenuVoyages(self.logic_layer).startDisplayVoyages()
        elif selection == '4':
            #listar upp alla flight attendants
            pass
        elif selection == '5':
            next_menu = DisplayMenuPilots(self.logic_layer).startDisplayPilots()
        elif selection == 'm':
            #next_menu = MainMenu()
            return 
        else:
            print("Invalid selection")