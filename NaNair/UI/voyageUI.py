from API.LL_API import LL_API
import datetime
from UI.airplaneUI import AirplaneUI
from UI.crewUI import CrewUI
from UI.extra_crewmember_menu import AddExtraCrewmemberMenu
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

        datetime_input = datetime.datetime(year_int,month_int,day_int,0,0,0)
        return datetime_input
    
    def getDateWithTime(self):
        '''Gets a date and time input from the user
        and returns a datetime object'''
        
        while True:
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

            time_now = datetime.datetime.now()

            year_now = time_now.year
            month_now = time_now.month
            day_now = time_now.day
            hour_now = time_now.hour
            minutes_now = time_now.minute

            if year_now<=year_int \
                and month_now <= month_int \
                    and day_now <= day_int \
                        and hour_now <= hour_int \
                            and minutes_now <= minutes_int:

                    return datetime.datetime(year_int, month_int, day_int, hour_int, minutes_int, 0)
            else:
                print('Date has already passed')



    def seperateDatetimeString(self, datetime_str):
        '''Seperates a datetime string and returns the split parts'''
        return datetime_str[:10],datetime_str[-8:]


    def prettyprint(self,voyage,voyage_staffed,aircraft_ID,voyage_duration_hrs,\
                flight_no_out, flight_no_home, voyage_duration_min, voyage_state):
        '''Prints out a voyage'''

        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(),\
            voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))

        print('\t Status: {}'.format(voyage_state))

        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))
        
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
        

    def queryOneVoyage(self):
        '''Helps user find one voyage and returns it'''
        voyages_tuple = self.showAllVoyagesInRange()

        if voyages_tuple:
            voyages_on_date, completed_voyages_in_range = voyages_tuple
            
            if len(completed_voyages_in_range) < len(voyages_on_date):
                voyage = self.checkCompleted()
                return voyage
            else:
                print('\nAll voyages in range are completed, not possible to change\n')
                return None

        else:
            print('\nNo voyages on these dates.\n')
            return None
    

    def checkCompleted(self):
        '''Checks if a voyage is completed'''
        while True:
            voyage_id = input("Enter voyage ID to select: ").strip()
            voyage = LL_API().getOneVoyage(voyage_id)
            if voyage:
                voyage_state = LL_API().get_status_of_voyage(voyage)
                if voyage_state == 'Completed':
                    print('\nVoyage is completed, not possible to change\n')
                    print('-'*30)
                    return None
                else:
                    return voyage
            else:
                print('\nNo voyage with this ID\n')


    def checkRank(self, crew_member,voyage,airplane_type_on_voyage):
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
            print('{} - {}, {}, was added to voyage {}'.format(
                        crew_member.getName(),
                        crew_member.getRole(), 
                        position,
                        voyage.getVoyageID()
                    ))

    def addCrewMember(self, crew_member, voyage,airplane_type_on_voyage):
        role = crew_member.getRole()

        if role == 'Pilot':
            if crew_member.getCaptain():
                if voyage.getCaptain() == 'empty':
                    voyage.setCaptain(crew_member,airplane_type_on_voyage)
                else: 
                    raise Exception('Captain already added to voyage')
            else:
                if voyage.getCopilot() == 'empty':
                    voyage.setCopilot(crew_member,airplane_type_on_voyage)
                else: 
                    raise Exception('Copilot already added to voyage')
                # GERA eh do you want to replace him 
#############################################

        elif role == 'Cabincrew':
            
            if voyage.getHeadFlightAtt() == 'empty':
                voyage.setHeadFlightAtt(crew_member)
            else:
                raise Exception('Head flight attendant already added to voyage')
            
                
            

    def addCrewToVoyage(self,voyage):
        '''Adds crew to a voyage'''
        #crew_member = CrewUI().queryShowNotWorkingCrew()

        airplane = LL_API().getAirplanebyInsignia(voyage.getAircraftID())
        airplane_type_on_voyage = airplane.get_planeTypeID()

        crew_on_voyage_list = voyage.getCrewOnVoyage()

        if 'empty' in crew_on_voyage_list[0:3]:
            print()
            CrewUI().showQualifiedCrew(voyage.getDepartureTime(), voyage.getAircraftID())
            print('You must add 1 captain and 1 copilot with license for {} and 1 head flight attendant'\
                .format(airplane_type_on_voyage))
            print(60*'-')
            print()
                
            while 'empty' in crew_on_voyage_list[0:3]:
        
                crew_member = CrewUI().queryShowNotWorkingCrew()
                if crew_member:
                    if crew_member.getRole() == 'Pilot':
                        self.checkRank(crew_member,voyage,airplane_type_on_voyage)
                    elif crew_member.getRole() == 'Cabincrew':
                        self.checkRank(crew_member,voyage,airplane_type_on_voyage)
                
                    crew_on_voyage_list = voyage.getCrewOnVoyage()
                else:
                    break
                
            if crew_member:
                LL_API().change_voyage(voyage)
                print('A captain, pilot and head flight attendant have been added to voyage {}'\
                    .format(voyage.getVoyageID()))
            else:
                return 
            

        elif 'empty' in crew_on_voyage_list:
           
            print()

            AddExtraCrewmemberMenu().startAddExtraCrewMenu(voyage,crew_on_voyage_list)

        else: 
            print('\nVoyage is fully staffed!\n')
            return 
