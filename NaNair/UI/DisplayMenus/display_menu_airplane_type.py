from UI.airplaneUI import AirplaneUI

class DisplayMenuAirplaneType:
    
    def startDisplayAirplaneType(self):
        '''Menu for displaying airplane types'''

        while True:
            print('\nWhat type would you like to list? Please choose one of the following')
            print('1 - NAFokkerF100')
            print('2 - NAFokkerF28')
            print('3 - NABAE146')
            print('m - Back to main menu')
            print()
            selection = input().strip()

            # User chooses NAFokkerF100
            if selection == '1':
                planeTypeID = 'NAFokkerF100'
                return AirplaneUI().showAirplanesByType(planeTypeID)
            
            # User chooses NAFokkerF28
            elif selection == '2':
                planeTypeID = 'NAFokkerF28'
                return AirplaneUI().showAirplanesByType(planeTypeID)
            
            # User chooses NABAE146
            elif selection == '3':
                planeTypeID = 'NABAE146'
                return AirplaneUI().showAirplanesByType(planeTypeID)
            
            # User chooses to go back to main menu
            elif selection == 'm':
                return
                
            # User does not choose any of the given possibilities
            else:
                print('Invalid selection!')
                print()