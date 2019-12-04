from API.LL_API import LL_API

class CrewUI:

    def __init__(self):
        self.BANNER = '{:<25}{:<20}{:<20}{:<10}\n'.format('Name', 'Pilot ID','License', 'Rank')
        self.BANNER += '_'*80
    def __str__(self):
        pass 
    
    def showCrew(self):
        '''' Shows full list of crew, pilots and flight attendants'''
        crew = LL_API().get_crew()
        return crew

    def showWorkingCrew(self):
        ''' Shows full list of working crew atm '''        
        return LL_API().get_working_crew()

    def showAllPilots(self):
        ''' Shows full list of pilots registered'''
        return LL_API().get_pilots()

    def showOnePilot(self, pilot_ID):
        ''' Shows details for a specific pilot'''
        
        pilot = LL_API().get_pilot_by_id(pilot_ID)
        print(pilot)

    def showByLicence(self, license_ID):
        ''' Shows a list of pilots that have a specific licence '''

        licensed_pilots_list = LL_API().get_licensed_pilots(license_ID)

        print(self.BANNER)

        for pilot_instance in licensed_pilots_list:
                print(pilot_instance)


    def showSortedByLicense(self):
        '''Shows a list of all pilots sorted by license'''

        sorted_pilots_list =  LL_API().sortPilotsByLicense()

        print(self.BANNER)
        
        for pilot in sorted_pilots_list:
            print(pilot)
    
        print()




    def showAllFlightAtt(self):
        ''' Shows a full list of all pilots registered''' 
        
        return LL_API().get_flight_att()
  
    def showOneFlightAtt(self, flight_att_ID):
        ''' Shows details for a specific flight attendant'''
        
        return LL_API().flight_att_by_id(flight_att_ID)

    # bíða með þar til crew er skráð á ákv vinnuferðir
    def showSchedule(self, crew_ID):
        ''' Shows the schedule for a specific crew member '''
        pass

