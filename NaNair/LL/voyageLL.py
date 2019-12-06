from API.IO_API import IO_API
from IO.voyageIO import VoyageIO
from LL.destinationLL import DestinationLL
from datetime import timedelta

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
        destination_duration_str = voyage_instance.getDestination().getDestinationDuration()
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

        return voyage_duration_hrs, voyage_duration_min




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

        if len(voyages_on_date_indexes) != 0:
            first_voyage_index = voyages_on_date_indexes[0]
            last_voyage_index = voyages_on_date_indexes[-1]

            for i in range(first_voyage_index,last_voyage_index+1):
                voyages_on_date.append(voyages[i])

    
            return voyages_on_date
            
        else:
            return None



            

        # for voyage in self.voyage_list:
        #     print(voyage) # þarf að formatta streng
 

    def assignVoyageID(self):
        # Find last voyage id in file by finding id of last voyage
        last_voyageID = self.voyage_list[-1].getVoyageID()
 
        new_id = int(last_voyageID) + 1
 
        return new_id
 
    def assignFlightNo(self, destination, depart_time):
        '''assigns a departing and arriving flight number based on a location'''
    

        if destination == 'LYR':
           first_two = '01'
        elif destination == 'GOH':
           first_two = '02'
        elif destination == 'KUS':
           first_two = '03'
        elif destination == 'FAE':
           first_two = '04'
        else:
           first_two = '05'
        
        #þarf að tekka a ef flug eru á sama degi
        # for voyage in self.voyage_list:
        #     time = voyage.getDepartureTime()
            
        #     if time.date() == depart_time.date():

        latter_two_depart = '00'
        latter_two_arrive = '01'

        departing_num = 'NA' + first_two + latter_two_depart
        arriving_num = 'NA' + first_two + latter_two_arrive

        return departing_num, arriving_num


    def findArrivalTime(self, dest_code, depart_time):
        destinations_instances = DestinationLL().getDestination()

        for destination in destinations_instances:
            if dest_code == destination.getDestinationName():
                duration = destination.getDestinationDuration()
        
        hrs = duration[0]
        mins = duration[1:2]
        
        arrival_time = depart_time + timedelta(hours=hrs, minutes=mins)





 
 
 
 
    def addVoyage(self,destination, departure_time):
        
        #voyage id found from last voyage in file
        voyage_ID = self.assignVoyageID()

        # Flight number
        flight_depart_num, flight_arrive_num = self.assignFlightNo(destination, departure_time)

        # airport found from dest code (3 letter code)
        airport = DestinationLL().getAirport(destination)

        #departing airport
        departing_from = KEF


    

 
 
        # #new_voyage_string = voyage_ID + flight_num + departing_from + destination + departure_time + arrival
 
 
        # VoyageIO().addVoyageToFile()



    def changeDateTimeOfVoyage(self,new_datetime_str,flight_number):

        print('In changeDateTimeofVoyage in VoyageLL.py')

        for i in range(len(self.upcoming_list)):
            if flight_number == self.upcoming_list[i][0]:
                self.upcoming_list[i][3] = new_datetime_str
        
        VoyageIO().changeVoyageFile(self.upcoming_list)

        return 'Change completed'





