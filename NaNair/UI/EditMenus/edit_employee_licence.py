from UI.crewUI import CrewUI
from API.LL_API import LL_API


class EditEmployeeLicense:
    '''Class to edit pilot license'''
   
    def isPilotOnFutureVoyage(self,pilot):
        '''Checks if pilot instance is working on other voyages in the future. If he is, 
        a list of the IDs for the voyages he is working on is returned.'''
        voyage_id_with_pilot = []
        
        # all future voyages
        upcoming_voyage_list = LL_API().get_upcoming_voyages()
        for voyage in upcoming_voyage_list:
            if pilot.getCrewID() in voyage.getCrewOnVoyage(): # if pilot is assigned to a voyage
                voyage_id_with_pilot.append(voyage.getVoyageID())

        return voyage_id_with_pilot



    def startEditEmployeeLicense(self,employee):
        '''Changes pilot license.'''
        
        old_license = employee.getLicense()
        new_license = CrewUI().getPilotLicense()
        print()
        # list of voyages employee is already assigned to
        voyage_id_with_pilot = self.isPilotOnFutureVoyage(employee)

        # if pilot is working on future voyages with old license
        if len(voyage_id_with_pilot) != 0:
            print('Pilot is assigned to future voyages')
            print('You must assign another pilot to voyages:')
            for voyage_id in voyage_id_with_pilot:
                print(voyage_id)
        
        # if pilot is not working on any voyages in the future
        else:
            employee.setLicense(new_license)
    
            CrewUI().changeEmployeeInfo(employee)

            print('License for {} has been changed from {} to {}'\
                .format(employee.getName(),old_license,new_license))