from display_menu_airplanes import DisplayMenuAirplanes

class SubMenuDisplay: 
    def __init__(self):
        print('sub menu Display')
    
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
            next_menu = DisplayMenuAirplanes().startDisplayAirplanes()
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