from UI.voyageUI import VoyageUI

class DisplayMenuVoyages: 
    def __init__(self, logic_layer):
        print('Display voyages')

    def startDisplayVoyages(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Voyages'))
        print('#'*20)
        print()

        start = True
        while start: 
            print('What would you like to display?')
            print()
            print('1 - All voyages in a certain time frame')
            print('2 - A single voyage')
            print('m - Go back to display menu')
            print()

            selection = input()

            if selection == '1':
                #lista upp allar ferðir á ákveðnum tíma
                pass
                start = False


            elif selection == '2':
                # lista ákveðna ferð
                start = False

            elif selection == 'm':
                # fara aftur á display
                return 
                start = False
            else: 
                print('Invalid selection')