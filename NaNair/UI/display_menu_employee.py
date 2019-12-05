from UI.crewUI import CrewUI
from UI.display_menu_attendants import DisplayMenuAttendants
from UI.display_menu_pilots import DisplayMenuPilots

# EMPLOYEE 

class DisplayMenuEmployee: 
    def __init__(self):
        print('in diplay employee')

    def startDisplayMenu(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Employees'))
        print('#'*20)
        print()

        start = True

        while start: 
          
            print('What would you like to display?') 
            print()

            print('1 - All employees)
            print('2 - Pilots')
            print('3 - Flight attendants')
            print('m - back to display menu')
            print()
            selection = input()
            

            if selection == '1':
                next_menu = CrewUI().showCrew()
                start = False

            elif selection == '2':
                next_menu = DisplayMenuAttendants(self.logic_layer).startDisplayAttendants()
                start = False

            elif selection == '3':
                next_menu = DisplayMenuPilots(self.logic_layer).startDisplayPilots()

            elif selection =='4':
                next_menu = SubMenuEdit()
                start = False

            elif selection == 'q':
                break
            else: 
                print('Invalid selection')