############ gera change crew members menu 




    

    def showOneVoyage(self,voyage = ''):
        '''Shows one voyage by ID'''

        while True:
            if voyage == '':
                voyage_id = input('\nEnter voyage ID: ').strip()
            else: 
                voyage_id = voyage.getVoyageID()

            print('-'*30)
            
            voyage = LL_API().getOneVoyage(voyage_id)
            if voyage != None:

                voyage_duration_hrs, voyage_duration_min = \
                LL_API().get_voyage_duration(voyage)

                voyage_state = LL_API().get_status_of_voyage(voyage)
                
                flight_no_out, flight_no_home = voyage.getFlightNumbers()
                crew_on_voyage_list = voyage.getCrewOnVoyage()
                
                if VoyageUI.EMPTY in crew_on_voyage_list[0:3]: 
                    # not fully staffed if there is not one captain, one pilot and
                    # one flight attendant 
                    voyage_staffed = 'Voyage not fully staffed'
                else: 
                    voyage_staffed = 'Voyage fully staffed'
                
                
                self.prettyprint(voyage,voyage_staffed,voyage.getAircraftID(),\
                    voyage_duration_hrs,flight_no_out, flight_no_home, voyage_duration_min, voyage_state)
                
                return voyage

            else:
                return None
            
        else:
            print('Voyage {} fully staffed'.format(voyage.getVoyageID()))
            print('Do you want to add an extra crew member?')
            print('1 - Yes')
            print('2 - No')
            selection = input().strip()
            if selection == '1':

                if 'empty' in crew_on_voyage_list[-2:]:
                    if 'empty' in crew_on_voyage_list[-1]:
                        crew_member = CrewUI().queryShowNotWorkingCrew()
                        voyage.setFlightAttOne(crew_member)
                        

                    elif 'empty' in crew_on_voyage_list[-2]:
                        crew_member = CrewUI().queryShowNotWorkingCrew()
                        voyage.setFlightAttTwo(crew_member)

            elif selection == '2':
                return 
            else:
                print('Invalid selection!')

        LL_API().change_voyage(voyage)

        #return AddExtraCrewmemberMenu().startAddExtraCrewMenu()

    def revertDatetimeStrtoDatetime(self,datetime_str):
        return LL_API().revertDatetimeStrtoDatetime(datetime_str)

    

    def addAircraftToVoyage(self,voyage):
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


                voyage_state = LL_API().get_status_of_voyage(voyage)

                if VoyageUI.EMPTY in crew_on_voyage_list[0:3]: 
                    # not fully staffed if there is not one captain, one pilot and
                    # one flight attendant 
                    voyage_staffed = 'Voyage not fully staffed'
                else: 
                    voyage_staffed = 'Voyage fully staffed'
                    
                aircraft_ID = voyage.getAircraftID().upper()

                # if aircraft_ID == VoyageUI.EMPTY: 
                #     aircraft_ID = None


                VoyageUI().prettyprint(voyage,voyage_staffed,aircraft_ID,\
                    voyage_duration_hrs, flight_no_out, flight_no_home, \
                        voyage_duration_min, voyage_state)

                print(60*VoyageUI.SEPERATOR)

            return voyages_on_date,completed_voyages_in_range
        else:
            return None



    
    def getDest(self):
        '''Gets user input for a 3 letter destination code'''

        destinations_class_list = LL_API().get_destinations()
        print()
        print('Please choose a destination. Available destinations are:')

        for destination in destinations_class_list[:-1]:
            print('\t{:<3}: {:<10}'.format(destination.getDestinationName(),\
                 destination.getDestinationAirport()))

        print()
        dest = input('Your destination (3 letters): ').upper().strip()
        check = LL_API().checkDestInput(dest)
        
        while check == False:
            dest = input('Please enter a valid destination: ').upper().strip()
            check = LL_API().checkDestInput(dest)
        
        return dest



    def addVoyage(self):

        dest = self.getDest()
        print('Enter departure time: ')

        departure_datetime = self.getDateWithTime()
        arrival_time = LL_API().getArrivalTime(departure_datetime, dest)

        while LL_API().checkIfTakenDate(departure_datetime) == True:
            print('Another voyage is departing or arriving at that time. Please choose another date.')
            departure_datetime = self.getDateWithTime()

        print('Would you like to assign an airplane to this voyage? (Y/N)')
        print('(You can also do this later)')
        selection = input().lower().strip()

        while selection != 'y' and selection != 'n':
            print('Please enter Y or N to make your choice')
            selection = input().lower().strip()

        if selection == 'y':
            plane_name = AirplaneUI().getAirplaneInput(departure_datetime, arrival_time)
        else:
            plane_name = 'empty'

        LL_API().add_voyage(dest, departure_datetime, plane_name)

        print()
        print('New voyage succesfully added!\n')
