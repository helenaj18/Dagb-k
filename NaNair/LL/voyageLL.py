from API.IO_API import IO_API
from IO.voyageIO import VoyageIO

DEPARTING_DATETIME = 4
ARRIVING_DATETIME = 8

class VoyageLL:
    ''' LL class for voyage '''



    def __init__(self):
        self.voyage_list = IO_API().loadVoyageFromFile()
        #self.upcoming_list = IO_API().read_file()
 
    def getVoyage(self,start_date,end_date):

        voyages = IO_API().loadVoyageFromFile()

        voyages_on_date = []
        
        for voyage in voyages:
            



       return voyages_on_date




        # departing_datetime_str = voyage[DEPARTING_DATETIME].departure_time 
        # departing_date, departing_time = departing_datetime_str.split('T')

        # arriving_datetime_str = voyage[ARRIVING_DATETIME].arrival_time
        # arriving_date ,arriving_time = arriving_datetime_str.split('T')

        # for voyage in voyages: 
        #     departing_date ,departing_time = voyage.departure_time.split('T')
        #     arriving_date ,arriving_time = voyage.arrival_time.split('T')

        #     if start_date == departing_date: #[DEPARTING_DATETIME]:
        #         first_voyage_index = voyages.index(voyage)
        #         voyage_date_indexes.append(first_voyage_index)
            
        #     if end_date == arriving_date:
        #         last_voyage_index = voyages.index(voyage)
        #         voyage_date_indexes.append(last_voyage_index)

        # first_voyage_index = voyage_date_indexes[0]
        # last_voyage_index = voyage_date_indexes[-1]

        # voyages_on_date.append(voyages[first_voyage_index:last_voyage_index])

        

        

        # for voyage in self.voyage_list:
        #     print(voyage) # þarf að formatta streng
 
    def addVoyage(self,destination, departure_time):

        return print('in add voyage LL')


        # voyage_ID = 10

        # # flight_num
        # departing_from = KEF
        
        # destination_list = IO_API().loadDestinationFromFile()
        # print(destination_list) ## 


        # #new_voyage_string = voyage_ID + flight_num + departing_from + destination + departure_time + arrival


        # VoyageIO().addVoyageToFile()


    def changeDateTimeOfVoyage(self,new_datetime_str,flight_number):

        print('In changeDateTimeofVoyage in VoyageLL.py')

        for i in range(len(self.upcoming_list)):
            if flight_number == self.upcoming_list[i][0]:
                self.upcoming_list[i][3] = new_datetime_str
        
        VoyageIO().changeVoyageFile(self.upcoming_list)

        return 'Change completed'





