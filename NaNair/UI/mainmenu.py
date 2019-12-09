# import sys
# sys.path.insert(1,'/Users/valaroff/Desktop/T111PROG/verklegt1/NaNair/API')
# import LL_API

from API.LL_API import LL_API
from UI.submenu_register import SubMenuRegister
from UI.submenu_edit import SubMenuEdit
from UI.submenu_display import SubMenuDisplay


class MainMenu:
 

    def start(self):
        # Header
        print('#'*20)
        print('{:^20}'.format('WELCOME'))
        print('#'*20)

        while True: 
            print()
            print('What would you like to do?')
            print('_'*28)
            print() 

            print('1 - Register')
            print('2 - Display')
            print('3 - Edit existing data')
            print('q - Quit')
            print()
            selection = input()
            

            if selection == '1':
                # Register Menu
                
                SubMenuRegister().startSubMenuRegister()

            elif selection == '2':
                # Display Menu

                SubMenuDisplay().startSubMenuDisplay()

            elif selection =='3':
                # Edit Menu

                SubMenuEdit().startSubMenuEdit()

            elif selection == 'q':
                # Quit the program

                break

            else: 
                print('Invalid selection')
