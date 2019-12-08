from UI.voyageUI import VoyageUI

class DisplayVoyageTimeFrame: 


    def startDisplayVoyageTimeFrame(self):

        while True: 
            print('What would you like to display?')
            print()
            print('1 - In a certain time frame')
            print('2 - On a specific day')
            print('m - Back to main menu')
            print()

            selection = input()

            if selection == '1':
                '''Lists up all voyages during a 
                   specific time frame'''

                return VoyageUI().showAllVoyagesInRange()
                
            elif selection == '2':
                ''' Lists all voyages on a specific day'''
                date_str = VoyageUI().getDateInput()

                return VoyageUI().showAllVoyagesInRange(date_str, date_str)

            elif selection == 'm':
                '''Goes back to main menu'''
                return 
            
            else:
                print('Invalid selection')