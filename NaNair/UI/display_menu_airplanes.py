from UI.airplaneUI import AirplaneUI


class DisplayMenuAirplanes: 
    def __init__(self, logic_layer):
        print('Display airplanes')

    def startDisplayAirplanes(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Airplanes'))
        print('#'*20)
        print()

        while True: 
            print('What would you like to display?')
            print()
            print('1 - List all airplanes')
            print('2 - List airplanes by type')
            print('m - Go back to display menu')
            print()

            selection = input()

            if selection == '1':
                #lista upp allar flugvelar 
                airplanes = AirplaneUI().showAllPlanes()

                header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity','length','height','wingspan')
                print(header_str)
                print('-'*len(header_str))

                for elem in airplanes:
                    print(elem)

            elif selection == '2':
                print('What type would you like to list?')
                print('NAFokkerF100')
                print('NAFokkerF28')
                print('NABAE146')
                print()
                planeTypeID = input()

                airplanes = AirplaneUI().showAirplanesByType(planeTypeID)

                header_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('PlaneInsignia','planeTypeId','Manufacturer','Model','Capacity','length','height','wingspan')
                print(header_str)
                print('-'*len(header_str))

                for elem in airplanes:
                    print(elem)


            elif selection == 'm':
                # fara aftur á display
                return
            else: 
                print('Invalid selection')