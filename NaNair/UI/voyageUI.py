from API.LL_API import LL_API
import datetime
from UI.airplaneUI import AirplaneUI
from UI.crewUI import CrewUI
from UI.EditMenus.extra_crewmember_menu import AddExtraCrewmemberMenu
import datetime


class VoyageUI:
    EMPTY = 'empty'
    SEPERATOR = '-'

    def getDateInput(self):
        '''Gets a date input from the user and returns a datetime object'''

        year_str = input('Year: ').strip()
        month_str = input('Month: ').strip()
        day_str = input('Day: ').strip()

        # check if date is valid
        year_int,month_int,day_int = LL_API().verifyDate(year_str,month_str,day_str)

        # turn date input into datetime object
        datetime_input = datetime.datetime(year_int,month_int,day_int,0,0,0)
        return datetime_input
    
    def getDateWithTime(self):
        '''Gets a date and time input from the user and returns a datetime object or a string
        if the user wants to quit'''
        
        while True:
            print('Enter departure time: ')
            year_str = input('Year: ').strip()
            month_str = input('Month: ').strip()
            day_str = input('Day: ').strip()
            
            # Check if date is valid
            year_int, month_int, day_int = LL_API().verifyDate(year_str, month_str, day_str)

            hour_str = input('Hour: ').strip()
            minutes_str = input('Minute: ').strip()
            print()

            # check if time is valid
            hour_int, minutes_int = LL_API().verifyTime(hour_str, minutes_str)

            # get date and time now
            time_now = datetime.datetime.now()

            year_now = time_now.year
            month_now = time_now.month
            day_now = time_now.day
            hour_now = time_now.hour
            minutes_now = time_now.minute

            # check if date has passed
            if year_now<=year_int:
                # if it is the same year but input months are in the future
                if year_now == year_int\
                    and month_now <= month_int \
                        and day_now <= day_int:

                    if day_now == day_int and month_now == month_int and year_int == year_now:
                        if hour_now <= hour_int:
                            if hour_now == hour_int:
                                if minutes_now <= minutes_int:
                                    return datetime.datetime(year_int, month_int, day_int, hour_int, minutes_int, 0)
                                else:
                                    print('Date has already passed!')
                            else:
                                return datetime.datetime(year_int, month_int, day_int, hour_int, minutes_int, 0)
                        else:
                            print('Date has already passed!')
                    else:
                        return datetime.datetime(year_int, month_int, day_int, hour_int, minutes_int, 0)
                # if input is earlier this year
                elif year_now == year_int\
                    and month_now > month_int:
                        print('Date has already passed!')
                else:
                    # if year_int is bigger than year now
                    return datetime.datetime(year_int, month_int, day_int, hour_int, minutes_int, 0)
            else:
                print('Date has already passed!')



    def seperateDatetimeString(self, datetime_str):
        '''Seperates a datetime string and returns the split parts'''
               # date             time
        return datetime_str[:10],datetime_str[-8:]


    def prettyprint(self,voyage,voyage_staffed,aircraft_ID,voyage_duration_hrs,\
                flight_no_out, flight_no_home, voyage_duration_min, voyage_state):
        '''Prints out a voyage'''
        print('\n'+'-'*50)
        # destination
        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(),\
            voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))
        print('-'*50)
        
        # status
        print('\t Status: {}'.format(voyage_state))

        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))
        
        # if aircraft is assigned
        if aircraft_ID != 'EMPTY' and aircraft_ID != 'empty':
            airplane = LL_API().getAirplanebyInsignia(aircraft_ID)
            aircraft_type = airplane.get_planeTypeID()
            total_seats = airplane.get_planeCapacity()
            sold_seats_out,sold_seats_home = voyage.getSeatsSold()
            print('\t Seats sold on flight {}: {}/{}'.format(flight_no_out,\
                sold_seats_out,total_seats))
            print('\t Seats sold on flight {}: {}/{}'.format(flight_no_home,\
                sold_seats_home,total_seats))
            print('\t Aircraft: {}, type {}'.format(aircraft_ID,aircraft_type))
        elif aircraft_ID == 'EMPTY' or aircraft_ID == 'empty':
            print('\t Aircraft: No aircraft assigned to voyage')

        print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,\
            voyage_duration_min))
        
        print('\t Status on staff: {}'.format(voyage_staffed))
        print('\t Voyage ID: {}'.format(voyage.getVoyageID()))

        print('-'*50)
        
    def checkVoyagesInRange(self):
        '''Checks if the voyages in a date range are completed.
           Returns None if they're all completed or if there are no voyages on the dates'''
        
        # Gets a tuple with a list of all voyages 
        # in a date range and a list of all completed 
        # voyages in a date range
        voyages_tuple = self.showAllVoyagesInRange()

        if voyages_tuple:
            voyages_on_date, completed_voyages_in_range = voyages_tuple
            
            # All voyages are completed if the lists are equally long
            if len(completed_voyages_in_range) < len(voyages_on_date):
                voyage = self.checkCompleted()
                return voyage
            else:
                print('-'*45+'\n')
                print('{:^45}'.format('All voyages in range are completed'))
                print('{:^45}'.format('not possible to change'))
                print('\n'+'-'*45)
                return None

        else:
            print('-'*45+'\n')
            print('No voyages on these dates.')
            print('\n'+'-'*45)
            return None
    

    def checkCompleted(self):
        '''Gets an voyage id as an input and checks if the voyage is completed'''
        
        while True:
            voyage_id = input("Enter voyage ID to select: ").strip()
            
            # class instance of voyage with inputted ID
            voyage = LL_API().getOneVoyage(voyage_id)
            if voyage:
                # get status of voyage (completed, not departed, in air)
                voyage_state = LL_API().get_status_of_voyage(voyage)
                if voyage_state == 'Completed':
                    print('-'*45+'\n')
                    print('{:^45}'.format('Voyage is completed'))
                    print('\n'+'-'*45)

                    return voyage
                else:
                    return voyage
            else:
                print('\nNo voyage with this ID\n')


    def changeSoldSeats(self,voyage,a_str):
        '''Changes sold seats on a given flight route in a voyage'''
        while True:
            print('\nEnter number of seats sold')
            print('m - to go back\n')
            new_seats_str = input('Enter your input: ').strip()
            if new_seats_str == 'm':
                return 
            elif new_seats_str.isdigit():
                LL_API().changeSoldSeats(voyage,a_str,new_seats_str)
                print('-'*45+'\n')
                print('{:^45}'.format('Number of sold seats successfully changed!'))
                print('\n'+'-'*45)
                return
            else: 
                print('\nInvalid input!')


    def checkRank(self, crew_member,voyage,airplane_type_on_voyage):
        '''Checks if rank of a crewmember, exeption raised if crewmember does not 
            have the right rank, role or licence for the voyage posotion'''
        success = True
        try:
            self.addCrewMember(crew_member,voyage,airplane_type_on_voyage) 
            # exception if pilot does not have License for assigned airplane

        except Exception as e:
            success = False
            print(e)
            input('Press any key to try continue editing voyage ').strip()
        
        if success:
            position = CrewUI().checkRank(crew_member)
            if position == 'Pilot':
                position = 'Copilot'
            
            print('\n'+'~'*45)
            a_str = '{} - {}, {},'.format(crew_member.getName(),crew_member.getRole(),position)
            b_str = 'was added to voyage {}'.format(voyage.getVoyageID())
            print('{:^45}'.format(a_str))
            print('{:^45}'.format(b_str))
            print('~'*45+'\n')



    def addCrewMember(self, crew_member, voyage,airplane_type_on_voyage):
        '''Takes in crew member instance, voyage instance and airplane type.
        Adds crew member to voyage'''
        
        # get role of crew member, where role is pilot or cabincrew
        role = crew_member.getRole()

        if role == 'Pilot':
            # if crew member is captain
            if crew_member.getBool():
                # if there is no captain assigned to voyage
                if voyage.getCaptain() == 'empty':
                    # check if crew member is working on another voyage that day
                    if AddExtraCrewmemberMenu().checkIfCrewmemberWorking(voyage,crew_member):
                        a_str = '\nCaptain is assigned to another voyage on the same date\n\
                            Please chose another captain\n'
                        raise Exception(a_str)

                    voyage.setCaptain(crew_member,airplane_type_on_voyage)
                # if there is already a captain
                else: 
                    raise Exception('A captain is already assigned to the voyage\n')
            # if crewmember is copilot
            else:
                # if there is no assigned copilot
                if voyage.getCopilot() == 'empty':
                    # check if pilot is working on the same day
                    if AddExtraCrewmemberMenu().checkIfCrewmemberWorking(voyage,crew_member):
                        a_str = 'pilot is assigned to another voyage on the same date\n\
                            Please chose another pilot\n'
                        raise Exception(a_str)
                    voyage.setCopilot(crew_member,airplane_type_on_voyage)
                # if there is already a copilot
                else: 
                    raise Exception('A copilot is already assigned to the voyage\n')

        elif role == 'Cabincrew':
            # if crew_member.getBool():
            if voyage.getHeadFlightAtt() == 'empty':
                if AddExtraCrewmemberMenu().checkIfCrewmemberWorking(voyage,crew_member):
                    a_str = 'pilot is assigned to another voyage on the same date\n\
                        Please chose another pilot\n'
                    raise Exception(a_str)
                voyage.setHeadFlightAtt(crew_member)
            else:
                raise Exception('\nA head flight attendant is already assigned to voyage\n')
            # elif crew_member.getBool() == False:
            #     raise Exception('You must add a Head Flight Attendant first\n')

          
            
                
    def addCrewToVoyage(self,voyage):
        '''Adds crew to a voyage'''

        airplane = LL_API().getAirplanebyInsignia(voyage.getAircraftID())
        airplane_type_on_voyage = airplane.get_planeTypeID()

        crew_on_voyage_list = voyage.getCrewOnVoyage()
        
        if 'empty' in crew_on_voyage_list[0:3]:
            print()
            CrewUI().showQualifiedCrew(voyage.getDepartureTime(), voyage.getAircraftID())
            print('You must add 1 captain and 1 copilot with license for {} and 1 head flight attendant'\
                .format(airplane_type_on_voyage))
            print(95*'-')
            print()
            
                
            while 'empty' in crew_on_voyage_list[0:3]:
                # Captain, copilot and head flight attendant must be added added at the same time
                # Voyage must have captain, copilot and head flight attendant 

                crew_member = CrewUI().queryShowNotWorkingCrew()
                if crew_member:
                    self.checkRank(crew_member,voyage,airplane_type_on_voyage)
                    crew_on_voyage_list = voyage.getCrewOnVoyage()

                else:
                    break
                
            if crew_member:
                LL_API().change_voyage(voyage)
                print('~'*70)
                print('A captain, pilot and head flight attendant have been added to voyage {}\n'\
                    .format(voyage.getVoyageID()))
                print('~'*70)
                AddExtraCrewmemberMenu().startAddExtraCrewMenu(voyage,crew_on_voyage_list)
                
            else:
                return 
            

        elif 'empty' in crew_on_voyage_list:
            # If captain, copilot and head flight attendant are assigned to voyage the
            # option to add extra flight attendant is presented  
            print()

            AddExtraCrewmemberMenu().startAddExtraCrewMenu(voyage,crew_on_voyage_list)

        else: 
            print('\nVoyage is fully staffed!\n')
            # If voyage is fully staffed no more crewmembers can be added
            return 

   
   
    def getStatusOfVoyage(self,voyage):
        '''Takes voyage instance and returns the status of the flight 
            (completed, in air, not departed)'''
        return LL_API().get_status_of_voyage(voyage)

    
    
    def showOneVoyage(self,voyage = ''):
        '''Shows one voyage by ID'''

        while True:
            if voyage == '':
                voyage_id = input('\nEnter voyage ID: ').strip()
            else: 
                voyage_id = voyage.getVoyageID()

            voyage = LL_API().getOneVoyage(voyage_id)

            if voyage != None:

                voyage_duration_hrs, voyage_duration_min = \
                LL_API().get_voyage_duration(voyage)

                voyage_state = self.getStatusOfVoyage(voyage)
                
                flight_no_out, flight_no_home = voyage.getFlightNumbers()
                crew_on_voyage_list = voyage.getCrewOnVoyage()
                
                if VoyageUI.EMPTY in crew_on_voyage_list[0:3]: 
                    # not fully staffed if there is not one captain, one pilot and
                    # one head flight attendant 
                    voyage_staffed = 'Voyage not fully staffed'
                else: 
                    voyage_staffed = 'Voyage fully staffed'
                
                
                self.prettyprint(voyage,voyage_staffed,voyage.getAircraftID(),\
                    voyage_duration_hrs,flight_no_out, flight_no_home, voyage_duration_min,\
                        voyage_state)
                
                return voyage

            else:
                return None

        LL_API().change_voyage(voyage)


    
    def revertDatetimeStrtoDatetime(self,datetime_str):
        return LL_API().revertDatetimeStrtoDatetime(datetime_str)

    

    def addAircraftToVoyage(self,voyage):
        '''Adds aircraft to voyage'''
        depart_datetime_object = self.revertDatetimeStrtoDatetime(voyage.getDepartureTime())
        arrival_datetime_object = self.revertDatetimeStrtoDatetime(voyage.getArrivalTimeHome())

        print()
        aircraft_ID = AirplaneUI().getAirplaneInput(depart_datetime_object, arrival_datetime_object)
        voyage.setAircraftID(aircraft_ID)

        print('Airplane has been added to voyage {}'.format(voyage.getVoyageID()))
        return LL_API().change_voyage(voyage)

    def showAllVoyagesInRange(self, start_datetime = '', end_datetime = ''):
        '''Shows all voyages for a current time period'''
 
        if start_datetime == '':
            print('\nEnter start date for time period')
            print()
            start_datetime = VoyageUI().getDateInput()


        if end_datetime == '':
            print('\nEnter end date for time period')
            print()
            end_datetime = VoyageUI().getDateInput()
        

        completed_voyages_in_range = LL_API().getCompletedVoyagesInRange(start_datetime,end_datetime)

        voyages_on_date = LL_API().get_all_voyages_in_date_range(start_datetime,end_datetime)
        start_date = VoyageUI().seperateDatetimeString(start_datetime.isoformat())[0]
        end_date = VoyageUI().seperateDatetimeString(end_datetime.isoformat())[0]
        


        if voyages_on_date != []:
            print()
            print('All voyages from {} to {}'.format(start_date,end_date))
            print(60*VoyageUI.SEPERATOR)

            for voyage in voyages_on_date:

                crew_on_voyage_list = voyage.getCrewOnVoyage()

                flight_no_out, flight_no_home = voyage.getFlightNumbers()

                voyage_duration_hrs, voyage_duration_min = \
                    LL_API().get_voyage_duration(voyage)


                voyage_state = self.getStatusOfVoyage(voyage)

                if VoyageUI.EMPTY in crew_on_voyage_list[0:3]: 
                    # not fully staffed if there is not one captain, one pilot and
                    # one flight attendant 
                    voyage_staffed = 'Voyage not staffed'
                elif VoyageUI.EMPTY in crew_on_voyage_list[-2:]:
                    voyage_staffed = 'Voyage has enough staff'
                else: 
                    voyage_staffed = 'Voyage fully staffed'
                    
                aircraft_ID = voyage.getAircraftID().upper()


                VoyageUI().prettyprint(voyage,voyage_staffed,aircraft_ID,\
                    voyage_duration_hrs, flight_no_out, flight_no_home, \
                        voyage_duration_min, voyage_state)


            return voyages_on_date,completed_voyages_in_range
        else:
            return None



    
    def getDest(self):
        '''Gets user input for a 3 letter destination code'''

        # all destinations
        destinations_class_list = LL_API().get_destinations()
        print()
        print('Please choose a destination. Available destinations are:')

        # print destinations with 3 letter IATA code
        for destination in destinations_class_list[:-1]:
            print('\t{:<3}: {:<10}'.format(destination.getDestinationName(),\
                 destination.getDestinationAirport()))

        print()
        dest = input('Your destination (3 letters): ').upper().strip()
        
        # check if input is valid
        check = LL_API().checkDestInput(dest)
        
        # while input is not valid
        while check == False:
            dest = input('Please enter a valid destination: ').upper().strip()
            check = LL_API().checkDestInput(dest)
        
        return dest



    def addVoyage(self):
        '''Gets input from user to add voyage to file'''
        dest = self.getDest()
        
        # put selection as 2 so while loop is entered
        selection = '2'

        # while user chooses to redo input
        while selection == '2':
            # get datetime input
            departure_datetime = self.getDateWithTime()

            print('Please enter one of the following: ')
            print('1 - Confirm input')
            print('2 - Redo input')
            print('3 - Cancel voyage registration')
            print()
            selection = input('Please choose one of the above: ').strip()
            print()

        # if user confirms input
        if selection == '1':   
            while True:
                if departure_datetime != None:
                    # arrival time found from departure time
                    arrival_time = LL_API().getArrivalTime(departure_datetime, dest)

                    # if date is taken by another voyage
                    while LL_API().checkIfTakenDate(departure_datetime) == True:
                        print('Another voyage is departing or arriving at that time. Please choose another date.')
                        departure_datetime = self.getDateWithTime()

                        if departure_datetime != 'c':
                            continue
                        else:
                            return

                    print('Would you like to assign an airplane to this voyage? (Y/N)')
                    print('(You can also do this later)')
                    selection = input('Y/N: ').lower().strip()

                    # while input is neither y or n
                    while selection != 'y' and selection != 'n':
                        selection = input('Please enter Y or N to make your choice: ').lower().strip()

                    # if chosen to add airplane
                    if selection == 'y':
                        plane_name = AirplaneUI().getAirplaneInput(departure_datetime, arrival_time)
                    # if chosen to add airplane later
                    else:
                        plane_name = 'empty'

                    LL_API().add_voyage(dest, departure_datetime, plane_name)

                    print()
                    print('~'*45)
                    print('{:^45}'.format('New voyage succesfully added!')) 
                    print('~'*45)
                    return
                else:
                    departure_datetime = self.getDateWithTime()
                    continue
        
        # user cancels registration
        elif selection == '3':
            return
        # if nothing else is chosen
        else:
            print('\nInvalid input!\n')



    def removeCrewFromVoyage(self,voyage):
        ''' Removes all crewmembers from voyage'''

        crew_members_counter = 0
        crew_on_voyage = voyage.getCrewOnVoyage()
        for crew_member in crew_on_voyage:
            if crew_member != 'empty':
                crew_members_counter += 1

        if crew_members_counter == 0:
            # if no crewmembers are assinged the can not be removed
            print('\n'+45*'-')
            print('No crewmembers are assigned to the voyage!')
            print(45*'-'+'\n')
        else:
            print('-'*45)
            print('{:^45}'.format('Are you sure you want to'))
            print('{:^45}'.format('remove all crew members?'))
            print('-'*45+'\n')
            print('1 - Yes\n2 - No (Go back)\n')
            selection = input('Please choose one of the above: ').strip()
            if selection == '1':
                voyage.removeCrewFromVoyage()
                LL_API().change_voyage(voyage)
                print('~'*45)
                print('{:^45}'.format('All crewmembers have been removed!'))
                print('~'*45+'\n')

            elif selection == '2':
                return 
            else:
                print('\nInvalid selection!\n')


