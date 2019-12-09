from API.IO_API import IO_API
from IO.voyageIO import VoyageIO
from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL
import datetime



class VoyageLL:
    ''' LL class for voyage '''

    # When a new voyage is added there are no sold seats
    seats_sold_out = '0'
    seats_sold_home = '0'

    # def __init__(self):
    #     self.voyage_list = IO_API().loadVoyageFromFile()

        
    # def splitDates(self, datetime):       # EKKI Í NOTKUN ??
    #     date = datetime[:10]
    #     year, month, day = date.split('-')

    #     return int(year), int:(month), int(day)

    
    def getUpcomingVoyges(self):
        voyage_list = IO_API().loadVoyageFromFile()
        date_today =  datetime.datetime.today()
        upcoming_voyages_list = []

        for voyage in voyage_list: 
            if voyage.getDepartureTime() >= date_today:
                upcoming_voyages_list.append(voyage)

        return upcoming_voyages_list
                 
        

    def getOneVoyage(self, voyage_to_get_ID_str):
        '''Takes in voyage id and returns the voyage class instance that has that id'''
        
        voyage_instance_list = IO_API().loadVoyageFromFile()
        for voyage_instance in voyage_instance_list:
            voyage_ID_str = voyage_instance.getVoyageID()
            if voyage_ID_str == voyage_to_get_ID_str: 
                return voyage_instance
                
        return None
                


    def getVoyageDuration(self,voyage_instance):
        ''' Returns voyage duration in hours and minutes'''
        
        # duration of one way trip in hrs and mins, format: xxhxxm where xx are numbers
        duration_str = voyage_instance.getDestination().getDestinationDuration()

        # hrs and mins isolated
        duration_hrs_int = int(duration_str[: -4])
        duration_minutes_int = int(duration_str[-3: -1])
        voyage_duration_min_int = duration_minutes_int * 2

        # Duration of round trip plus 1 hour layover
        voyage_duration_hrs_int = duration_hrs_int * 2 + 1 

        if voyage_duration_min_int == 60:
            voyage_duration_hrs_int = voyage_duration_hrs_int + 1
            voyage_duration_min_int = 0 

        elif voyage_duration_hrs_int > 60: 
            voyage_duration_hrs_int = voyage_duration_hrs_int + 1
            voyage_duration_min_int = voyage_duration_min_int - 60 

        return voyage_duration_hrs_int, voyage_duration_min_int


    def isEmployeeWorkingOnDate(self, date, employee_id):
        '''Checks if an inputted employee is working on an inputted date.
        Returns True if he is, else False.'''

        voyages_intstance_list = self.getVoyageInDateRange(date, date)
        for voyage in voyages_intstance_list:
            if employee_id in voyage.getCrewOnVoyage():
                return True
        return False


    def getVoyageStatus(self, voyage_instance):
        '''Takes a voyage instance and checks its status based on current time. A string describing 
        the status is returned.'''

        time_now_datetime = datetime.datetime.now()

        voyage_depart_date_str = voyage_instance.getDepartureTime()
        voyage_arrive_date_str = voyage_instance.getArrivalTimeHome()

        # Turn depart and arrive time string into a datetime value
        voyage_depart_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_depart_date_str)
        voyage_arrive_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_arrive_date_str)

        # if voyage departed before current time
        if time_now_datetime < voyage_depart_datetime:
            status_str = 'Not departed'
        # if voyage departed before current time but has not yet arrived
        elif time_now_datetime >= voyage_depart_datetime and time_now_datetime < voyage_arrive_datetime:
            status_str = 'In air'
        # if voyage has arrived    
        else:
            status_str = 'Completed'
        
        return status_str

    def addCaptain(self, voyage_id, date, employee_id):
        '''Captain added to an existing voyage'''

        is_unavailable_bool = self.isEmployeeWorkingOnDate(date, employee_id)
        if is_unavailable_bool:
            raise Exception("Staff member notavailable on this date")
        voyage_instance = VoyageIO.getOneVoyage(voyage_id)
        if voyage_instance is None:
            raise Exception("Voyage not found")
        voyage_instance.setCaptain(employee_id)


    def getVoyageInDateRange(self, start_datetime, end_datetime):
        ''' Returns a list of instances of all voyages in a certain date range'''

        voyages_instance_list = IO_API().loadVoyageFromFile()

        voyages_on_date_list = []

        list_of_dates = []
        delta = datetime.timedelta(days=1)

        while start_datetime <= end_datetime:
            list_of_dates.append(start_datetime.date().isoformat())
            start_datetime += delta

            
        for voyage in voyages_instance_list:
            departure_datetime = voyage.getDepartureTime()
            departure_date = departure_datetime[:10]

            arrival_datetime = voyage.getArrivalTimeHome()
            arrival_date = arrival_datetime[:10]

            if departure_date in list_of_dates:
                voyages_on_date_list.append(voyage)

            elif arrival_date in list_of_dates:
                voyages_on_date_list.append(voyage)

        return voyages_on_date
    
    def getCompletedVoyagesInRange(self, start_datetime, end_datetime):
        '''Gets a list of completed voyages
           in a date range'''
        voyages_on_date = self.getVoyageInDateRange(start_datetime, end_datetime)
        completed_voyage_list = []

        for voyage in voyages_on_date:
            if self.getVoyageStatus(voyage) == 'Completed':
                completed_voyage_list.append(voyage)
        
        return completed_voyage_list
        return voyages_on_date_list
            


    def assignVoyageID(self):
        '''Assign a voyage an id based on last voyage in file.'''
        
        # get voyage id of last voyage in file
        last_voyageID_str = self.voyage_list[-1].getVoyageID()
 
        new_id_int = int(last_voyageID_str) + 1
        return str(new_id_int)
 

    def assignFlightNo(self, destination, depart_time):
        '''Assigns a departing and arriving flight number based on a location
        and other trips that day.'''
    
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

        # if no voyages are on the departing day
        latter_two_depart = '00'
        latter_two_arrive = '01'

        for voyage_instance in voyage_list:
            # if the dest IATA code matches the voyage in file there is another voyage to 
            # the same destination on the same day
            if destination == voyage_instance.getDestination().getDestinationAirport():
                # flight numbers of registered voyage:
                depart_num, arrival_num = voyage_instance.getFlightNumbers()

                # if the registered voyage has higher numbers
                if latter_two_depart <= depart_num[-2:]:
                    latter_two_depart = str( int(depart_num[-2:]) + 2 )
                    latter_two_arrive = str( int(arrival_num[-2:]) + 2 )
                # int() removes the zero so it is added back in
                if len(latter_two_depart) == 1:
                    latter_two_depart = '0' + latter_two_depart
                    latter_two_arrive = '0' + latter_two_arrive

        departing_num = 'NA' + first_two + latter_two_depart
        arriving_num = 'NA' + first_two + latter_two_arrive

        return departing_num, arriving_num


    def TimeDifference(self, time_datetime, dest_code):
        '''Calculates time difference between KEF and destinations'''
        
        if dest_code == 'LYR':
            time_datetime = time_datetime + datetime.timedelta(hours=1)
        elif dest_code == 'GOH' or dest_code == 'KUS':
            time_datetime = time_datetime + datetime.timedelta(hours=-3)

        # time in faroe islands (FAE) and tingwall (LWK) is gmt so no need to change

        return time_datetime


    def findArrivalTime(self, dest_code, depart_time_datetime):
        '''Takes in destination code and departure time and returns arrival time at
        destination as datetime object.'''

        destinations_instances = DestinationLL().getDestination()

        # finds duration of flight to destination as string
        for destination in destinations_instances:
            if dest_code == destination.getDestinationAirport():
                duration_str = destination.getDestinationDuration()
        
        # turns duration string into int values, form of string is xxhxxm where x are numbers
        index_of_h_int = duration_str.find('h')

        if index_of_h_int == 1:    
            hrs_int = int(duration_str[0])
        else:
            hrs_int = int(duration_str[ :(index_of_h_int - 1) ])
        mins_int = int(duration_str[(index_of_h_int + 1):3])
        
        arrival_time_datetime = depart_time_datetime + timedelta(hours=hrs_int, minutes=mins_int)

        return arrival_time_datetime


    def getAvailablePlanes(self, departure_time):
        '''Finds which planes are available at departing time. Returns list of insatnces of 
        available planes.'''
        
        available_tuple = AirplaneLL().getAirplanesByDateTime(departure_time)
        
        # if available tuple is None all planes are available
        if available_tuple != None:
            not_available_planes,available_planes = available_tuple    
        else:
            available_planes = AirplaneLL().getAirplanes()
        
        return available_planes


    def checkPlaneInput(self, plane_input, list_of_plane_instances):
        '''Checks if inputted plane exists in inputted list of available planes'''

        BoolCheck = False
        for plane in list_of_plane_instances:
            if plane_input == plane.get_planeInsignia():
                BoolCheck = True
        
        return BoolCheck

 
    def addVoyage(self,destination, departure_time, plane):
        '''Finds values from input to register a new voyage. Returns a list with all info.'''    
    
        voyage_id = self.assignVoyageID()

        # Flight numbers
        flight_depart_num, flight_arrive_num = self.assignFlightNo(destination, departure_time)

        # arrival time in other country added, time difference taken into account
        arrival_time_gmt = self.findArrivalTime(destination, departure_time)
        arrival_time_out = self.TimeDifference(arrival_time_gmt, destination)

        # plane stops at destination for 1 hour 
        departure_time_back = arrival_time_out + datetime.timedelta(hours=1)

        arrival_time_back = self.findArrivalTime(destination, departure_time_back)

        # info added to list in same order as in allvoyages.csv
        info_list = [voyage_id, flight_depart_num, self.seats_sold_out, 'KEF', destination,\
                    departure_time.isoformat(), arrival_time_out.isoformat(),\
                    flight_arrive_num, self.seats_sold_home, destination, 'KEF',\
                    departure_time_back.isoformat(), arrival_time_back.isoformat(),\
                    plane]

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
        
        start_time = departure_datetime + datetime.timedelta(minutes=-30)
        end_time = departure_datetime + datetime.timedelta(minutes=30)

        # list of voyages that depart the same day
        voyages_during_departure_date = self.getVoyageInDateRange(start_time, end_time)

        # list of all times in restricted hour
        while start_time <= end_time:
            datetime_list.append(start_time.isoformat())
            start_time += datetime.timedelta(minutes=1)

        # if a voyage that departs the same day as inputted voyage is also in datetime_list
        # it is too close in time
        for voyage in voyages_during_departure_date:
            if voyage.getDepartureTime() in datetime_list:
                taken = True
            elif voyage.getArrivalTimeHome() in datetime_list:
                taken = True
        
        return taken


    def changeVoyageFile(self,voyage):
        '''Sends class instance of updated employee into IO layer to read into file'''
        return IO_API().changeVoyageFile(voyage)





