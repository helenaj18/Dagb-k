# from UI.mainmenu import MainMenu
from API.LL_API import LL_API
from UI.crewUI import CrewUI

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
                # prenta Destination upplýsingar
                # SETJA INN MENU HVERJU ÞÚ VILT BREYTA 
                # EDIT MENU DESTINATION 
                pass

            elif selection == '3':
                crew_id = input('Input employee ID: ')
                #lista upplýsingar um starfsmanninn
                CrewUI().showOneCrewMember(crew_id)
                
                #menu - hverju viltu breyta
                print('What would you like to change?')
                print()
                #ef flugmaður
        
                print('1 - Address')
                print('2 - Phone number')
                print('3 - Email')
                print('4 - Rank')
                print('5 - License')

                #eða ef flugfreyja
                print('1 - Address')
                print('2 - Phone number')
                print('3 - Email')
                print('4 - Rank')

            elif selection == 'm':
                return # goes back to main menu 
                
                
            else:
                print("Invalid selection")