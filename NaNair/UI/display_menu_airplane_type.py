from UI.airplaneUI import AirplaneUI

class DisplayMenuAirplaneType:
    
    def startDisplayAirplaneType(self):

        while True:
            print('What type would you like to list? Please choose one of the following')
            print('1 - NAFokkerF100')
            print('2 - NAFokkerF28')
            print('3 - NABAE146')
            print('m - Back to main menu')
            print()
            selection = input()

            if selection == '1':
                planeTypeID = 'NAFokkerF100'
                return AirplaneUI().showAirplanesByType(planeTypeID)
            elif selection == '2':
                planeTypeID = 'NAFokkerF28'
                return AirplaneUI().showAirplanesByType(planeTypeID)
            elif selection == '3':
                planeTypeID = 'NABAE146'
                return AirplaneUI().showAirplanesByType(planeTypeID)
            
            elif selection == 'm':
                return
                
            else:
                print('Invalid selection')