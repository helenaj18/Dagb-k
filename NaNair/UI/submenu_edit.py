# from UI.mainmenu import MainMenu
from LL.voyageLL import VoyageLL

class SubMenuEdit:
    def __init__(self, logic_layer):
        print('sub menu Edit')
        self.logic_layer = logic_layer

    def startSubMenuEdit(self):
        print('EDIT EXISTING DATA')
        print('What would you like to edit? ')

        start = True
        
        while start: 
            print('1 - Existing voyage')
            print('2 - Destination')
            print('m - Main menu')

            selection = input()

            if selection == '1': 
                start = False
                VoyageLL().changeDateTimeOfVoyage()

            elif selection == '2':
                start = False
            elif selection == 'm':
                # next_menu = MainMenu() ATH HVERNIG MAÐUR FER TIL BAKA Í MAIN MENU
                start = False
            else:
                print("Invalid selection")