from API.LL_API import LL_API
from UI.crewUI import CrewUI
from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI
from UI.destinationUI import DestinationUI
import datetime


class SubMenuRegister: 

    def startSubMenuRegister(self):
        # Header
        print()
        print('#'*45)
        print('{:^45}'.format('REGISTER'))
        print('#'*45)
        print()

        while True:
            print('-'*45)
            print('{:^45}'.format('What would you like to do?'))
            print('-'*45)
            print()
            print('1 - Add new Employee')
            print('2 - Add new Voyage')
            print('3 - Add new Airplane with an existing type')
            print('4 - Add new Airplane Type')
            print('4 - Add new Destination')

            print('m - Main menu')
            print()

            selection = input('Please choose one of the above (1-4 or m): ').strip()

            if selection == '1': 
                # Add new employee

                return CrewUI().addCrew()

            elif selection == '2':
                # Add new voyage

                return VoyageUI().addVoyage()
                
            elif selection == '3':
                # Add new Airplane

                return AirplaneUI().addAirplane()
            
            elif selection == '4':
                
                return AirplaneUI().addAirplaneType()

            elif selection == '5':
                # Add new destination

                return DestinationUI().addDestination()

                
            elif selection == 'm':
                # Back to main menu
                return

            else:
                print("\nInvalid selection!\n")
                
