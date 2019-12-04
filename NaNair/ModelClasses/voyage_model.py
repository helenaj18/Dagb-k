class Voyage:
    def __init__(self,voyage_ID,flight_no,departure_location,destination,\
                    departure_time,arrival_time,aircraft_ID,captain,copilot,\
                        head_flight_att,flight_att_one,flight_att_two):

        self.__voyage_ID = voyage_ID
        self.__flight_no = flight_no
        self.__departure_location = departure_location
        self.__destination = destination
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__aircraft_ID = aircraft_ID
        self.__captain = captain
        self.__copilot = copilot
        self.__head_flight_att = head_flight_att
        self.__flight_att_one = flight_att_one
        self.__flight_att_two = flight_att_two

    # GERA GET OG SET FYRIR ÞAÐ SEM Á AÐ VERA 

    def __str__(self):
        a_string = str(self.__voyage_ID) +',' + str(self.__flight_no)
    
        return a_string


 
 
