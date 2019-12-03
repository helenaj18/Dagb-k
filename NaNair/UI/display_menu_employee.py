from UI.crewUI import CrewUI

# EMPLOYEE 

class DisplayMenuEmployee: 
    def __init__(self):
        print('in diplay employee')

    def startDisplayMenu(self):
        print('DISPLAY - Employees')
        start = True

        while start: 
          
            print('What would you like to display?') 

            print('1 - All employees)
            print('2 - Single employee ')
            print('3 - Working status on a certain date'')
            print('m - back to display menu')
            print()
            selection = input()
            

            if selection == '1':
                next_menu = CrewUI().showCrew()
                start = False

            elif selection == '2':
                next_menu = CrewUI().
                start = False

            elif selection =='3':
                next_menu = SubMenuEdit()
                start = False

            elif selection == 'q':
                break
            else: 
                print('Invalid selection')