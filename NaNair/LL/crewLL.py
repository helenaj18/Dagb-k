class CrewLL:
 
    def __init__(self):
        pass
 
    def getCrew(self):
        ''' Gets the whole crew '''
        pass
 
    def getPilots(self):
        ''' Gets pilot from all the pilots (crew)'''
        pass
 
    def addPilot(self):
        ''' Adds pilot to pilots (crew)'''
        pass
 
    def editPilot(self):
        ''' Edits information of a pilot '''
        pass
 
    def addFlightAttendant(self):
        ''' Adds flight attendant to flight attendants (crew)'''
        pass
 
    def editFlightAttendant(self):
        ''' Edits information of a flight attendant '''
        pass
 
    def getWorkingCrew(self):
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