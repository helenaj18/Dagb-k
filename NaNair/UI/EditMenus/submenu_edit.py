from API.LL_API import LL_API
from UI.crewUI import CrewUI
from UI.EditMenus.edit_employee_info_menu import EditEmployeeMenu
from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI
from UI.destinationUI import DestinationUI
from UI.EditMenus.edit_existing_voyage_menu import EditExistingVoyage
class SubMenuEdit:

    EMPTY = 'empty'

    def startSubMenuEdit(self):
        '''Main editing menu'''
        # Header
        print()
        print('#'*45)
        print('{:^45}'.format('EDIT EXISTING DATA'))
        print('#'*45)
        print()

        start = True
        while start: 
            print('-'*45)
            print('{:^45}'.format('What would you like to edit? '))
            print('-'*45)
            print()
            print('1 - Existing voyage')
            print('2 - Destination')
            print('3 - Employee')
            print('m - Main menu')
            print()

            selection = input('Please chose one of the above: ').strip()

            if selection == '1':
                # edit existing voyage
                EditExistingVoyage().startEditExistingVoyage()
               

            elif selection == '2':
                # Change destination emergency contact
                print('1 - Change emergency contact')
                print('2 - Change emergency phone number')
                user_selection = input('Please choose one of the above (1 or 2)').strip()

                if user_selection == '1':
                    # name of emergency contact changed
                    DestinationUI().changeEmergencyContactName()
                elif user_selection == '2':
                    # phone number of emergency contact changed
                    DestinationUI().changeEmergencyContactPhoneNumber()
                else:
                    print('Invalid selection!')

            elif selection == '3':
                while True:
                    # Prints out information about an employee with inputted crew id
                    crew_id = CrewUI().getPersonalID()
                    if crew_id:
                        crew_member_found = CrewUI().showOneCrewMember(crew_id) 
                        # Check if id is valid
                        if crew_member_found:
                            return EditEmployeeMenu().editSelection(crew_id)
                    else:
                        return
                        
            elif selection == 'm':
                # Back to main menu
                return 
                
            else:
                print("Invalid selection")