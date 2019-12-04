from API.LL_API import LL_API
import datetime

class VoyageUI:

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

        for item in voyages_on_dates:
            print(item)

    def showOneVoyage(self,voyage_ID):
        '''Shows one specific voyage'''
        pass
