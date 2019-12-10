from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI
from UI.change_employee_on_voyage_menu import ChangeEmployeeOnVoyage

class ChangeOneVoyageMenu:

    EMPTY = 'empty'

    def __init__(self,voyage):
        self.voyage = voyage

    def startChangeOneVoyageMenu(self):

        while True:
            print("\nWhat do you want to change in voyage {}?\n".format(self.voyage.getVoyageID()))

            # Change existing voyage
            print('1 - Add an airplane to a voyage')
            print('2 - Add employees to a voyage')
            print('3 - Change number of sold seats')
            print('4 - Change employees on voyage')

            print('m - Back to edit menu voyage\n')
            user_selection = input('Please choose one of the above (1/2/m): ').strip()
            
            if user_selection == '1':
                # Gets a list of all airplane insignias
                airplane_insignia_list = AirplaneUI().getAirplaneInsigniaList()
                
                # If an aircraft is assigned to the voyage 
                # the aircraft ID would be in the airplane insignia list
                if self.voyage.getAircraftID() in airplane_insignia_list:
                    print('Airplane already assigned to Voyage')
                    continue
                else:
                    VoyageUI().addAircraftToVoyage(self.voyage)
                    continue
            
            elif user_selection == '2':
                if self.voyage.getAircraftID() == self.EMPTY:
                    print('\nNo aircraft assigned to voyage')
                    print('Aircraft must me assigned before staff can be added\n')

                else:
                    return VoyageUI().addCrewToVoyage(self.voyage)
            
            elif user_selection == '3':
                pass

            elif user_selection == '4':
                ChangeEmployeeOnVoyage().startChangeEmployeeOnVoyage()

            elif user_selection == 'm':
                return
            
            else:
                print('Invalid selection')
                