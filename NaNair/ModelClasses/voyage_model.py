
class Voyage:
    def __init__(self,voyage_ID,flight_no,seats_sold_out,flight_no_home,seats_sold_home,departure_location,destination,\
                    departure_time,departure_time_out,arrival_time_out,arrival_time_home,aircraft_ID,captain,copilot,\
                        head_flight_att,flight_att_one,flight_att_two):

        self.__voyage_ID = voyage_ID
        self.__flight_no_out = flight_no
        self.__flight_no_home = flight_no_home
        self.__departure_location = departure_location
        self.__destination = destination
        self.__departure_time = departure_time
        self.__departure_time_out = departure_time_out
        self.__arrival_time_out = arrival_time_out
        self.__arrival_time_home = arrival_time_home
        self.__aircraft_ID = aircraft_ID
        self.__captain = captain
        self.__copilot = copilot
        self.__head_flight_att = head_flight_att
        self.__flight_att_one = flight_att_one
        self.__flight_att_two = flight_att_two
        self.__seats_sold_out = seats_sold_out
        self.__seats_sold_home = seats_sold_home
        
    def getDepartureLocation(self):
        '''Returns the departure location of a voyage'''
        return self.__departure_location

    def getDepartureTime(self):
        '''Returns the departure time of a voyage'''
        return self.__departure_time

    def getDepartureTimeAtDestination(self):
        '''Returns the departure time at destination of a voyage'''
        return self.__departure_time_out

    def getArrivalTimeOut(self):
        '''Returns the arrival time out of a voyage'''
        return self.__arrival_time_out
        
    def getArrivalTimeHome(self):
        '''Returns the arrival time home of a voyage'''
        return self.__arrival_time_home

    def getSeatsSold(self):
        '''Gets seats sold out and home in a tuple'''
        return self.__seats_sold_out,self.__seats_sold_home

    def getCrewOnVoyage(self):
        '''Gets crew members on a voyage in a list'''
        crew_on_voyage_list = [self.__captain, self.__copilot, self.__head_flight_att,\
            self.__flight_att_one, self.__flight_att_two]
        return crew_on_voyage_list

    def getFlightNumbers(self):
        '''Returns flight numbers of a voyage in a tuple'''
        return self.__flight_no_out, self.__flight_no_home

    def getDestination(self):
        '''Gets destination instance in a voyage'''
        return self.__destination

    def getAircraftID(self):
        '''Gets the aircraft ID of a voyage'''
        return self.__aircraft_ID

    def getCaptain(self):
        '''Gets the captain's ID in a voyage'''
        return self.__captain

    def getCopilot(self):
        '''Gets the copilot's ID in a voyage'''
        return self.__copilot
    
    def getHeadFlightAtt(self):
        '''Gets the head flight attendant in a voyage'''
        return self.__head_flight_att
    
    def getFlightAttOne(self):
        '''Gets the flight attendant one in a voyage'''
        return self.__flight_att_one

    def getFlightAttTwo(self):
        ''''Gets the flight attendant two in a voyage'''
        return self.__flight_att_two


    def getVoyageID(self):
        '''Gets the voyage id'''
        return self.__voyage_ID


    # SET METHODS
    def setDepartureTime(self, new_time):
        '''Sets the departure time '''
        self.__departure_time = new_time
    
    def setArrivalTime(self, new_time):
        '''Sets the arrival time '''
        self.__arrival_time = new_time
    
    def setAircraftID(self, new_id):
        '''Sets the aircraft id'''
        self.__aircraft_ID = new_id
    
    def setDepartNum(self, new_number):
        self.__flight_no_out = new_number
    
    def setArrivalNum(self, new_number):
        self.__flight_no_home = new_number
    
    def setCaptain(self, new_capt, airplane_type):
        '''Check if captain can fly this type 
        and set the new captain if he can'''

        if not new_capt.canFly(airplane_type):
            raise Exception("Pilot can not fly this type")
    
        self.__captain = new_capt.getCrewID()
    
    def setCopilot(self, new_copilot,airplane_type):
        '''Check if copilot can fly this type 
        and set the new copilot if he can'''

        if not new_copilot.canFly(airplane_type):
            raise Exception("Copilot can not fly this type")
    
        self.__copilot = new_copilot.getCrewID()
    
    def setHeadFlightAtt(self, new_head):
        '''Check if flight attendant is a head flight attendant 
        and set the new head flight attendant if he can'''

        if not new_head.getBool():
            raise Exception('You must add a head flight attendant')
        
        self.__head_flight_att = new_head.getCrewID()

    def setFlightAttOne(self, new_att):
        '''Sets flight attendant one'''
        self.__flight_att_one = new_att.getCrewID()
    
    def setFlightAttTwo(self, new_att):
        '''Sets flight attendant two'''
        self.__flight_att_two = new_att.getCrewID()

    def setSeatsSoldOut(self,new_seat_number):
        '''Sets seats sold out'''
        self.__seats_sold_out = new_seat_number
        
    def setSeatsSoldHome(self,new_seat_number):
        '''Sets seats sold home'''
        self.__seats_sold_home = new_seat_number
                

    def removeCrewFromVoyage(self):
        self.__captain = 'empty'
        self.__copilot = 'empty'
        self.__head_flight_att = 'empty'
        self.__flight_att_one = 'empty'
        self.__flight_att_two = 'empty'
        
    def removeAirplaneFromVoyage(self):
        self.__aircraft_ID = 'empty'