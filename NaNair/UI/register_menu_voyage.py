from UI.airplaneUI import AirplaneUI
from API.LL_API import LL_API

class RegisterMenuVoyage:
    
    def startRegisterVoyage(self):

        while True:

            destinations_class_list = LL_API().get_destinations()

            print('Please choose a destination. Available destinations are:')

            for destination in destinations_class_list:
                print(destination.getDestinationAirport() + '\t' + destination.getDestinationName())
            
            dest = input('Your destination (3 letters): ')
            

            # print('What type would you like to list? Please choose one of the following')
            # print('1 - NAFokkerF100')
            # print('2 - NAFokkerF28')
            # print('3 - NABAE146')
            # print()
            # selection = input()

            # if selection == '1':
            #     planeTypeID = 'NAFokkerF100'
            #     return AirplaneUI().showAirplanesByType(planeTypeID)
            # elif selection == '2':
            #     planeTypeID = 'NAFokkerF28'
            #     return AirplaneUI().showAirplanesByType(planeTypeID)
            # elif selection == '3':
            #     planeTypeID = 'NABAE146'
            #     return AirplaneUI().showAirplanesByType(planeTypeID)
            # else:
            #     print('Invalid selection')