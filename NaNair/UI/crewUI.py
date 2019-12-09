from API.LL_API import LL_API
import datetime
from ModelClasses.flight_att_model import FlightAttendant
from ModelClasses.pilot_model import Pilot
from UI.destinationUI import DestinationUI


class CrewUI:

    pilot_header = '{:<25}{:<20}{:<25}{:10}\n'.format('Name','Employee ID','Position','License')
    pilot_header += '-'*85
    flight_att_header = '{:<25}{:<20}{:<25}\n'.format('Name','Employee ID','Position')
    flight_att_header += '-'*70

    def showCrew(self):
        '''' Shows full list of crew, pilots and flight attendants'''
        crew = LL_API().get_crew()
        string = ''
        
        print(CrewUI.pilot_header)

        for employee in crew:
            string = '{:<25}{:<20}'.format(employee.getName(),employee.getCrewID())

            if type(employee) == Pilot:
                if employee.getBool():
                    string += '{:<25}{:<10}'.format('Captain', employee.getLicense())
                else:
                    string += '{:<25}{:<10}'.format('Co-pilot', employee.getLicense())
            else:
                if employee.getBool():
                    string += '{:<15}'.format('Head service manager')
                else:
                    string += '{:<15}'.format('Flight attendant')
            
            print(string)

        print()


    def showWorkingCrew(self,date_str):
        datetime_object = LL_API().revertDatetimeStrtoDatetime(date_str)
        working_crew_list = LL_API().get_working_crew(datetime_object)
        print(working_crew_list)
        self.printCrew(working_crew_list,True)


    def showNotWorkingCrew(self,date_str):
        datetime_object = LL_API().revertDatetimeStrtoDatetime(date_str)
        not_working_crew_list = LL_API().get_not_working_crew(datetime_object)
        self.printCrew(not_working_crew_list, False)

    

    def queryShowNotWorkingCrew(self):

        while True:
            print('What staff member do you want to pick from the list above (Employee ID): ')
            crew_id = input().lower()

            employee = LL_API().get_crew_member_by_id(crew_id)
            if employee != None:
                return employee
            print('Employee not found, try again')

    def showQualifiedCrew(self, depart_time_str, plane_insignia):
        '''Prints a list of crew that can be assigned to new voyage'''

        qualified_crew_list = LL_API().getQualifiedCrew(depart_time_str, plane_insignia)

<<<<<<< HEAD
        self.printCrew(qualified_crew_list, False)
=======
        if qualified_crew_list != None:
            self.printCrew(qualified_crew_list, False)
        else:
            print('There are no non-working pilots qualified to fly this plane. Please pick another one.')
