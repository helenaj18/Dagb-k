from API.LL_API import LL_API
import datetime



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


    def seperateDatetimeString(self, datetimestring):
        
        return datetimestring[:10]

    def prettyprint(self,voyage,voyage_staffed,aircraft_ID,voyage_duration_hrs,\
                flight_no_out, flight_no_home, voyage_duration_min):

        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(), voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))
        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))
        print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,voyage_duration_min))

        print('\t Aircraft: {}'.format(aircraft_ID))
        print('\t Status on staff: {}'.format(voyage_staffed))
        print('\t Seats sold: {}'.format('ATH no info'))
        


    def showAllVoyages(self): # BÆTA INN EH TIME PERIOD
        '''Shows all voyages for a current time period'''

        print('Enter start date for time period')
        print()
        start_datetime = VoyageUI().getDateInput()
        start_date = VoyageUI().seperateDatetimeString(start_datetime)

        print('Enter end date for time period')
        print()
        end_datetime = VoyageUI().getDateInput()
        end_date = VoyageUI().seperateDatetimeString(end_datetime)

        voyages_on_date = LL_API().get_all_voyages(start_datetime,end_datetime)

        print()
        print('All voyages from {} to {}'.format(start_date,end_date))
        print(60*VoyageUI.SEPERATOR)

        for voyage in voyages_on_date:

            crew_on_voyage_list = voyage.getCrewOnVoyage()

            flight_no_out, flight_no_home = voyage.getFlightNumbers()

            voyage_duration_hrs, voyage_duration_min = LL_API().get_voyage_duration(voyage)

            if VoyageUI.EMPTY in crew_on_voyage_list:
                voyage_staffed = 'Voyage not fully staffed'
            else: 
                voyage_staffed = 'Voyage fully staffed'
                
            aircraft_ID = voyage.getAircraftID()

            if aircraft_ID == VoyageUI.EMPTY: 
                aircraft_ID = 'No aircraft assigned to voyage'

            


            VoyageUI().prettyprint(voyage,voyage_staffed,aircraft_ID,voyage_duration_hrs,\
                flight_no_out, flight_no_home, voyage_duration_min)

            print(60*VoyageUI.SEPERATOR)


            

    def showOneVoyage(self,voyage_ID):
        '''Shows one specific voyage'''
        pass

    def addVoyage(self):

        destinations_class_list = LL_API().get_destinations()
        print('Please choose a destination. Available destinations are:')

        for destination in destinations_class_list:
            print('{:<3}: {:<10}'.format(destination.getDestinationName(), destination.getDestinationAirport()))

        print()
        dest = input('Your destination (3 letters): ')
        print('Enter departure time: ')
        date = input('Date (dd/mm/yyyy): ')
        time = input('Time (hh:mm): ')

        day, month, year = date.split('/')
        hour, min = time.split(':')

        departure_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(min), 0)

        LL_API().add_voyage(dest, departure_time)
