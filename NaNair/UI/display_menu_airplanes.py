from airplaneUI import AirplaneUI

class DisplayMenuAirplanes: 
    def __init__(self):
        print('Display airplanes')

    def startDisplayAirplanes(self):
        print('DISPLAY - Airplanes')

        start = True
        while start: 
            print('What would you like to display?')
            print('1 - List all airplanes')
            print('2 - List airplanes by type')
            print('m - Go back to display menu')

            selection = input()

            if selection == '1':
                #lista upp allar flugvelar 
                AirplaneUI().ShowAllPlanes()
                start = False


            elif selection == '2':
                # lista eftir typu
                start = False

            elif selection == 'm':
                # fara aftur á display
                start = False
            else: 
                print('Invalid selection')