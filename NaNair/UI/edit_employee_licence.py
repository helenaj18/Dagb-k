from UI.crewUI import CrewUI
from API.LL_API import LL_API


class EditEmployeeLicense:

    def isPilotOnFutureVoyage(self,pilot):
        voyage_id_with_pilot = []
        upcoming_voyage_list = LL_API.get_upcoming_voyages()
        for voyage in upcoming_voyage_list:
            if pilot.getCrewID() in voyage.getCrewOnVoyage():
                voyage_id_with_pilot.append(voyage.getVoyageID)
                return voyage_id_with_pilot

            else:
                return voyage_id_with_pilot



    def startEditEmployeeLicense(self,employee):

        new_license = CrewUI().getPilotLicense()
        print()
        voyage_id_with_pilot = self.isPilotOnFutureVoyage()

        if len(voyage_id_with_pilot) != 0:
            print('Pilot is assigned to future voyages')
            print('You must assign another pilot to voyages:')
            for voyage_id in voyage_id_with_pilot:
                print(voyage_id)
            
        else:
            employee.setLicense(new_license)
    
        CrewUI().changeEmployeeInfo(employee)