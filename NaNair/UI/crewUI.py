from API.LL_API import LL_API

class CrewUI:

    def __init__(self):
        self.BANNER_pilot = '{:<25}{:<20}{:<25}{:<10}\n'.format('Name', 'Pilot ID', 'Rank', 'License')
        self.BANNER_pilot += '_'*80
        self.BANNER_att = '{:<25}{:<20}{:<20}\n'.format('Name', 'Flight Att. ID', 'Rank')
        self.BANNER_att += '_'*80
        self.BANNER_crew = '{:<25}{:<20}{:<25}{:<20}\n'.format('Name','Crew Member ID','Rank','License')
        self.BANNER_crew += '_'*80
    def __str__(self):
        pass 
    
    def showCrew(self):
        '''' Shows full list of crew, pilots and flight attendants'''
        crew = LL_API().get_crew()
        string = ''

        print(self.BANNER_pilot)

        for employee in crew:
            string = '{:<25}{:<20}'.format(employee.getName(),employee.getCrewID())

            try:
                if employee.getCaptain():
                    string += '{:<25}{:<10}'.format('Captain', employee.getLicense())
                else:
                    string += '{:<25}{:<10}'.format('Co-pilot', employee.getLicense())
            except AttributeError:
                if employee.getHeadFlightAtt():
                    string += '{:<15}'.format('Head service manager')
                else:
                    string += '{:<15}'.format('Flight attendant')
            
            print(string)

        print()
    

    def showWorkingCrew(self,date):
        working_crew_list = LL_API().get_working_crew(date)
        header_str = '{:<20}{:<20}{:<20}{:<20}{:<20}'.format('Name','Id','Address','Phone Number','Destination')
        print(header_str)
        print(len(header_str)*'-')

        for working_crew_per_voyage in working_crew_list:
            destination = working_crew_per_voyage[1]
            for crew_id in working_crew_per_voyage[0]:
                if crew_id != 'empty':
                    crew_member = LL_API().get_crew_member_by_id(crew_id)
                    crew_name = crew_member.getName()
                    crew_address = crew_member.getAddress()
                    crew_phone = crew_member.getPhoneNumber()
                    format_str = '{:<20}{:<20}{:<20}{:<20}{:<20}'.format(crew_name,crew_id,crew_address,crew_phone,destination)
                    print(format_str)


    def showNotWorkingCrew(self,date):
        pass
        
    def showOneCrewMember(self,crew_id):
        crew_member = LL_API().get_crew_member_by_id(crew_id)

        if crew_member == None:
            print('Employee with this id not found!')
            print()
        else:
            print('Name: {}'.format(crew_member.getName()))
            print('SSN: {}'.format(crew_member.getCrewID()))
            print('Address: {}'.format(crew_member.getAddress()))
            print('Phone number: {}'.format(crew_member.getPhoneNumber()))
            print('Email: {}'.format(crew_member.getEmail()))
            
            try:
                if crew_member.getCaptain():
                    print('Rank: Captain')
                else:
                    print('Rank: Co-pilot')
                print('License: {}'.format(crew_member.getLicense()))
            except:
                if crew_member.getHeadFlightAtt():
                    print('Rank: Head service manager')
                else:
                    print('Rank: Flight attendant')

            print()


    def showAllPilots(self):
        ''' Shows full list of pilots registered'''
        return LL_API().get_pilots()

    # def showOnePilot(self, pilot_ID):
    #     ''' Shows details for a specific pilot'''
        
    #     pilot = LL_API().get_pilot_by_id(pilot_ID)
        
    #     print()
    #     print('Name: {}'.format(pilot.getName()))
    #     print('SSN: {}'.format(pilot.getCrewID()))
    #     print('Address: {}'.format(pilot.getAddress()))
    #     print('Phone number: {}'.format(pilot.getPhoneNumber()))
    #     print('Email: {}'.format(pilot.getEmail()))
    #     if pilot.getCaptain():
    #         print('Rank: Captain')
    #     else:
    #         print('Rank: Co-pilot')
    #     print()

    def showByLicense(self, license_ID):
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
  
    # def showOneFlightAtt(self, flight_att_ID):
    #     ''' Shows details for a specific flight attendant'''
    #     flight_att = LL_API().flight_att_by_id(flight_att_ID)
        
    #     print()
    #     print('Name: {}'.format(flight_att.getName()))
    #     print('SSN: {}'.format(flight_att.getCrewID()))
    #     print('Address: {}'.format(flight_att.getAddress()))
    #     print('Phone number: {}'.format(flight_att.getPhoneNumber()))
    #     print('Email: {}'.format(flight_att.getEmail()))
    #     if flight_att.getHeadFlightAtt():
    #         print('Rank: Head Service Manager')
    #     else:
    #         print('Rank: Flight Attendant')
    #     print()
        

    # bíða með þar til crew er skráð á ákv vinnuferðir
    def showSchedule(self, crew_ID):
        ''' Shows the schedule for a specific crew member '''
        pass

