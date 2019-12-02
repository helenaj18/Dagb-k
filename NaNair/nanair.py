# velkomin 

# UI LAYER 


# LOGIC LAYER

class DestinationLL:
    def __init__(self):
        pass
 
    def get_destination(self):
        ''' Gets destination from Destination class'''
        pass
 
 
class CrewLL:
 
    def __init__(self):
        pass
 
    def get_crew(self):
        ''' Gets the whole crew '''
        pass
 
    def get_pilots(self):
        ''' Gets pilot from all the pilots (crew)'''
        pass
 
    def add_pilot(self):
        ''' Adds pilot to pilots (crew)'''
        pass
 
    def edit_pilot(self):
        ''' Edits information of a pilot '''
        pass
 
    def add_flight_attendant(self):
        ''' Adds flight attendant to flight attendants (crew)'''
        pass
 
    def edit_flight_attendant(self):
        ''' Edits information of a flight attendant '''
        pass
 
    def get_working_crew(self):
        ''' Gets the working crew '''
        pass

class VoyageLL:
    ''' LL class for voyage '''
    def __init__(self, voyage,voyageIO):
        self.voyage = voyage
        self.voyageIO = voyageIO
        pass
 
    def get_voyage(self,ID):
        pass
 
    def add_voyage(self):
        pass
 
 
class AirplaneLL:
    ''' LL class for airplane '''
    def __init__(self, airplane, airplaneIO):
        self.airplane = airplane
        self.airplaneIO = airplaneIO
 
    def get_airplanes(self):
        pass
   
    def add_airplane(self):
        pass


class Voyage:
    def __init__(self, airplane, pilot, flight_att, flight_route, voyage_id):
        self.__airplane = airplane
        self.__pilot = pilot
        self.__flight_att = flight_att
        self.__flight_route = flight_route
        self.__voyage_id = voyage_id
 

class Airplane:
    def __init__(self, name, seats, airplane_type):
        self.name = name
        self.seats = seats
        self.airplane_type = airplane_type
 
class Crew:
    def __init__(self, name, crewID, address, landline, mobile, email):
        self.name = name
        self.crewID = crewID
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.email = email
 
 
class Pilot(Crew):
    def __init__(self, pilot_license, captain):
        self.pilotl_icense = pilot_license
        self.captain = captain
 
 
class FlightAttendant(Crew):
    def __init__(self, head_flight_att):
        self.head_flight_att = True
        

class FlightRoute:
    def __init__(self, dep_location, dep_time, dest, duration):
        self.__departure_location = dep_location
        self.__departure_time = dep_time
        self.__destination = dest
        self.__duration = duration


class Destination:
    def __init__(self,name,airport,distance,contact,emergency_phone_number,duration):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration


# IO LAYER 

class DestinationIO:
    def __init__(self, filename):
        self.__destination_filename = filename

    def load_destination_from_file(self):
        '''Fetches destination from a file'''
        pass

    def change_destination_from_file(self):
        '''Change the destination or other destination info in file'''
        pass

    def add_destination_from_file(self):
        '''Adds the destination into file'''
        pass


class PilotIO:
    def __init__(self, filename):
        self.__pilot_filename = filename
    
    def load_pilot_from_file(self):
        '''Fetches pilot info from file'''
        pass

    def change_pilot_from_file(self):
        '''Change pilot info in file'''
        pass

    def add_pilot_from_file(self):
        '''Add pilot info into file'''
        pass

class AttendantIO:

    def __init__(self, filename):
        self.__flight_att_filename = filename

    def load_flight_att_from_file(self):
        '''Gets info of flight attendant from file'''
        pass

    def change_flight_att_from_file(self):
        '''Changes the info of flight attendant'''
        pass

    def add_flight_att_from_file(self):
        '''Adds flight attendant info into file'''
        pass


class AirplaneIO:

    def __init__(self,filename):
        self.__airplane_filename = filename

    def load_airplane_from_file(self):
        '''Loads existing airplanes from the file'''
        pass

    def change_airplane_from_file(self):
        '''Changes an existing airplane in the file'''
        pass

    def add_airplane_from_file(self):
        '''Adds a new airplane to the file'''
        pass


class VoyageIO:

    def __init__(self,filename):
        self.__voyage_filename = filename

    def load_voyage_from_file(self):
        '''Loads existing voyages from the file'''
        pass

    def change_voyage_from_file(self):
        '''Changes an existing voyage in the file'''
        pass

    def add_voyage_from_file(self):
        '''Adds a new voyage to the file'''
        pass