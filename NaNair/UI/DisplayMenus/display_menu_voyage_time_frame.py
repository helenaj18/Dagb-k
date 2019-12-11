from UI.voyageUI import VoyageUI

class DisplayVoyageTimeFrame: 


    def startDisplayVoyageTimeFrame(self):

        while True: 
            print('-'*45)
            print('{:^45}'.format('What would you like to display? '))
            print('-'*45)
            print()
            print('1 - In a certain time frame')
            print('2 - On a specific day')
            print('m - Back to main menu')
            print()

            selection = input('\nPlease choose one of the above (1/2/m): ').strip()

            if selection == '1':
                # Lists up all voyages during a specific time frame
                
                if VoyageUI().showAllVoyagesInRange() != None:
                    return
                else:
                    print('\nNo voyages on these dates\n')
  
            elif selection == '2':
                # Lists all voyages on a specific day inputted by user
                print()
                date_str = VoyageUI().getDateInput()

                if VoyageUI().showAllVoyagesInRange(date_str, date_str):
                    return
                else:
                    print('\nNo voyages on this date\n')
                
            elif selection == 'm':
                #Goes back to main menu
                return 
            
            else:
                print('\nInvalid selection!\n')