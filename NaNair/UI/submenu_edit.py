# from UI.mainmenu import MainMenu
from API.LL_API import LL_API
from UI.crewUI import CrewUI
from UI.edit_employee_info_menu import EditEmployeeMenu
from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI

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
                VoyageUI().showOneVoyage(voyage)


                
                while True:
                    print("\nWhat do you want to change in voyage {}".format(voyage.getVoyageID()))
                    # Change existing voyage
                    print('1 - Add an airplane to a voyage')
                    print('2 - Add employees to a voyage')
                    print('3 - Change date')
                    print("m - Back to main menu")
                    user_selection = input()
                    if user_selection == '1':
                        return VoyageUI().addAircraftToVoyage(voyage)

                    
                    elif user_selection == '2':
                        if voyage.getAircraftID == 'empty ':

                            print()
                            print('No aircraft assigned to voyage')
                            print('Aircraft must me assigned before staff can be added')
                            print()
                            return 

                        else:

                            #crew_on_voyage_list = voyage.getCrewOnVoyage()
                            CrewUI().showNotWorkingCrew(voyage.getDepartureTime()) ################
                            print()

                            VoyageUI().addCrewToVoyage(voyage)
                            #return
                        
                                            
                    elif user_selection == '3':
                        # change date
                    
                        return VoyageUI().changeTimeOfVoyage()
                    
                    elif user_selection == 'm':
                        return
                    
                    else:
                        print('Invalid selection')


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