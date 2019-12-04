from UI.crewUI import CrewUI

class DisplayMenuPilots: 
    def __init__(self, logic_layer):
        print('Display pilots')

    def startDisplayPilots(self):
        print('DISPLAY - Pilots')

        start = True
        while start: 
            print('What would you like to display?')
            print('1 - Pilots with a license for a specific airplane')
            print('2 - All pilots sorted by license')
            print('m - Go back to display menu')

            selection = input()

            if selection == '1':
                #lista upp flugmenn með x leyfi
                start = False


            elif selection == '2':
                # lista upp alla flugmenn eftir hvaða leyfi þeir hafa
                start = False

            elif selection == 'm':
                # fara aftur á display
                start = False
            else: 
                print('Invalid selection')