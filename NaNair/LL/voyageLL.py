from API.IO_API import IO_API
from IO.voyageIO import VoyageIO
from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL
from datetime import timedelta
from datetime import datetime



class VoyageLL:
    ''' LL class for voyage '''

    # When a new voyage is added
    # the solds seats are 0
    seats_sold_out = '0'
    seats_sold_home = '0'

    def __init__(self):
        self.voyage_list = IO_API().loadVoyageFromFile()

        
    # def splitDates(self, datetime):       # EKKI Í NOTKUN ??
    #     date = datetime[:10]
    #     year, month, day = date.split('-')

    #     return int(year), int(month), int(day)


    def getOneVoyage(self, voyage_to_get_ID):

        voyage_list = IO_API().loadVoyageFromFile()
        for voyage in voyage_list:
            voyage_ID = voyage.getVoyageID()
            if voyage_ID == voyage_to_get_ID: 
                return voyage
                
        return None


    def getVoyageDuration(self,voyage_instance):
        ''' Returns voyage duration, flight duration back and forth plus a one hr layover'''

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


    def isEmployeeWorkingOnDate(self, date, employee_id):

        voyages = self.getVoyageInDateRange(date, date)
        for voyage in voyages:
            if employee_id in voyage.getCrewOnVoyage():
                return True
        return False


    def getVoyageStatus(self, voyage_instance):
        '''Returns the status of voyage'''

        time_now = datetime.now()

        voyage_depart_date_str = voyage_instance.getDepartureTime()
        voyage_arrive_date_str = voyage_instance.getArrivalTimeHome()

        voyage_depart_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_depart_date_str)
        voyage_arrive_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_arrive_date_str)

        if time_now < voyage_depart_datetime:
            status = 'Not departed'
        elif time_now >= voyage_depart_datetime and time_now < voyage_arrive_datetime:
            status = 'In air'
        else:
            status = 'Completed'
        
        return status

    def addCaptain(self, voyage_id, date, employee_id):

        is_unavailable = self.isEmployeeWorkingOnDate(date, employee_id)
        if is_unavailable:
            raise Exception("Staff member notavailable on this date")
        voyage = VoyageIO.getOneVoyage(voyage_id)
        if voyage is None:
            raise Exception("Voyage not found")
        voyage.setCaptain(employee_id)


    def getVoyageInDateRange(self, start_datetime, end_datetime):
        ''' Returns a list of instances of all voyages in a certain date range'''

        voyages = IO_API().loadVoyageFromFile()
        date = type(start_datetime)

        voyages_on_date = []

        list_of_dates = []
        delta = timedelta(days=1)

        while start_datetime <= end_datetime:
            list_of_dates.append(start_datetime.date().isoformat())
            start_datetime += delta

            
        for voyage in voyages:
            departure_datetime = voyage.getDepartureTime()
            departure_date = departure_datetime[:10]

            arrival_datetime = voyage.getArrivalTimeHome()
            arrival_date = arrival_datetime[:10]

            if departure_date in list_of_dates:
                voyages_on_date.append(voyage)

            elif arrival_date in list_of_dates:
                voyages_on_date.append(voyage)

        return voyages_on_date
            


    def assignVoyageID(self):
        '''Find last voyage id in file by finding id of last voyage'''
        
        last_voyageID = self.voyage_list[-1].getVoyageID()
 
        new_id = int(last_voyageID) + 1
 
        return str(new_id)
 

    def assignFlightNo(self, destination, depart_time):
        '''assigns a departing and arriving flight number based on a location'''
    
        # first two letters are dictated by destination
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
        
        # all voyages on departing day
        voyage_list = self.getVoyageInDateRange(depart_time, depart_time)

        latter_two_depart = '00'
        latter_two_arrive = '01'

        for voyage_instance in voyage_list:
            if destination == voyage_instance.getDestination().getDestinationAirport():
                depart_num, arrival_num = voyage_instance.getFlightNumbers()
                if latter_two_depart <= depart_num[-2:]:
                    latter_two_depart = str( int(depart_num[-2:]) + 2 )
                    latter_two_arrive = str( int(arrival_num[-2:]) + 2 )
                if len(latter_two_depart) == 1:
                    latter_two_depart = '0' + latter_two_depart
                    latter_two_arrive = '0' + latter_two_arrive

        departing_num = 'NA' + first_two + latter_two_depart
        arriving_num = 'NA' + first_two + latter_two_arrive

        return departing_num, arriving_num


    def TimeDifference(self, time, dest_code):
        '''calculates time difference from iceland time'''
        if dest_code == 'LYR':
            time = time + timedelta(hours=1)
        elif dest_code == 'GOH' or dest_code == 'KUS':
            time = time + timedelta(hours=-3)

        # time in faroe islands (FAE) and tingwall (LWK) is gmt so no need to change

        return time


    def findArrivalTime(self, dest_code, depart_time):
        destinations_instances = DestinationLL().getDestination()

        for destination in destinations_instances:
            if dest_code == destination.getDestinationAirport():
                duration = destination.getDestinationDuration()
        
        hrs = int(duration[0])
        mins = int(duration[2:3])
        
        arrival_time = depart_time + timedelta(hours=hrs, minutes=mins)

        return arrival_time


    def getAvailablePlanes(self, departure_time):
        available_tuple = AirplaneLL().getAirplanesByDateTime(departure_time.isoformat())
        
        if available_tuple != None:
            not_available_planes,available_planes = available_tuple
            
        else:
            available_planes = AirplaneLL().getAirplanes()
        
        return available_planes


    def checkPlaneInput(self, plane_input, list_of_planes):

        BoolCheck = False
        for plane in list_of_planes:
            if plane_input == plane.get_planeInsignia():
                BoolCheck = True
        
        return BoolCheck

 
    def addVoyage(self,destination, departure_time, plane):
    
        info_list = []
        voyage_id = self.assignVoyageID()

        info_list.append( voyage_id )

        # Flight number
        flight_depart_num, flight_arrive_num = self.assignFlightNo(destination, departure_time)

        info_list.append(flight_depart_num)
        
        info_list.append(VoyageLL.seats_sold_out)

        #departing airport added to info
        info_list.append('KEF')
        info_list.append(destination)

        info_list.append(departure_time.isoformat())

        arrival_time_gmt = self.findArrivalTime(destination, departure_time)

        # arrival time in other country added
        arrival_time_out = self.TimeDifference(arrival_time_gmt, destination)
        info_list.append(arrival_time_out.isoformat())

        info_list.append(flight_arrive_num)
        info_list.append(VoyageLL.seats_sold_home)

        #ARRIVING TRIP

        # departing from and arriving at when on return trip appended
        info_list.append(destination)
        info_list.append('KEF')


        # depart time added to list
        # plane stops at destination for 1 hour 
        departure_time_back = arrival_time_out + timedelta(hours=1)
        info_list.append(departure_time_back.isoformat())

        arrival_time_back = self.findArrivalTime(destination, departure_time_back)
        info_list.append( arrival_time_back.isoformat() )

        info_list.append(plane)

        # staff not yet added so those values will be empty
        for i in range(5):
            info_list.append('empty')
        
        new_voyage_str = ','.join(info_list)


        IO_API().addVoyageToFile(new_voyage_str)


    def checkDestInput(self, dest_input):
        '''Checks if destination IATA code is valid'''

        destinations_instances = DestinationLL().getDestination()
        boolOutcome = False

        if len(dest_input) == 3:
            for destination in destinations_instances:
                if dest_input == destination.getDestinationAirport():
                    boolOutcome = True
        
        return boolOutcome

    def checkIfTakenTime(self, departure_datetime):
        '''Checks if date inputted by user is taken by another voyage'''

        taken = False
        datetime_list = []

        # assume one plane can leave each half hour
        
        start_time = departure_datetime + timedelta(minutes=-30)
        end_time = departure_datetime + timedelta(minutes=30)

        voyages_during_departure_date = self.getVoyageInDateRange(start_time, end_time)

        while start_time <= end_time:
            datetime_list.append(start_time.isoformat())
            start_time += timedelta(minutes=1)

        for voyage in voyages_during_departure_date:
            if voyage.getDepartureTime() in datetime_list:
                taken = True
            elif voyage.getArrivalTimeHome() in datetime_list:
                taken = True
        
        return taken


    def changeVoyageFile(self,voyage):
        return IO_API().changeVoyageFile(voyage)





