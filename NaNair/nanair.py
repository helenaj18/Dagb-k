# velkomin 

# UI LAYER 


# LOGIC LAYER



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





