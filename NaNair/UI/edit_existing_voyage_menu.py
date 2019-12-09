from UI.voyageUI import VoyageUI
from UI.airplaneUI import AirplaneUI
from UI.crewUI import CrewUI
from API.LL_API import LL_API

class EditExistingVoyage:
    EMPTY = 'empty'

    def startEditExistingVoyage(self):
        print()
        print('1 - Enter voyage ID')
        print('2 - See a list of voyages on a specific time range')
        print()
        selection = input()

        if selection == '1':
            voyage_id = input('Enter voyage ID: ')
            voyage = LL_API().getOneVoyage(voyage_id)
            
            if voyage != None:
                VoyageUI().showOneVoyage(voyage)
        
        elif selection == '2':
            print("Select date range to find a voyage to edit")
            voyage = VoyageUI().queryOneVoyage()
            if voyage != None:
                VoyageUI().showOneVoyage(voyage)
        else:
            print('Invalid selection!')
            selection = input()


        while True:
            print("\nWhat do you want to change in voyage {}?".format(voyage.getVoyageID()))
            # Change existing voyage
            print('1 - Add an airplane to a voyage')
            print('2 - Add employees to a voyage')
            print('m - Back to edit menu')
            user_selection = input('Please choose one of the above (1 or 2): ')
            
            if user_selection == '1':
                airplane_insignia_list = AirplaneUI().getAirplaneInsigniaList()
                if voyage.getAircraftID() in airplane_insignia_list:
                    print('Airplane already assigned to Voyage')
                    continue
                else:
                    VoyageUI().addAircraftToVoyage(voyage)
                    continue
            
            elif user_selection == '2':
                if voyage.getAircraftID() == self.EMPTY:
                    print()
                    print('No aircraft assigned to voyage')
                    print('Aircraft must me assigned before staff can be added')
                    print() 

                else:
                    
                    insignia = voyage.getAircraftID()
                    CrewUI().showQualifiedCrew(voyage.getDepartureTime(), insignia)
                    print()

                    return VoyageUI().addCrewToVoyage(voyage)
            
            elif user_selection == 'm':
                return
            
            else:
                print('Invalid selection')