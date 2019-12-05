from API.IO_API import IO_API
from IO.voyageIO import VoyageIO

DEPARTING_DATETIME = 4
ARRIVING_DATETIME = 8

class VoyageLL:
    ''' LL class for voyage '''



    def __init__(self):
        self.voyage_list = IO_API().loadVoyageFromFile()
        #self.upcoming_list = IO_API().read_file()
        
    def splitDates(self, datetime):
        date = datetime[:10]
        year, month, day = date.split('-')

        return int(year), int(month), int(day)

    def getOneVoyage(self, voyage_ID):

        return VoyageIO().getOneVoyage(voyage_ID)

    def getVoyageDuration(self,voyage_instance):
        destination_duration_str = voyage.getDestination().getDuration()





    def getVoyageInDateRange(self, start_datetime, end_datetime):

        voyages = IO_API().loadVoyageFromFile()

        voyages_on_date = []
        voyages_on_date_indexes = []
        

        start_date = start_datetime[:10]
        end_date = end_datetime[:10]
            
        
        for voyage in voyages:

            departure_datetime = voyage.getDepartureTime()
            
            departure_date = departure_datetime[:10]

            arrival_datetime = voyage.getArrivalTime()
            
            arrival_date = arrival_datetime[:10]

            
            if arrival_date == start_date:
                first_voyage_index = voyages.index(voyage)
                voyages_on_date_indexes.append(voyages.index(voyage))

            if departure_date == end_date: 
                voyages_on_date_indexes.append(voyages.index(voyage))

        first_voyage_index = voyages_on_date_indexes[0]
        last_voyage_index = voyages_on_date_indexes[-1]

        for i in range(first_voyage_index,last_voyage_index+1):
            voyages_on_date.append(voyages[i])

    
        return voyages_on_date



            

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





