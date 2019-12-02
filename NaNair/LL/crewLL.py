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