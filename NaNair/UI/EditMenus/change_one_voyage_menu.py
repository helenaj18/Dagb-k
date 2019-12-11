from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI


class ChangeOneVoyageMenu:

    EMPTY = 'empty'
    
    def startChangeOneVoyageMenu(self):
        '''Menu to change one voyage'''

        # status of voyage (not departed, in air, completed)
        voyage_state_str = VoyageUI().getStatusOfVoyage(self.voyage)

        if voyage_state_str != 'Completed':
            self.changeNotCompletedVoyage()
        
        elif voyage_state_str == 'Completed':
            print('\nDo you want to change sold seats on voyage?\n')
            print('1 - Yes\n2 - No (Go back to edit existing voyage)')
            selection = input().strip()
            if selection == '1':
                VoyageUI().showOneVoyage(self.voyage)
                self.changeCompletedVoyage()
            elif selection == '2':
                return 
            else:
                print('invalid selection')

    def changeCompletedVoyage(self):
        while True:
            print("\nWhat do you want to change in voyage {}?\n".format(self.voyage.getVoyageID()))
            print('1 - Change number of sold seats out')
            print('2 - Change number of sold seats home')

            print('m - Back to edit existing voyage\n')
            user_selection = input('Please choose one of the above (1-2 or m): ').strip()

            if user_selection == '1':
                VoyageUI().changeSoldSeats(self.voyage,'out')
            
            elif user_selection == '2':
                VoyageUI().changeSoldSeats(self.voyage,'home')

            elif user_selection == 'm':
                return
            
            else:
                print('Invalid selection')

            
                
    def changeNotCompletedVoyage(self):
        while True:
            print("\nWhat do you want to change in voyage {}?\n".format(self.voyage.getVoyageID()))

            # Change existing voyage
            print('1 - Add an airplane to a voyage')
            print('2 - Add employees to a voyage')
            print('3 - Change number of sold seats out')
            print('4 - Change number of sold seats home')

            print('m - Back to edit menu voyage\n')
            user_selection = input('Please choose one of the above (1-4 or m): ').strip()
            
            if user_selection == '1':
                # Gets a list of all airplane insignias
                airplane_insignia_list = AirplaneUI().getAirplaneInsigniaList()
                
                # If an aircraft is assigned to the voyage 
                # the aircraft ID would be in the airplane insignia list
                if self.voyage.getAircraftID() in airplane_insignia_list:
                    print('-'*40+'\n')
                    print('Airplane already assigned to Voyage!')
                    print('\n'+'-'*40)
                    continue
                else:
                    VoyageUI().addAircraftToVoyage(self.voyage)
                    continue
            
            elif user_selection == '2':
                if self.voyage.getAircraftID() == self.EMPTY:
                    print('-'*40+'\n')
                    print('No aircraft assigned to voyage')
                    print('Aircraft must me assigned before staff can be added')
                    print('\n'+'-'*40)

                else:
                    return VoyageUI().addCrewToVoyage(self.voyage)
            
            elif user_selection == '3':
                VoyageUI().changeSoldSeats(self.voyage,'out')
            
            elif user_selection == '4':
                VoyageUI().changeSoldSeats(self.voyage,'home')

            elif user_selection == 'm':
                return
            
            else:
                print('Invalid selection')