from API.LL_API import LL_API
import datetime



class VoyageUI:
    EMPTY = 'empty'
    SEPERATOR = '-'

    def __init__(self):
        pass

    def __str__(self):
        pass

    def showAllVoyages(self): # BÆTA INN EH TIME PERIOD
        '''Shows all voyages for a current time period'''
        print('Enter start date for time period')
        year = int(input('Year: '))
        month = int(input('Month: '))
        day = int(input('Day: '))
    
        start_date = datetime.datetime(year,month,day,0,0,0).isoformat()

        print('Enter end date for time period')
        end_year = int(input('Year: '))
        end_month = int(input('Month: '))
        end_day = int(input('Day: '))
     
        end_date = datetime.datetime(end_year,end_month,end_day,0,0,0).isoformat()

        voyages_on_date = LL_API().get_all_voyages(start_date,end_date)
        
        print()
        print('All voyages from {}.{}.{} to {}.{}.{}'.format(year,month,day,end_year,end_month,end_day))
        print(60*VoyageUI.SEPERATOR)

        for voyage in voyages_on_date:

            destination = voyage.getDestination() # Destination model object
            destination_airport = destination.getAirport()
            destination_name = destination.getName()
            destination_duration_str = destination.getDuration()

            depature_datetime = voyage.getDepartureTime()
            flight_no_out, flight_no_home = voyage.getFlightNumbers()
            crew_on_voyage_list = voyage.getCrewOnVoyage()

            destination_duration_hrs = int(destination_duration_str[: -4])
            destination_duration_minutes = int(destination_duration_str[-3: -1])

            voyage_duration_min = destination_duration_minutes * 2

            voyage_duration_hrs = destination_duration_hrs * 2 + 1 # Both ways plus one hr layover

            if voyage_duration_min == 60:
                voyage_duration_hrs = voyage_duration_hrs + 1
                voyage_duration_min = 0 
            elif voyage_duration_hrs > 60: 
                voyage_duration_hrs = voyage_duration_hrs + 1
                voyage_duration_min = voyage_duration_min - 60 



            if VoyageUI.EMPTY in crew_on_voyage_list:
                voyage_staffed = 'Voyage not fully staffed'
            else: 
                voyage_staffed = 'Voyage fully staffed'
                
            aircraft_ID = voyage.getAircraftID()

            if aircraft_ID == VoyageUI.EMPTY: 
                aircraft_ID = 'No aircraft assigned to voyage'


            depature_date = depature_datetime[:10]
            depature_time = depature_datetime[-8:-3]



            print('To {}, {} on {} at {}'.format(destination_name,destination_airport,\
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
