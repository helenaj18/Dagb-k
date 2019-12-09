from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI
from UI.crewUI import CrewUI

class EditExistingVoyage:
    EMPTY = 'empty'

    def startEditExistingVoyage(self):
        print("Select date range to find a voyage to edit")
        voyage = VoyageUI().queryOneVoyage()
        if voyage != None:
            VoyageUI().showOneVoyage(voyage)

            while True:
                print("\nWhat do you want to change in voyage {}".format(voyage.getVoyageID()))
                # Change existing voyage
                print('1 - Add an airplane to a voyage')
                print('2 - Add employees to a voyage')
                print('m - Back to edit menu')
                user_selection = input('Please choose one of the above (1/2/m): ')
                
                if user_selection == '1':
                    airplane_insignia_list = AirplaneUI().getAirplaneInsigniaList()
                    if voyage.getAircraftID() in airplane_insignia_list:
                        print('\nAirplane already assigned to Voyage\n')
                        continue
                    else:
                        VoyageUI().addAircraftToVoyage(voyage)
                        print('Aircraft successfully added!')
                        continue 
                
                elif user_selection == '2':
                    if voyage.getAircraftID() == self.EMPTY:

                        print()
                        print('No aircraft assigned to voyage')
                        print('Aircraft must me assigned before staff can be added')
                        print() 
                    

                    else:

                        #crew_on_voyage_list = voyage.getCrewOnVoyage()
                        insignia = voyage.getAircraftID()
                        CrewUI().showQualifiedCrew(voyage.getDepartureTime(), insignia)
                        print()

                        return VoyageUI().addCrewToVoyage(voyage)
                
                elif user_selection == 'm':
                    return
                
                else:
                    print('Invalid selection')