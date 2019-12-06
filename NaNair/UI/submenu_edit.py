# from UI.mainmenu import MainMenu
from API.LL_API import LL_API
from UI.crewUI import CrewUI
from UI.edit_employee_info_menu import EditEmployeeMenu

class SubMenuEdit:
    def __init__(self, logic_layer):
        print('sub menu Edit')
        self.logic_layer = logic_layer

    def startSubMenuEdit(self):
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
                new_datetime_str = input('Enter new date - (format 2019-11-20T15:24:00)') #ATH setja input
                flight_number = input('Enter flight voyage - (format NAXXXX)') #ATH setja input
                #ATH voyage id og breyta í voyage LL líka
                
                LL_API().change_voyage(new_datetime_str,flight_number)

            elif selection == '2':
                print('1 - Change emergency contact')
                print('2 - Change emergency phone number')
                user_selection = input()
                if user_selection == '1':
                    LL_API().changeDestinationEmergencyContact()
                elif user_selection == '2':
                    LL_API().changeDestinationEmergencyPhone()
                else:
                    print('Invalid selection!')
                # SETJA INN MENU HVERJU ÞÚ VILT BREYTA 
                # EDIT MENU DESTINATION 
                pass

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
                return # goes back to main menu 
                
                
            else:
                print("Invalid selection")