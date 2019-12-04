from UI.voyageUI import VoyageUI

class DisplayMenuVoyages: 
    def __init__(self, logic_layer):
        print('Display voyages')

    def startDisplayVoyages(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Voyages'))
        print('#'*20)
        print()


        while True: 
            print('What would you like to display?')
            print()
            print('1 - All voyages in a certain time frame')
            print('2 - A single voyage')
            print('m - Go back to display menu')
            print()

            selection = input()

            if selection == '1':
                #lista upp allar ferðir á ákveðnum tíma
                return VoyageUI().showAllVoyages()
                


            elif selection == '2':
                # lista ákveðna ferð
                pass

            elif selection == 'm':
                # fara aftur á display
                return 
            
            else: 
                print('Invalid selection')