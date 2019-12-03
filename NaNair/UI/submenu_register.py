#from mainmenu import MainMenu

class SubMenuRegister: 
    def __init__(self, logic_layer): # muna ap taka inn logic layer sem main menu bjó til!!1!!!!!
        print('sub menu Register')
        self.logic_layer = logic_layer


    def startSubMenuRegister(self):
        print('REGISTER')
        print('What would you like to do?')

        while True:
            print('1 - New employee')
            print('2 - Add staff to an available voyage')
            print('3 - New voyage')
            print('m - Main menu')

            selection = input()

            if selection == '1': 
                pass
            elif selection == '2':
                pass
            elif selection == '3':
                pass
            elif selection == 'm':
                return

            else:
                print("Invalid selection")
                
