# from UI.mainmenu import MainMenu
from API.LL_API import LL_API
from UI.crewUI import CrewUI
from UI.edit_employee_info_menu import EditEmployeeMenu
from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI
from UI.destinationUI import DestinationUI
from UI.edit_existing_voyage_menu import EditExistingVoyage
class SubMenuEdit:

    EMPTY = 'empty'
    def __init__(self, logic_layer):
        print('sub menu Edit')
        self.logic_layer = logic_layer

    def startSubMenuEdit(self):
        # Header
        print('#'*20)
        print('{:^20}'.format('EDIT EXISTING DATA'))
        print('#'*20)
        print()

        

        start = True
        while start: 
            print('What would you like to edit? ')
            print()
            print('1 - Existing voyage')
            print('2 - Destination')
            print('3 - Employee')
            print('m - Main menu')

            selection = input().strip()

            if selection == '1':
                EditExistingVoyage().startEditExistingVoyage()
               

            elif selection == '2':
                # Change destination emergency contact
                print('1 - Change emergency contact')
                print('2 - Change emergency phone number')
                user_selection = input().strip()
                if user_selection == '1':
                    DestinationUI().changeEmergencyContactName()
                elif user_selection == '2':
                    DestinationUI().changeEmergencyContactPhoneNumber()
                else:
                    print('Invalid selection!')

            elif selection == '3':
                crew_id = CrewUI().getPersonalID()

                while True:
                    #lista upplýsingar um starfsmanninn
                    #employee = LL_API().get_crew_member_by_id(crew_id)
                    crew_member_found = CrewUI().showOneCrewMember(crew_id) #prentar út upplýsingar um starfsmann
                    if crew_member_found: 
                        return EditEmployeeMenu().editSelection(crew_id)    
                    else: 
                        crew_id = input('Input employee ID: ')
                        if DestinationUI().checkIfInt(crew_id):
                            if len(crew_id) == 10:
                                return crew_id
                            else:
                                print('Invalid personal ID!')
                        else:
                            print('Invalid personal ID!')
                        

            elif selection == 'm':
                # Back to main menu
                return 
                
            else:
                print("Invalid selection")