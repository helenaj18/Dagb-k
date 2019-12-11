from UI.voyageUI import VoyageUI
from UI.crewUI import CrewUI
from API.LL_API import LL_API
from UI.EditMenus.change_one_voyage_menu import ChangeOneVoyageMenu

class EditExistingVoyage:
    EMPTY = 'empty'

    def startEditExistingVoyage(self):
        '''Menu for editing existing voyages'''
        while True:
            print('\n'+'-'*45)
            print('{:^45}'.format('Edit existing voyage menu'))
            print('-'*45)
            print('1 - Enter voyage ID')
            print('2 - See a list of voyages on a specific time range')
            print('m - Back to edit menu')
            print()
            selection = input('Please choose one of the above: ').strip()
            print()

            # voyage found by entering voyage 
            if selection == '1':
                # check if voyage was in the past and cannot be changed
                voyage = VoyageUI().checkCompleted()
                voyage_state = LL_API().get_status_of_voyage(voyage)
                
                if voyage_state != 'Completed':
                    # print info on voyage
                    VoyageUI().showOneVoyage(voyage)


            # voyage found by viewing all voyages during an inputted time frame
            elif selection == '2':
                print('Select date range to find a voyage to edit')
                voyage = VoyageUI().checkVoyagesInRange()
                if voyage:
                    VoyageUI().showOneVoyage(voyage)
                    print()
                else:
                    return 

            elif selection == 'm':
                # goes back to main menu
                return

            else:
                # if none of the possible options was chosen
                print('Invalid selection!\n')
                voyage = None
                
            if voyage:
                # voyage instance sent to editing menu
                ChangeOneVoyageMenu(voyage).startChangeOneVoyageMenu()

  
