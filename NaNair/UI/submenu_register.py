#from mainmenu import MainMenu

class SubMenuRegister: 
    def __init__(self): # muna ap taka inn logic layer sem main menu bjó til!!1!!!!!
        print('sub menu Register')
        #self.logic.........


    def startSubMenuRegister(self):
        print('REGISTER')
        print('What would you like to do?')
        start = True
        while start:
            print('1 - New employee')
            print('2 - Add staff to an available voyage')
            print('m - Main menu')

            selection = input()

            if selection == '1': 
                start = False
            elif selection == '2':
                start = False
            elif selection == 'm':
                #next_menu = MainMenu()
                start = False
            else:
                print("Invalid selection")
                
