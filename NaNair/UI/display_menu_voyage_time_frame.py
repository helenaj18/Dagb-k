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

                return VoyageUI().showAllVoyages()
                
            elif selection == '2':
                ''' Lists one voyage by ID'''
                # lista ákveðna ferð
                pass

            elif selection == 'm':
                '''Goes back to main menu'''
                return 
            
            else:
                print('Invalid selection')