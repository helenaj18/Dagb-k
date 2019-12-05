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
    

    def showWorkingCrew(self,date_str):
        format_str = LL_API().get_working_crew(date_str)
        print('#'*30)
        print('{:^30}'.format('Working Crew'))
        print()
        print('#'*30)
        header_str = '{:<20}{:<20}{:<20}{:<20}{:<20}'.format('Name','Employee Id','Address','Phone Number','Destination')

        print(header_str)
        print(len(header_str)*'-')
        print(format_str)
        print()

<<<<<<< HEAD
    def showNotWorkingCrew(self,date):
        pass

    def changeEmployeeInfo(self):
        
=======
    def showNotWorkingCrew(self,date_str):
        format_str = LL_API().get_not_working_crew(date_str)
        print('#'*30)
        print('{:^30}'.format('Not Working Crew'))
        print('#'*30)
        print()
        header_str = '{:<20}{:<20}{:<20}{:<20}'.format('Name','Employee Id','Address','Phone Number')

        print(header_str)
        print(len(header_str)*'-')
        print(format_str)
        print()
>>>>>>> 299e9535101d9377ee388c1c2148af25cc53ae03
        
    def showOneCrewMember(self,crew_id):
        crew_member = LL_API().get_crew_member_by_id(crew_id)
        print('-'*50)

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

    def addCrew(self):
        info_list = []
        print('Please fill in the following information. Press enter to skip.\n')

        info_list.append(input('Personal ID (required): '))
        info_list.append(input('Name (required): '))

        print('Please choose one of the following job titles:')
        print('1 - Captain')
        print('2 - Co-pilot')
        print('3 - Head service manager')
        print('4 - Flight attendant')
        rank = input()
        while rank != '1' and rank != '2' and rank != '3' and rank != '4':
            print('Please choose a number between 1-4')
            rank = input()
                
        info_list.append(rank)

        if rank == '1' or rank =='2':
            info_list.append( input('Pilot license: ') )

        info_list.append( input('Home address: ') )
        info_list.append( input('Phone number: ') )
        info_list.append( input('Email: ') )

        LL_API().addCrew(info_list)

        #info_list for pilots is longer because of license

        print('New Employee added!\n') 
        

    # bíða með þar til crew er skráð á ákv vinnuferðir
    def showSchedule(self, crew_ID):
        ''' Shows the schedule for a specific crew member '''
        pass

