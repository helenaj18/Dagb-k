from API.LL_API import LL_API
from UI.submenu_register import SubMenuRegister
from UI.EditMenus.submenu_edit import SubMenuEdit
from UI.DisplayMenus.submenu_display import SubMenuDisplay


class MainMenu:

    def start(self):
        # Header
        print()
        print()
        print('#'*28)
        print('{:^28}'.format('WELCOME'))
        print('#'*28)

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
