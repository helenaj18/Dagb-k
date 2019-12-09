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

        year_str = input('Year: ')
        month_str = input('Month: ')
        day_str = input('Day: ')

        # check if date is valid
        year_int,month_int,day_int = LL_API().verifyDate(year_str,month_str,day_str)

        datetime_input = datetime.datetime(year_int,month_int,day_int,0,0,0)
        return datetime_input
    
    def getDateWithTime(self):
        '''Gets a date and time input from the user and returns a datetime object'''

        year_str = input('Year: ')
        month_str = input('Month: ')
        day_str = input('Day: ')
        
        # check if date is valid
        year_int, month_int, day_int = LL_API().verifyDate(year_str, month_str, day_str)

        hour_str = input('Hour: ')
        minutes_str = input('Minute: ')
        print()

        # check if time is valid
        hour_int, minutes_int = LL_API().verifyTime(hour_str, minutes_str)

        return datetime.datetime(year_int, month_int, day_int, hour_int, minutes_int, 0)


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
        
        if aircraft_ID != 'EMPTY':
            airplane = LL_API().getAirplanebyInsignia(aircraft_ID)
            aircraft_type = airplane.get_planeTypeID()
            total_seats = airplane.get_planeCapacity()
            sold_seats_out,sold_seats_home = voyage.getSeatsSold()
            print('\t Seats sold on flight {}: {}/{}'.format(flight_no_out,\
                sold_seats_out,total_seats))
            print('\t Seats sold on flight {}: {}/{}'.format(flight_no_home,\
                sold_seats_home,total_seats))
            print('\t Aircraft: {}, type {}'.format(aircraft_ID,aircraft_type))
        elif aircraft_ID == 'EMPTY':
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

                while True:
                    voyage_id = input("Enter voyage ID to select: ")
                    voyage = LL_API().getOneVoyage(voyage_id)
                    if voyage:
                        voyage_state = LL_API().get_status_of_voyage(voyage)
                        if voyage_state == 'Completed':
                            print('Voyage is completed, not possible to change')
                        else:
                            return voyage
                    print("Invalid voyage id")
            else:
                print('All voyages in range are completed, not possible to change')
                return None

        else:
            print()
            print('No voyages on these dates')
            print()
    



    def checkRank(self, crew_member,voyage,airplane_type_on_voyage):
        success = True
        try:
            self.addCrewMember(crew_member,voyage,airplane_type_on_voyage) 
            # exception if pilot does not have License for assigned airplane

        except Exception as e:
            success = False
            print(e)
            input('Press any key to try continue editing voyage')
        
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
                voyage.setCaptain(crew_member,airplane_type_on_voyage)
            else:
                voyage.setCopilot(crew_member,airplane_type_on_voyage)
        elif role == 'Cabincrew':
                voyage.setHeadFlightAtt(crew_member)
            
                
            



    def addCrewToVoyage(self,voyage):
        '''Adds crew to a voyage'''
        #crew_member = CrewUI().queryShowNotWorkingCrew()
        insignia = voyage.getAircraftID()
        airplane = LL_API().getAirplanebyInsignia(voyage.getAircraftID())
        airplane_type_on_voyage = airplane.get_planeTypeID()

        crew_on_voyage_list = voyage.getCrewOnVoyage()

        if 'empty' in crew_on_voyage_list[0:3]:
            CrewUI().showNotWorkingCrew(voyage.getDepartureTime())
            print()

            print('You must add 1 captain and 1 copilot with license for {} and 1 head flight atttendant'\
                .format(airplane_type_on_voyage))
            while 'empty' in crew_on_voyage_list[0:3]:
                crew_member = CrewUI().queryShowNotWorkingCrew()
                if crew_member.getRole() == 'Pilot':
                    self.checkRank(crew_member,voyage,airplane_type_on_voyage)
                elif crew_member.getRole() == 'Cabincrew':
                    self.checkRank(crew_member,voyage,airplane_type_on_voyage)
                    

                crew_on_voyage_list = voyage.getCrewOnVoyage()

        elif 'empty' in crew_on_voyage_list:
            AddExtraCrewmemberMenu().startAddExtraCrewMenu(voyage,crew_on_voyage_list)

        else: 
            print('Voyage is fully staffed')
            return 


    

    def showOneVoyage(self,voyage = ''):
        '''Shows one voyage by ID'''

        while True:
            if voyage == '':
                voyage_id = input('Enter voyage ID: ')
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
                
                return

            else:
                return None
            
        else:
            print('Voyage {} fully staffed'.format(voyage.getVoyageID()))
            print('Do you want to add an extra crew member?')
            print('1 - Yes')
            print('2 - No')
            selection = input()
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

        LL_API().change_voyage(voyage)

        #return AddExtraCrewmemberMenu().startAddExtraCrewMenu()

    def revertDatetimeStrtoDatetime(self,datetime_str):
        return LL_API().revertDatetimeStrtoDatetime(datetime_str)

    

    def addAircraftToVoyage(self,voyage):
        datetime_object = self.revertDatetimeStrtoDatetime(voyage.getDepartureTime())

        AirplaneUI().showAirplanesByDateTime(datetime_object)
        print()
        print('Which Aircraft would you like to assign to voyage {}? (PlaneInsignia)'.format(voyage.getVoyageID()))
        print()
        aircraft_ID = input().upper()
        voyage.setAircraftID(aircraft_ID)

        return LL_API().change_voyage(voyage)

    def changeTimeOfVoyage(self,voyage):
        print('Enter new date and time')
        year = input('Year: ')
        month = input('Month: ')
        day = input('Day: ')
        time = input('Time: (HH:MM) ')
        hrs = time[:2]
        mins = time[-2:]
        new_time = datetime.datetime(year,month,day,hrs,mins,0,0).isoformat()
        voyage.setDepartureTime(new_time)
        return LL_API().change_voyage(voyage)


    def showAllVoyagesInRange(self, start_datetime = '', end_datetime = ''):
        '''Shows all voyages for a current time period'''
 
        if start_datetime == '':
            print('Enter start date for time period')
            print()
            start_datetime = VoyageUI().getDateInput()


        if end_datetime == '':
            print('Enter end date for time period')
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
        dest = input('Your destination (3 letters): ').upper()
        check = LL_API().checkDestInput(dest)
        
        while check == False:
            dest = input('Please enter a valid destination: ').upper().strip()
            check = LL_API().checkDestInput(dest)
        
        return dest
        


    
    def getAirplaneInput(self,departure_datetime):
        print('Please choose an airplane.')

        airplanes_class_list = LL_API().showPlanesForNewVoyage(departure_datetime)

        for plane in airplanes_class_list:
            print('\t{:<6}: {:<10}'.format(plane.get_planeInsignia(),\
                    plane.get_planeTypeID()))        

        plane_name = input('Chosen plane (type name of plane on this format TF-XXX): ').upper().strip()
        check = LL_API().checkPlaneInput(plane_name, airplanes_class_list)

        while check == False:
            print('Please choose one of the listed planes.')
            plane_name = input().upper().strip()
            check = LL_API().checkPlaneInput(plane_name, airplanes_class_list)
        
        return plane_name



    def addVoyage(self):

        dest = self.getDest()
        print('Enter departure time: ')

        departure_datetime = self.getDateWithTime()

        while LL_API().checkIfTakenDate(departure_datetime) == True:
            print('Another voyage is departing or arriving at that time. Please choose another date.')
            departure_datetime = self.getDateWithTime()

        print('Would you like to assign an airplane to this voyage? (Y/N)')
        print('(You can also do this later)')
        selection = input().lower()

        while selection != 'y' and selection != 'n':
            print('Please enter Y or N to make your choice')
            selection = input()

        if selection == 'y':
            plane_name = self.getAirplaneInput(departure_datetime)
        else:
            plane_name = 'empty'

        LL_API().add_voyage(dest, departure_datetime, plane_name)

        print()
        print('New voyage succesfully added!\n')
