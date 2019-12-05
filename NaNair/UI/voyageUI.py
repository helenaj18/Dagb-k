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
    
        date = datetime.datetime(year,month,day,0,0,0).isoformat()

        return date


    def showAllVoyages(self): # BÆTA INN EH TIME PERIOD
        '''Shows all voyages for a current time period'''
        print('Enter start date for time period')
        print()
        start_date = VoyageUI().getDateInput()

        print('Enter end date for time period')
        print()
        end_date = VoyageUI().getDateInput

        voyages_on_date = LL_API().get_all_voyages(start_date,end_date)
        
        print()
        print('All voyages from {}.{}.{} to {}.{}.{}'.format(year,month,day,end_year,end_month,end_day))
        print(60*VoyageUI.SEPERATOR)

        for voyage in voyages_on_date:

            flight_no_out, flight_no_home = voyage.getFlightNumbers()
            crew_on_voyage_list = voyage.getCrewOnVoyage()

            voyage_duration_hrs, voyage_duration_min = LL_API().get_voyage_duration(voyage)


            if VoyageUI.EMPTY in crew_on_voyage_list:
                voyage_staffed = 'Voyage not fully staffed'
            else: 
                voyage_staffed = 'Voyage fully staffed'
                
            aircraft_ID = voyage.getAircraftID()

            if aircraft_ID == VoyageUI.EMPTY: 
                aircraft_ID = 'No aircraft assigned to voyage'


            depature_date = voyage.getDepartureTime()[:10]
            depature_time = voyage.getDepartureTime()[-8:-3]



            print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(), voyage.getDestination().getDestinationAirport(),\
                depature_date ,depature_time))
            print('\t Flight numbers: {} - {}'.format(flight_no_out,flight_no_home))
            print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,voyage_duration_min))

            print('\t Aircraft: {}'.format(aircraft_ID))
            print('\t Status on staff: {}'.format(voyage_staffed))
            print('\t Seats sold: {}'.format('ATH no info'))
            print(60*VoyageUI.SEPERATOR)


            

    def showOneVoyage(self,voyage_ID):
        '''Shows one specific voyage'''
        pass
