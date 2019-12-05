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

        voyages_on_dates = LL_API().get_all_voyages(start_date,end_date)
        print()
        print('All voyages from {}.{}.{} to {}.{}.{}'.format(year,month,day,end_year,end_month,end_day))
        print(60*VoyageUI.SEPERATOR)

        for voyage in voyages_on_dates:
            destination = voyage.getDestination()
            destination_name = voyage.getDestinationName()
            depature_datetime = voyage.getDepartureTime()
            return_datetime = voyage.getArrivalTime()
            flight_no_out, flight_no_home = voyage.getFlightNumbers()
            crew_on_voyage_list = voyage.getCrewOnVoyage()


            if VoyageUI.EMPTY in crew_on_voyage_list:
                voyage_manned = 'Voyage not fully manned'
            else: 
                voyage_manned = 'Voyage fully manned'

            aircraft_ID = voyage.getAircraftID()

            if aircraft_ID == VoyageUI.EMPTY: 
                aircraft_ID = 'No aircraft assigned to voyage'
    
            #year

            depature_date = depature_datetime[:10]
            depature_time = depature_datetime[-8:-3]
            total_time = return_datetime #- depature_datetime

            print('To '+destination_name + ', '+destination + ' on ' + depature_date + ' at ' + depature_time)
            print('\t Flight numbers: ' + flight_no_out + ' - ' + flight_no_home)
            print('\t Total time: ' + total_time)
            print('\t Aircraft: ' + aircraft_ID)
            print('\t Status on staff: ' + voyage_manned)
            print('\t Seats sold: ')
            print(60*VoyageUI.SEPERATOR)


            

    def showOneVoyage(self,voyage_ID):
        '''Shows one specific voyage'''
        pass