>>>>>>> d43b89865e5b619f3f9287adc1dffd950abe65b7
        

    def checkRank(self,crew_member):
        role = crew_member.getRole()
        if role == 'Pilot':
            if crew_member.getCaptain(): 
                position = 'Captain'
            else: 
                position = 'Pilot'
        elif role == 'Cabincrew':
            if crew_member.getBool(): 
                position = 'Head'
            else: 
                position = 'Flight Att.'
        return position
        

    def printCrew(self,crew_list, not_working):
        ''' Prints Crew'''
        header = 'Working Crew' if not_working else 'Not Working crew'
        format_str = ''

        if crew_list != None:
            print('#'*30)
            print('{:^30}'.format(header))
            print()
            print('#'*30)
            if header == 'Working Crew':
                header_str = '{:<15}{:<20}{:<15}{:<15}{:<25}{:<15}{:<20}{:<15}'.format(
                    'Role','Name','Employee Id','Position','Email',\
                        'Phone Number','Destination','License')
                for crew_member_info in crew_list:
                    crew_member = crew_member_info[0]
                    destination = crew_member_info[1]

                    position = self.checkRank(crew_member)

                    if crew_member.getRole() == 'Cabincrew':
                        crew_license = 'N/A'
                    else:
                        crew_license = crew_member.getLicense()

                    format_str += '{:<15}{:<20}{:<15}{:<15}{:<25}{:<15}{:<20}{:<15}\n'.format(
                    crew_member.getRole(),
                    crew_member.getName(),
                    crew_member.getCrewID(),
                    position,
                    crew_member.getEmail(),
                    crew_member.getPhoneNumber(),
                    destination,
                    crew_license
                )

            else:
                header_str = '{:<15}{:<20}{:<15}{:<15}{:<25}{:<20}{:<15}'.format(
                    'Role','Name','Employee Id','Position','Email',\
                        'Phone Number','License')

                for crew_member in crew_list:

                    if crew_member.getRole() == 'Cabincrew':
                        crew_license = 'N/A'
                    else:
                        crew_license = crew_member.getLicense()

                    position = self.checkRank(crew_member)
                    format_str += '{:<15}{:<20}{:<15}{:<15}{:<25}{:<20}{:<15}\n'.format(
                    crew_member.getRole(),
                    crew_member.getName(),
                    crew_member.getCrewID(),
                    position,
                    crew_member.getEmail(),
                    crew_member.getPhoneNumber(),
                    crew_license
                )

            print(header_str)
            print(len(header_str)*'-')
            print(format_str)


            print()
        else:
            print('\nNo voyages on this day\n')


    def changeEmployeeInfo(self,employee):
        return LL_API().changeCrewInfo(employee)


    def changePilotLicense(self,crew_id,new_license):
        return LL_API().changePilotLicense(crew_id,new_license)

            
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

            if type(crew_member) == Pilot:
                if crew_member.getBool():
                    print('Rank: Captain')
                    print('License: {}'.format(crew_member.getLicense()))
                else:
                    print('Rank: Co-pilot')
                    print('License: {}'.format(crew_member.getLicense()))
            else:
                if crew_member.getBool():
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

        print(CrewUI.pilot_header)

        for pilot_instance in licensed_pilots_list:
            
            if pilot_instance.getBool():
                rank = 'Captain'
            else:
                rank = 'Copilot'

            print('{:<25}{:<20}{:<25}{:<10}'.format(pilot_instance.getName(), pilot_instance.getCrewID(), rank, pilot_instance.getLicense()))

        print()

    def showSortedByLicense(self):
        '''Shows a list of all pilots sorted by license'''

        sorted_pilots_list =  LL_API().sortPilotsByLicense()

        print(CrewUI.pilot_header)
        
        for pilot in sorted_pilots_list:
            
            if pilot.getBool():
                rank = 'Captain'
            else:
                rank = 'Copilot'

            print('{:<25}{:<20}{:<25}{:<10}'.format(pilot.getName(), pilot.getCrewID(), rank, pilot.getLicense()))
    
        print()

    def showAllFlightAtt(self):
        ''' Shows a full list of all pilots registered''' 
        
        print(CrewUI.flight_att_header)

        flight_att = LL_API().get_flight_att()

        for attendant in flight_att:

            if attendant.getBool():
                rank = 'Head service manager'
            else:
                rank = 'Flight attendant'

            print('{:<25}{:<20}{:<20}'.format(attendant.getName(), attendant.getCrewID(), rank ))
        print()

    def addCrew(self):
        '''Gets information about a new 
           crew member and adds it to the
           crew file'''

        info_list = []
        print('Please fill in the following information. Press enter to skip.\n')

        personal_id = self.getPersonalID()
        info_list.append(personal_id)

        employee_name = self.getName()
        info_list.append(employee_name)

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

        if rank == '1' or rank == '2':
            pilot_license = self.getPilotLicense()
            info_list.append(pilot_license)


        home_address = self.getHomeAddress()
        info_list.append(home_address)

        phone_number = self.getPhoneNumber()
        info_list.append(phone_number)

        email_address = self.getEmail()
        info_list.append(email_address)

        LL_API().addCrew(info_list)

        #info_list for pilots is longer because of license

        print('\nNew Employee added!\n') 

        return
    
    def getHomeAddress(self):
        '''Gets home address of an 
           employee from user'''

        home_address = input('Home address: ')
        if home_address != '':
            return home_address
        else:
            return 'empty'

    def getPilotLicense(self):
        print('Pilot license:')
        print('1 - NAFokkerF100')
        print('2 - NAFokkerF28')
        print('3 - NABAE146')

        while True:
            pilot_license = input('Please choose one of the above: ')

            if pilot_license == '1':
                pilot_license = 'NAFokkerF100'
                return pilot_license
            elif pilot_license == '2':
                pilot_license = 'NAFokkerF28'
                return pilot_license
            elif pilot_license == '3':
                pilot_license = 'NABAE146'
                return pilot_license
            else:
                print('Invalid selection')


    def getPhoneNumber(self):
        '''Gets the employee's phone 
           number from user'''
        while True:
            employee_phone_number = input("Enter the employee's phone number: ")
            if len(employee_phone_number) !=0 and DestinationUI().checkIfInt(employee_phone_number):
                if len(employee_phone_number) == 7:
                    return employee_phone_number
                else:
                    print('Invalid phone number')
            elif len(employee_phone_number) == 0:
                return 'empty'
            else:
                print('Invalid phone number')


    def getEmail(self):
        '''Gets the employee's email address'''
        while True:
            email_address = input('Email: ')
            if len(email_address) == 0:
                return 'empty'
            elif '@' and '.' in email_address and len(email_address) != 0:
                return email_address
            else:
                print('Invalid email address!')

    def getName(self):
        while True:
            employee_name = input("Enter the employee's name: ").capitalize()
            for letter in employee_name:
                if letter.isdigit():
                    print('Invalid name, please enter only letters!')
                    break
            else:
                if len(employee_name) != 0:
                    return employee_name
                else:
                    print('The name is required')


    def getPersonalID(self):
        '''Gets personal ID from user'''

        while True:
            personal_id = input('Personal ID (required): ')

            if DestinationUI().checkIfInt(personal_id):
                if len(personal_id) == 10:
                    return personal_id
                else:
                    print('Invalid personal ID!')
            else:
                print('Invalid personal ID!')

    def showSchedule(self, crew_ID):
        ''' Shows the schedule for a specific crew member '''
        employee = LL_API().get_crew_member_by_id(crew_ID)
        
        if employee != None:
            print('Enter the "From date" for the work schedule')
            
            start_year_str = input('Year: ')
            start_month_str = input('Month: ')
            start_day_str = input('Day: ')

            start_year_int, start_month_int, start_day_int = LL_API().verifyDate(start_year_str, start_month_str, start_day_str)
            start_date = datetime.datetime(start_year_int,start_month_int,start_day_int,0,0,0)
            
            print('Enter the "To date" for work schedule')
            end_year_str = input('Year: ')
            end_month_str = input('Month: ')
            end_day_str = input('Day: ')

            end_year_int, end_month_int, end_day_int = LL_API().verifyDate(end_year_str, end_month_str, end_day_str)
            end_date = datetime.datetime(end_year_int,end_month_int,end_day_int,0,0,0)
            
            work_schedule_list = LL_API().get_work_schedule(start_date,end_date,crew_ID)
            
        
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
                return True
            else:
                print('No voyages in this time period\n')
                return True
        else:
            return False
            
    def prettyprint(self,voyage,flight_no_out,flight_no_home,voyage_duration_hrs,voyage_duration_min,\
        aircraft_ID):

        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(), voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))
        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))
        print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,voyage_duration_min))
        print('\t Aircraft: {}'.format(aircraft_ID))

