from UI.display_menu_airplanes import DisplayMenuAirplanes

class SubMenuDisplay: 
    def __init__(self, logic_layer):
        print('sub menu Display')
        self.logic_layer = logic_layer
    
    def startSubMenuDisplay(self):
        print('DISPLAY')
        print('What would you like to display? ')

        print('1 - Airplanes')
        print('2 - Destinations')
        print('3 - Voyages')
        print('4 - Flight Attendants')
        print('5 - Pilots')

        print('m - Main menu')

        selection = input()

        if selection == '1': 
            next_menu = DisplayMenuAirplanes(self.logic_layer).startDisplayAirplanes()
        elif selection == '2':
            # fara beint í destination UI 
            pass
        elif selection == '3':
            # employee
            pass
        elif selection == '4':
            pass
        elif selection == '5':
            pass
        elif selection == 'm':
            #next_menu = MainMenu()
            pass
        else:
            print("Invalid selection")