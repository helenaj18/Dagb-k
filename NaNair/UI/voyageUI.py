from API.LL_API import LL_API
import datetime
from UI.airplaneUI import AirplaneUI
from LL.voyageLL import VoyageLL


class VoyageUI:
    EMPTY = 'empty'
    SEPERATOR = '-'

    def __init__(self):
        pass

    def __str__(self):
        pass

    def getDateInput(self):

        year = int(input('Year: '))
        month = int(input('Month: '))
        day = int(input('Day: '))

        return datetime.datetime(year,month,day,0,0,0).isoformat()
    
    def getDateWithTime(self):

        year = input('Year: ')
        month = input('Month: ')
        day = input('Day: ')
        
        year, month, day = LL_API().verifyDate(year, month, day)

        hour = input('Hour: ')
        min = input('Minute: ')
        print()

        hour, min = LL_API().verifyTime(hour, min)

        return datetime.datetime(int(year), int(month), int(day), int(hour), int(min), 0)


    def seperateDatetimeString(self, datetimestring):
        
        return datetimestring[:10]

    def totalSeats(aircraft_ID):
        pass

    def prettyprint(self,voyage,voyage_staffed,aircraft_ID,voyage_duration_hrs,\
                flight_no_out, flight_no_home, voyage_duration_min):

        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(),\
            voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))

        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))

        print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,\
            voyage_duration_min))

        print('\t Aircraft: {}'.format(aircraft_ID))
        print('\t Status on staff: {}'.format(voyage_staffed))
        print('\t Seats sold: {}/{}'.format('ATH no info','total seats'))
        print('\t Voyage ID: {}'.format(voyage.getVoyageID()))
        
    def queryOneVoyage(self):
        '''Helps user find one voyage and returns it'''

        self.showAllVoyagesInRange()
        voyage = None
        while voyage is None:
            voyage_id = input("Enter voyage ID to select: ")
            voyage = VoyageLL().getOneVoyage(voyage_id)
            if voyage:
                return voyage
            print("Invalid voyage id")
    
    def showOneVoyage(self):
        '''Shows one voyage by ID'''
        while True:
            voyage_id = input("Enter voyage ID: ")
            voyage = VoyageLL().getOneVoyage(voyage_id)
            if voyage != None:

                voyage_duration_hrs, voyage_duration_min = \
                LL_API().get_voyage_duration(voyage)
                
                flight_no_out, flight_no_home = voyage.getFlightNumbers()
                crew_on_voyage_list = voyage.getCrewOnVoyage()
                
                if VoyageUI.EMPTY in crew_on_voyage_list[0:3]: 
                    # not fully staffed if there is not one captain, one pilot and
                    # one flight attendant 
                    voyage_staffed = 'Voyage not fully staffed'
                else: 
                    voyage_staffed = 'Voyage fully staffed'
                
                
                self.prettyprint(voyage,voyage_staffed,voyage.getAircraftID(),\
                    voyage_duration_hrs,flight_no_out, flight_no_home, voyage_duration_min)
                
                return
            else:
                print('No voyage with this ID')
            


    def showAllVoyagesInRange(self): # BÆTA INN EH TIME PERIOD
        '''Shows all voyages for a current time period'''

        print('Enter start date for time period')
        print()
        start_datetime = VoyageUI().getDateInput()
        start_date = VoyageUI().seperateDatetimeString(start_datetime)

        print('Enter end date for time period')
        print()
        end_datetime = VoyageUI().getDateInput()
        end_date = VoyageUI().seperateDatetimeString(end_datetime)

        voyages_on_date = LL_API().get_all_voyages_in_date_range(start_datetime,end_datetime)

        print()
        print('All voyages from {} to {}'.format(start_date,end_date))
        print(60*VoyageUI.SEPERATOR)

        for voyage in voyages_on_date:

            crew_on_voyage_list = voyage.getCrewOnVoyage()

            flight_no_out, flight_no_home = voyage.getFlightNumbers()

            voyage_duration_hrs, voyage_duration_min = \
                LL_API().get_voyage_duration(voyage)

            if VoyageUI.EMPTY in crew_on_voyage_list[0:3]: 
                # not fully staffed if there is not one captain, one pilot and
                # one flight attendant 
                voyage_staffed = 'Voyage not fully staffed'
            else: 
                voyage_staffed = 'Voyage fully staffed'
                
            aircraft_ID = voyage.getAircraftID()

            if aircraft_ID == VoyageUI.EMPTY: 
                aircraft_ID = 'No aircraft assigned to voyage'

            


            VoyageUI().prettyprint(voyage,voyage_staffed,aircraft_ID,\
                voyage_duration_hrs, flight_no_out, flight_no_home, \
                    voyage_duration_min)

            print(60*VoyageUI.SEPERATOR)


    
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
            print('Please enter a valid destination!')
            dest = input().upper()
            check = LL_API().checkDestInput(dest)
        
        return dest




    def addVoyage(self):

        dest = self.getDest()
        print('Enter departure time: ')

        departure_time = self.getDateWithTime()

        print('Please choose an airplane.')

        airplanes_class_list = LL_API().showPlanesForNewVoyage(departure_time)

        for plane in airplanes_class_list:
            print('\t{:<6}: {:<10}'.format(plane.get_planeInsignia(),\
                 plane.get_planeTypeID()))        

        plane_name = input('Chosen plane (type name of plane): ').upper()
        check = LL_API().checkPlaneInput(plane_name, airplanes_class_list)

        while check == False:
            print('Please choose one of the listed planes.')
            plane_name = input()
            check = LL_API().checkPlaneInput(plane_name, airplanes_class_list)

        LL_API().add_voyage(dest, departure_time, plane_name)

        print()

        print('New voyage succesfully added!\n')
