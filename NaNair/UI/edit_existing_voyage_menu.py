from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI
from UI.crewUI import CrewUI
from API.LL_API import LL_API
from UI.change_one_voyage_menu import ChangeVoyageMenu

class EditExistingVoyage:
    EMPTY = 'empty'

    def startEditExistingVoyage(self):
        while True:
            print()
            print('1 - Enter voyage ID')
            print('2 - See a list of voyages on a specific time range')
            print('m - Back to edit menu')
            print()
            selection = input('Please choose one of the above (1/2/m): ').strip()

            if selection == '1':
                voyage = VoyageUI().checkCompleted()
                
                if voyage != None:
                    VoyageUI().showOneVoyage(voyage)
            
            elif selection == '2':
                print("Select date range to find a voyage to edit")
                voyage = VoyageUI().queryOneVoyage()
                if voyage:
                    VoyageUI().showOneVoyage(voyage)
                    print()
                else:
                    return 

            elif selection == 'm':
                return

            else:
                print('Invalid selection!')
                print()

            if voyage:

                ChangeVoyageMenu(voyage).startChangeVoyageMenu()
                