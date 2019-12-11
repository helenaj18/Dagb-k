from API.LL_API import LL_API
import datetime
from ModelClasses.flight_att_model import FlightAttendant
from ModelClasses.pilot_model import Pilot
from UI.destinationUI import DestinationUI
import string

class CrewUI:

    pilot_header = '\n{:<25}{:<20}{:<25}{:10}\n'.format('Name','Employee ID','Position','License')
    pilot_header += '-'*85
    flight_att_header = '\n{:<25}{:<20}{:<25}\n'.format('Name','Employee ID','Position')
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
        self.printCrew(working_crew_list,True)


    def showNotWorkingCrew(self,date_str):
        datetime_object = LL_API().revertDatetimeStrtoDatetime(date_str)
        not_working_crew_list = LL_API().get_not_working_crew(datetime_object)
        self.printCrew(not_working_crew_list, False)

    

    def queryShowNotWorkingCrew(self):

        while True:
            print('Pick a staff member from the list above\n')
            print('1 - cancel and go back')
            
            crew_id = input('What staff member do you want to pick from the list above (Employee ID): ').lower().strip()
            if crew_id != '1':
                employee = LL_API().get_crew_member_by_id(crew_id)
                if employee != None:
                    return employee
                print('Employee not found, try again')
            else:
                return


    def showQualifiedCrew(self, depart_time_str, plane_insignia):
        '''Prints a list of crew that can be assigned to new voyage'''

        qualified_crew_list = LL_API().getQualifiedCrew(depart_time_str, plane_insignia)

        if qualified_crew_list != None:
            self.printCrew(qualified_crew_list, False)
        else:
            print('There are no non-working pilots qualified to fly this plane. Please pick another one.')
        

    def checkRank(self,crew_member):
        role = crew_member.getRole()
        if role == 'Pilot':
            if crew_member.getBool(): 
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
            print('\n'+'-'*45)
            print('{:^45}'.format(header))
            print()
            print('-'*45+'\n')
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
            print()
            print('{:^45}'.fomat('No voyages on this day!'))
            print('-'*45)


    def changeEmployeeInfo(self,employee):
        return LL_API().changeCrewInfo(employee)


    def changePilotLicense(self,crew_id,new_license):
        return LL_API().changePilotLicense(crew_id,new_license)

            
    def showOneCrewMember(self,crew_id):
        crew_member = LL_API().get_crew_member_by_id(crew_id)
        print('\n'+'-'*45)

        if crew_member == None:
            print('Employee with this id not found!')
            print()
            return False
        else:
            print('{:<15}{:<15}'.format('Name:',crew_member.getName()))
            print('{:<15}{:<15}'.format('SSN:',crew_member.getCrewID()))
            print('{:<15}{:<15}'.format('Address:',crew_member.getAddress()))
            print('{:<15}{:<15}'.format('Phone number:',crew_member.getPhoneNumber()))
            print('{:<15}{:<15}'.format('Email:',crew_member.getEmail()))

            if type(crew_member) == Pilot:
                if crew_member.getBool():
                    print('{:<15}{:<15}'.format('Rank:','Captain'))
                    print('{:<15}{:<15}'.format('License:',crew_member.getLicense()))
                else:
                    print('{:<15}{:<15}'.format('Rank:','Co-pilot'))
                    print('{:<15}{:<15}'.format('License:',crew_member.getLicense()))
            else:
                if crew_member.getBool():
                    print('{:<15}{:<15}'.format('Rank:','Head service manager'))
                else:
                    print('{:<15}{:<15}'.format('Rank:','Flight attendant'))

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
        print()
        print('-'*45)
        print('{:^45}'.format('Please fill in the following information.'))
        print('{:^45}'.format('Press enter to skip.'))
        print('-'*45)
        print()

        personal_id = self.getPersonalID()
        if personal_id:
            while LL_API().doesIDExist(personal_id):

                print('{:^45}'.format('Another crew member already has that ID!'))
                print('{:^45}'.format('Please input another ID.'))
                print('-'*45)
                print()
            
                personal_id = self.getPersonalID()

            info_list.append(personal_id)


            employee_name = self.getName()
            info_list.append(employee_name)

            print()
            print('-'*45)
            print('{:^45}'.format('Please choose one of the following'))
            print('{:^45}'.format('job titles:'))
            print('-'*45)
            print()
            print('1 - Captain')
            print('2 - Co-pilot')
            print('3 - Head service manager')
            print('4 - Flight attendant')
            print('m - Back to main menu')
            rank = input('\nPlease choose a number between 1-4 or m: ').strip()

            while rank != '1' and rank != '2' and rank != '3' and rank != '4' and rank != 'm':
                rank = input('Please choose a number between 1-4 or m: ').strip()
                    
            info_list.append(rank)
        print()
        print('-'*45)
        print('{:^45}'.format('Please choose one of the following'))
        print('{:^45}'.format('job titles:'))
        print('-'*45)
        print()
        print('1 - Captain')
        print('2 - Co-pilot')
        print('3 - Head service manager')
        print('4 - Flight attendant')
        print('m - Back to main menu')
        rank = input('\nPlease choose a number between: ').strip()

        while rank != '1' and rank != '2' and rank != '3' and rank != '4' and rank != 'm':
            rank = input('Please choose a number between: ').strip()
                
        info_list.append(rank)

        if rank == '1' or rank == '2':
            pilot_license = self.getPilotLicense()
            info_list.append(pilot_license)
        elif rank == 'm':
            return

            if rank == '1' or rank == '2':
                pilot_license = self.getPilotLicense()
                info_list.append(pilot_license)
            elif rank == 'm':
                return


            home_address = self.getHomeAddress()
            info_list.append(home_address)

            phone_number = self.getPhoneNumber()
            info_list.append(phone_number)

            email_address = self.getEmail()
            info_list.append(email_address)

            LL_API().addCrew(info_list)

            #info_list for pilots is longer because of license
            print()
            print('~'*45)
            print('{:^45}'.format('New Employee added!')) 
            print('~'*45)
        
            return

        else:
            return
        
    def getHomeAddress(self):
        '''Gets home address of an 
           employee from user'''
           
        digits_list = []

        while True:
            home_address = input('Home address: ').strip()
            for letter in home_address:
                if letter in string.punctuation:
                    print('Invalid home address!')
                    break
                elif letter.isdigit():
                    digits_list.append(letter)
            else:
                if len(digits_list) != 0 and len(digits_list) == len(home_address):
                    print('Invalid home address!')
                    continue
                else:
                    if home_address != '':
                        return home_address
                    else:
                        return 'empty'

    def getPilotLicense(self):
        '''Gets pilot license from user '''
        success = False
        airplane_types = LL_API().loadAirplaneTypes()

        print('-'*45)
        print('{:^45}'.format('Please chose one of the following'))
        print('{:^45}'.format('pilot licenses:'))
        print('-'*45)
        print()
        
        while True:
            counter = 1
            for airplane_type in airplane_types:
                print('{} - {}'.format(counter,airplane_type))
                counter += 1

            selection = input('\nPlease choose one of the above: ').strip()

            for i in range(1,counter+1):
                if selection == str(i):
                    pilot_license = airplane_types[i-1].getplaneTypeID()
                    success = True
                    return pilot_license

            if not success:
                print('\nInvalid selection!\n')


    def getPhoneNumber(self):
        '''Gets the employee's phone 
           number from user'''
        while True:
            employee_phone_number = input("Enter the employee's phone number: ").strip()
            if len(employee_phone_number) !=0 and DestinationUI().checkIfInt(employee_phone_number):
                if len(employee_phone_number) == 7:
                    return employee_phone_number
                else:
                    print('\nInvalid phone number!\n')
            elif len(employee_phone_number) == 0:
                return 'empty'
            else:
                print('\nInvalid phone number!\n')


    def getEmail(self):
        '''Gets the employee's email address'''
        while True:
            email_address = input('Email: ').strip()
            if len(email_address) == 0:
                return 'empty'
            elif '@' and '.' in email_address and len(email_address) != 0:
                return email_address
            else:
                print('\nInvalid email address!\n')

    def getName(self):
        while True:
            employee_name = input("Enter the employee's name: ").capitalize().strip()
            for letter in employee_name:
                if letter.isdigit():
                    print('\nInvalid name, please enter only letters!\n')
                    break
            else:
                if len(employee_name) != 0:
                    return employee_name
                else:
                    print('\nThe name is required!\n')


    def getPersonalID(self):
        '''Gets personal ID from user'''

        while True:
            print('\nInput personal ID of emlployee(SSN - 10 digits, no hyphen)')
            print('m - Back to main menu')
            personal_id = input('Input your choice: ').strip()
            if personal_id != 'm':
                if DestinationUI().checkIfInt(personal_id):
                    if len(personal_id) == 10:
                        return personal_id
                    else:
                        print('\nInvalid personal ID!\n')
                else:
                    print('\nInvalid personal ID!\n')
            else:
                return 
           

    def getDateInput(self,a_string):
        b_str = 'Enter the {} date for the period'.format(a_string)
        print('\n'+'-'*45)
        print('{:^45}'.format(b_str))
        print('{:^45}'.format('on work schedule'))
        print('-'*45+'\n')
        
        year_str = input('Year: ').strip()
        month_str = input('Month: ').strip()
        day_str = input('Day: ').strip()

        return year_str,month_str,day_str


    def showSchedule(self, crew_ID):
        ''' Shows the schedule for a specific crew member '''
        employee = LL_API().get_crew_member_by_id(crew_ID)
        
        if employee != None:
        
            
            start_year_str,start_month_str,start_day_str = self.getDateInput('start')
            

            start_year_int, start_month_int, start_day_int = LL_API().verifyDate(start_year_str, start_month_str, start_day_str)
            start_date = datetime.datetime(start_year_int,start_month_int,start_day_int,0,0,0) #VERIFY INPUT
            
            end_year_str,end_month_str,end_day_str = self.getDateInput('end')

            end_year_int, end_month_int, end_day_int = LL_API().verifyDate(end_year_str, end_month_str, end_day_str)
            end_date = datetime.datetime(end_year_int,end_month_int,end_day_int,0,0,0) # VERIFY INPUT
            
            work_schedule_list = LL_API().get_work_schedule(start_date,end_date,crew_ID)
            
        
            name_header_str = '{:^45}\n{:^45}'.format(employee.getName(),'ID:'+crew_ID)
            date_str = '{}.{}.{}-{}.{}.{}'.format(\
                start_day_int,start_month_int,start_year_int,end_day_int,end_month_int,end_year_int)
            header_str = '{:^45}\n{:^45}'.format('Working Schedule',date_str)

            
            print('\n'+'-'*45)
            print(name_header_str)
            print(header_str)
            print(45*'-'+'\n')

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

    #def prettyprintScheduleHeader(self)
            
    def prettyprint(self,voyage,flight_no_out,flight_no_home,voyage_duration_hrs,voyage_duration_min,\
        aircraft_ID):

        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(), voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))
        print(45*'-')
        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))
        print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,voyage_duration_min))
        print('\t Aircraft: {}'.format(aircraft_ID))
        print()

