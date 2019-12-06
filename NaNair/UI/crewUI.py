from API.LL_API import LL_API
import datetime

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
        self.printCrew(format_str)

    def showNotWorkingCrew(self,date_str):
        format_str = LL_API().get_not_working_crew(date_str)
        self.printCrew(format_str)

    def printCrew(self,format_str):
        if format_str != None:
            print('#'*30)
            print('{:^30}'.format('Working Crew'))
            print()
            print('#'*30)
            header_str = '{:<20}{:<20}{:<20}{:<20}{:<20}'.format('Name','Employee Id','Address','Phone Number','Destination')

            print(header_str)
            print(len(header_str)*'-')
            print(format_str)
            print()
        else:
            print('\nNo voyages on this day\n')

    def verifyDate(self,year_str,month_str,day_str):
        while True:
            try:
                year_int = int(year_str)
                month_int = int(month_str)
                day_int = int(day_str)
                
                date_tuple = self.checkIfDateValid(year_int,month_int,day_int)
                if date_tuple != None:
                    year_int,month_int,day_int = date_tuple
                    return year_int,month_int,day_int
                else:
                    print('Invalid date! Try again: ')
                    year_str = input('Year: ')
                    month_str = input('Month: ')
                    day_str = input('Day: ')

            except ValueError:
                print('Invalid date! Try again: ')
                year_str = input('Year: ')
                month_str = input('Month: ')
                day_str = input('Day: ')

    def checkIfDateValid(self,year_int,month_int,day_int):
        '''Checks if date is valid'''
        # Ath á kannski að vera eh year today? spyrja völu hún gerði þetta eh staðar
        if 0<year_int<=2020:
            if 0<month_int<=12:
                months_with_30_days = [1,3,5,7,8,10,12]
                if month_int in months_with_30_days:
                    if 0<day_int<=31:
                        return year_int,month_int,day_int
                    else:
                        return None
                elif month_int == 2:
                    if 0<day_int<=28:
                        return year_int,month_int,day_int
                    else:
                        return None
                else:
                    if 0<day_int<=30:
                        return year_int,month_int,day_int
                    else:
                        return None
            else:
                return None
        else:
            return None


    def changeEmployeeInfo(self,employee):
        LL_API().changeCrewInfo(employee)


    def changePilotLicense(self,crew_id,new_license):
        LL_API().changePilotLicense(crew_id,new_license)

            
    def showOneCrewMember(self,crew_id):
        crew_member = LL_API().get_crew_member_by_id(crew_id)
        print('-'*50)

        if crew_member == None:
            print('Employee with this id not found!')
            print()
            return False
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
            return True


    def showAllPilots(self):
        ''' Shows full list of pilots registered'''
        return LL_API().get_pilots()


    def showByLicense(self, license_ID):
        ''' Shows a list of pilots that have a specific licence '''

        licensed_pilots_list = LL_API().get_licensed_pilots(license_ID)

        print(self.BANNER_pilot)

        for pilot_instance in licensed_pilots_list:
            
            if pilot_instance.getCaptain():
                rank = 'Captain'
            else:
                rank = 'Copilot'

            print('{:<25}{:<20}{:<25}{:<10}'.format(pilot_instance.getName(), pilot_instance.getCrewID(), rank, pilot_instance.getLicense()))

        print()

    def showSortedByLicense(self):
        '''Shows a list of all pilots sorted by license'''

        sorted_pilots_list =  LL_API().sortPilotsByLicense()

        print(self.BANNER_pilot)
        
        for pilot in sorted_pilots_list:
            
            if pilot.getCaptain():
                rank = 'Captain'
            else:
                rank = 'Copilot'

            print('{:<25}{:<20}{:<25}{:<10}'.format(pilot.getName(), pilot.getCrewID(), rank, pilot.getLicense()))
    
        print()

    def showAllFlightAtt(self):
        ''' Shows a full list of all pilots registered''' 
        
        print(self.BANNER_att)

        flight_att = LL_API().get_flight_att()

        for attendant in flight_att:

            if attendant.getHeadFlightAtt():
                rank = 'Head service manager'
            else:
                rank = 'Flight attendant'

            print('{:<25}{:<20}{:<20}'.format(attendant.getName(), attendant.getCrewID(), rank ))
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
        
        print('Enter the "From date" for work schedule')
        
        start_year_str = input('Year: ')
        start_month_str = input('Month: ')
        start_day_str = input('Day: ')

        start_year_int, start_month_int, start_day_int = CrewUI().verifyDate(start_year_str, start_month_str, start_day_str)
        start_date = datetime.datetime(start_year_int,start_month_int,start_day_int,0,0,0).isoformat()
        
        print('Enter the "To date" for work schedule')
        end_year_str = input('Year: ')
        end_month_str = input('Month: ')
        end_day_str = input('Day: ')

        end_year_int, end_month_int, end_day_int = CrewUI().verifyDate(end_year_str, end_month_str, end_day_str)
        end_date = datetime.datetime(end_year_int,end_month_int,end_day_int,0,0,0).isoformat()
        
        work_schedule_list = LL_API().get_work_schedule(start_date,end_date,crew_ID)

        employee = LL_API().get_crew_member_by_id(crew_ID)
        #working_crew_list
        name_header_str = '{:<10} {:<10}'.format(employee.getName(),crew_ID)
        header_str = 'Working Schedule {}.{}.{}-{}.{}.{}'.format(start_day_int,start_month_int,start_year_int,end_day_int,end_month_int,end_year_int)
        print()
        print(name_header_str)
        print(header_str)
        print(len(header_str)*'-')
        if work_schedule_list != None: 
            for voyage in work_schedule_list:
                flight_no_out,flight_no_home = voyage.getFlightNumbers()
                voyage_duration_hrs, voyage_duration_min = LL_API().get_voyage_duration(voyage)
                aircraft_ID = voyage.getAircraftID()
                self.prettyprint(voyage,flight_no_out,flight_no_home,voyage_duration_hrs,voyage_duration_min,\
                aircraft_ID)
        else:
            print('No voyages on this time period\n')

            
    def prettyprint(self,voyage,flight_no_out,flight_no_home,voyage_duration_hrs,voyage_duration_min,\
        aircraft_ID):

        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(), voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))
        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))
        print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,voyage_duration_min))
        print('\t Aircraft: {}'.format(aircraft_ID))

