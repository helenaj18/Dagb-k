# from UI.mainmenu import MainMenu
from API.LL_API import LL_API
from UI.crewUI import CrewUI
from UI.edit_employee_info_menu import EditEmployeeMenu
from UI.voyageUI import VoyageUI

class SubMenuEdit:
    def __init__(self, logic_layer):
        print('sub menu Edit')
        self.logic_layer = logic_layer

    def startSubMenuEdit(self):
        # Header
        print('#'*20)
        print('{:^20}'.format('EDIT EXISTING DATA'))
        print('#'*20)
        print()

        print('What would you like to edit? ')
        print()

        start = True
        while start: 
            print('1 - Existing voyage')
            print('2 - Destination')
            print('3 - Employee')
            print('m - Main menu')

            selection = input()

            if selection == '1':
                print("Select date range to find a voyage to edit")
                voyage = VoyageUI().queryOneVoyage()
                keep_editing = True
                while keep_editing:
                    print("\nWhat do you want to change in voyage {}".format(voyage.getVoyageID()))
                    # Change existing voyage
                    print('1 - Register employee on a voyage')
                    print('2 - Change date')
                    print("m - go back")
                    user_selection = input()

                    if user_selection == '1':
                        
                        crew_member = CrewUI().queryShowNotWorkingCrew(voyage.getDepartureTime())
                        print('You must add 1 captain, 1 copilot, 1 flight atttendant')
                        success = True
                        while True:
                            try:
                                voyage.addCrewMember(crew_member)

                            except Exception as e:
                                success = False
                                print(e)
                                input("Press any key to try continue editing voyage")
                            
                            if success:
                                print('{} - {}, was added to voyage {}'.format(
                                            crew_member.getName(),
                                            crew_member.getRole(), 
                                            voyage.getVoyageID()
                                        ))
                                if crew_member.getRole() 

                                            
                    elif selection == '2':
                        # change date
                        new_datetime_str = input('Enter new date - (format 2019-11-20T15:24:00)') 
                        flight_number = input('Enter flight voyage - (format NAXXXX)') 
                        #ATH voyage id og breyta í voyage LL líka
                        
                        LL_API().change_voyage_dates(new_datetime_str,flight_number)


            elif selection == '2':
                # Change destination emergency contact
                print('1 - Change emergency contact')
                print('2 - Change emergency phone number')
                user_selection = input()
                if user_selection == '1':
                    LL_API().changeDestinationEmergencyContact()
                elif user_selection == '2':
                    LL_API().changeDestinationEmergencyPhone()
                else:
                    print('Invalid selection!')

            elif selection == '3':
                crew_id = input('Input employee ID: ')
                while True:
                    #lista upplýsingar um starfsmanninn
                    #employee = LL_API().get_crew_member_by_id(crew_id)
                    crew_member_found = CrewUI().showOneCrewMember(crew_id) #prentar út upplýsingar um starfsmann
                    if crew_member_found: 
                        return EditEmployeeMenu().editSelection(crew_id)    
                    else: 
                        crew_id = input('Input employee ID: ')
                        

            elif selection == 'm':
                # Back to main menu
                return 
                
            else:
                print("Invalid selection")