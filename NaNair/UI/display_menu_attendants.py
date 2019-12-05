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
                return CrewUI().showAllFlightAtt()
                start = False


            elif selection == '2':
                # lista stakan flugþjón eftir kennitölu

                attendant_id = input('Input flight attendant ID: ')

                return CrewUI().showOneFlightAtt(attendant_id)
                start = False

            elif selection == 'm':
                # fara aftur á display
                return
            else: 
                print('Invalid selection')