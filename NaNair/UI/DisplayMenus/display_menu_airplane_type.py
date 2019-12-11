from UI.airplaneUI import AirplaneUI

class DisplayMenuAirplaneType:
    
    def startDisplayAirplaneType(self):
        '''Menu for displaying airplane types'''

        success = False
        airplane_types = AirplaneUI().getAirplaneTypes()

        while True:
            print('\nWhat type would you like to list? Please choose one of the following')
            counter = 1
            for airplane_type in airplane_types:
                print('{} - {}'.format(counter,airplane_type))
                counter += 1

            selection = input('\nPlease choose one of the above: ').strip()

            for i in range(1,counter+1):
                if selection == str(i):
                    planeTypeId = airplane_types[i-1].getplaneTypeID()
                    success = True
                    return AirplaneUI().showAirplanesByType(planeTypeId)

            if not success:
                print('\nInvalid selection!\n')