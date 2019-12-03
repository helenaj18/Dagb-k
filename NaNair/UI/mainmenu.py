# import sys
# sys.path.insert(1,'/Users/valaroff/Desktop/T111PROG/verklegt1/NaNair/API')
# import LL_API

#from UI.API.LL_API import LL_API
from submenu_register import SubMenuRegister
from submenu_edit import SubMenuEdit
from submenu_display import SubMenuDisplay


class MainMenu:
    def __init__(self):
        #self.LogicLayer = LL_API()
        return 

    def start(self):
        print('WELCOME')
        start = True

        while start: 
          
            print('What would you like to do?') 

            print('1 - Register')
            print('2 - Display')
            print('3 - Edit existing data')
            print('q - Quit')
            print()
            selection = input()
            

            if selection == '1':
                next_menu = SubMenuRegister().startSubMenuRegister()
                start = False

            elif selection == '2':
                next_menu = SubMenuDisplay().startSubMenuDisplay()
                start = False

            elif selection =='3':
                next_menu = SubMenuEdit()
                start = False

            elif selection == 'q':
                break
            else: 
                print('Invalid selection')




#MainMenu().start()