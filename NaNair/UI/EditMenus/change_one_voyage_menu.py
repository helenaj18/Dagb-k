from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI


class ChangeOneVoyageMenu:

    def __init__(self,voyage):
        self.voyage = voyage

    EMPTY = 'empty'
    
    def startChangeOneVoyageMenu(self):
        '''Menu to change one voyage'''

        # status of voyage (not departed, in air, completed)
        voyage_state_str = VoyageUI().getStatusOfVoyage(self.voyage)

        # if voyage has not yet departed
        if voyage_state_str != 'Completed':
            # go to change voyage
            self.changeNotCompletedVoyage()
        
        # if voyage was in the past
        elif voyage_state_str == 'Completed':
            while True:
                print('\nDo you want to change sold seats on voyage?\n')
                print('1 - Yes\n2 - No (Go back to edit existing voyage)')
                selection = input('Please choose one of the above: ').strip()

                # go to change sold seats on voyage
                if selection == '1':
                    # info on one voyage printed
                    VoyageUI().showOneVoyage(self.voyage)

                    # go to change voyage
                    self.changeCompletedVoyage()
                # go back
                elif selection == '2':
                    return 
                else:
                    print('invalid selection')

    def changeCompletedVoyage(self):
        '''Allows user to modify voyages that were in the past'''
        while True:
            print('-'*45)
            print('What do you want to change in voyage {}?'.format(self.voyage.getVoyageID()))
            print('-'*45+'\n')
            print('1 - Change number of sold seats out')
            print('2 - Change number of sold seats home')            
            print('m - Back to edit existing voyage\n')
            user_selection = input('Please choose one of the above: ').strip()

            if user_selection == '1':
                #user goes to change nr of sold seats on flight out
                VoyageUI().changeSoldSeats(self.voyage,'out')
            
            elif user_selection == '2':
                #user goes to change nr of sold seats home
                VoyageUI().changeSoldSeats(self.voyage,'home')

            elif user_selection == 'm':
                # user goes back to main menu
                return
            # if none of the possible were chosen
            else:
                print('Invalid selection')

            
                
    def changeNotCompletedVoyage(self):
        '''Change info of voyage that has not yet departed'''
        
        while True:
            print('-'*45)
            print("\nWhat do you want to change in voyage {}?\n".format(self.voyage.getVoyageID()))
            print('-'*45+'\n')
            # Change existing voyage
            print('1 - Add an airplane to a voyage')
            print('2 - Add employees to a voyage')
            print('3 - Change number of sold seats out')
            print('4 - Change number of sold seats home')
            print('5 - Remove all employees from voyage')

            print('m - Back to edit menu voyage\n')
            user_selection = input('Please choose one of the above: ').strip()
            
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
                    # user goes to add aircraft to voyage
                    VoyageUI().addAircraftToVoyage(self.voyage)
                    continue
            
            # add employees to voyage
            elif user_selection == '2':
                # if no aircraft is assigned
                if self.voyage.getAircraftID() == self.EMPTY:
                    print('-'*45+'\n')
                    print('No aircraft assigned to voyage')
                    print('Aircraft must me assigned before staff can be added')
                    print('\n'+'-'*45)

                else:
                    # go to add crew to voyage
                    return VoyageUI().addCrewToVoyage(self.voyage)
            
            # change number of sold seats out
            elif user_selection == '3':
                VoyageUI().changeSoldSeats(self.voyage,'out')
            
            # change number of sold seats home
            elif user_selection == '4':
                VoyageUI().changeSoldSeats(self.voyage,'home')

            elif user_selection == '5':
               VoyageUI().removeCrewFromVoyage(self.voyage)



            # go to edit menu
            elif user_selection == 'm':
                return
            
            # if none of the possibilities were chosen
            else:
                print('Invalid selection!')