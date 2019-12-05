from UI.crewUI import CrewUI
from UI.display_menu_attendants import DisplayMenuAttendants
from UI.display_menu_pilots import DisplayMenuPilots

# EMPLOYEE 

class DisplayMenuEmployee: 
    def __init__(self, logic_layer):
        print('Display employees')
        self.logic_layer = logic_layer

    def startDisplayMenu(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Employees'))
        print('#'*20)
        print()

        while True: 
          
            print('What would you like to display?') 
            print()

            print('1 - All employees')
<<<<<<< HEAD
            print('2 - Single employee')
            print('3 - Pilots')
            print('4 - Flight attendants')
=======
            print('2 - Pilots')
            print('3 - Flight attendants')
            print('4 - One Crew Member by ID')
>>>>>>> efef86ae2099928cf555e46cf974e2e2d9b1bba4
            print('m - back to display menu')
            print()
            selection = input()
            

            if selection == '1':
                CrewUI().showCrew()

            elif selection =='2':
                crew_id = input('Enter the Crew members ID (SSN): ')
                CrewUI.showOneCrewMember(crew_id)

            elif selection == '3':
                DisplayMenuPilots(self.logic_layer).startDisplayPilots()

<<<<<<< HEAD
            elif selection == '4':
                DisplayMenuAttendants(self.logic_layer).startDisplayAttendants()
            
            elif selection == 'm':
                return
=======
            elif selection =='4':
                crew_id = input('Enter the Crew members ID (SSN): ')
                CrewUI().showOneCrewMember(crew_id)
>>>>>>> efef86ae2099928cf555e46cf974e2e2d9b1bba4

            else: 
                print('Invalid selection')