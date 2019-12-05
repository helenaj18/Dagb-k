from UI.crewUI import CrewUI

class DisplayMenuAttendants: 
    def __init__(self, logic_layer):
        print('Display pilots')

    def startDisplayAttendants(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Flight Attendants'))
        print('#'*20)
        print()

        start = True
        while start: 
            print('What would you like to display?')
            print()
            print('1 - All flight attendants')
            print('2 - Single flight attendant information')
            print('m - Go back to display menu')
            print()

            selection = input()

            if selection == '1':
                #lista upp alla flugþjóna


                start = False


            elif selection == '2':
                # lista stakan flugþjón eftir kennitölu

                return CrewUI().showSortedByLicense()
                start = False

            elif selection == 'm':
                # fara aftur á display
                start = False
            else: 
                print('Invalid selection')