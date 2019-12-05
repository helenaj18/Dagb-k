from API.LL_API import LL_API

class CrewUI:

    def __init__(self):
        self.BANNER_pilot = '{:<25}{:<20}{:<20}{:<10}\n'.format('Name', 'Pilot ID', 'Rank', 'License')
        self.BANNER_pilot += '_'*80
        self.BANNER_att = '{:<25}{:<20}{:<20}\n'.format('Name', 'Flight Att. ID', 'Rank')
        self.BANNER_att += '_'*80
        self.BANNER_crew = '{:<25}{:<20}{:<25}{:<20}\n'.format('Name','Crew Member ID','Rank','License')
        self.BANNER_crew += '_'*85
    def __str__(self):
        pass 
    
    def showCrew(self):
        '''' Shows full list of crew, pilots and flight attendants'''
        crew = LL_API().get_crew()

        print(self.BANNER_pilot)

        for employee in crew:
            print(employee)
        print()
    
    def showWorkingCrew(self,date):
        pass

    def showNotWorkingCrew(self,date):
        pass
        
    def showOneCrewMember(self,crew_id):
        print(self.BANNER_crew)
        crew_member = LL_API().get_crew_member_by_id(crew_id)
        print(crew_member)
        print()

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
        print()

    def showByLicence(self, license_ID):
        ''' Shows a list of pilots that have a specific licence '''

        licensed_pilots_list = LL_API().get_licensed_pilots(license_ID)

        print(self.BANNER_pilot)

        for pilot_instance in licensed_pilots_list:
                print(pilot_instance)

        print()

    def showSortedByLicense(self):
        '''Shows a list of all pilots sorted by license'''

        sorted_pilots_list =  LL_API().sortPilotsByLicense()

        print(self.BANNER_pilot)
        
        for pilot in sorted_pilots_list:
            print(pilot)
    
        print()

    def showAllFlightAtt(self):
        ''' Shows a full list of all pilots registered''' 
        
        print(self.BANNER_att)

        flight_att = LL_API().get_flight_att()

        for attendant in flight_att:
            print(attendant)
        print()
  
    def showOneFlightAtt(self, flight_att_ID):
        ''' Shows details for a specific flight attendant'''
        flight_att = LL_API().flight_att_by_id(flight_att_ID)
        print(flight_att)
        print()
        

    # bíða með þar til crew er skráð á ákv vinnuferðir
    def showSchedule(self, crew_ID):
        ''' Shows the schedule for a specific crew member '''
        pass

