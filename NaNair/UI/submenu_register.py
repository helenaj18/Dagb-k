from API.LL_API import LL_API
import datetime

class SubMenuRegister: 
    def __init__(self, logic_layer): # muna ap taka inn logic layer sem main menu bjó til!!1!!!!!
        print('sub menu Register')
        self.logic_layer = logic_layer


    def startSubMenuRegister(self):
        print('#'*20)
        print('{:^20}'.format('REGISTER'))
        print('#'*20)
        print()

        print('What would you like to do?')
        print()

        while True:
            print('1 - Add New employee')
            print('2 - Add staff to an available voyage')
            print('3 - Add New voyage')
            print('m - Main menu')
            print()

            selection = input()

            if selection == '1': 
                pass
            elif selection == '2':
                pass
            elif selection == '3':
                destination_of_voyage = input('Destination: (3char airport code)').upper()
                print('Departure time')
                dep_year = input('Year: ')
                dep_month = input('Month: ')
                dep_day = input('Day: ')
                dep_hour = input('Hour: ')
                dep_minute = input('Minute: ')
                departure_time = datetime.datetime(dep_year,dep_month,dep_day,dep_hour,dep_minute,0).isoformat()


                LL_API().add_voyage(destination_of_voyage,departure_time)


                
            elif selection == 'm':
                return

            else:
                print("Invalid selection")
                
