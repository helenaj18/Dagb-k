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
        print('#'*28)
        print('{:^28}'.format('REGISTER'))
        print('#'*28)
        print()

        while True:
            print('What would you like to do?')
            print()
            print('1 - Add new Employee')
            print('2 - Add new Voyage')
            print('3 - Add new Airplane')
            print('4 - Add new Destination')

            print('m - Main menu')
            print()

            selection = input().strip()

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
                # Add new destination

                return DestinationUI().addDestination()

                
            elif selection == 'm':
                # Back to main menu
                return

            else:
                print("Invalid selection")
                
