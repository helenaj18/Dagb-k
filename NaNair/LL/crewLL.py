from API.IO_API import IO_API
from API.LL_API import LL_API

class CrewLL:
 
    def __init__(self):
        pass
 
    def getCrew(self):
        ''' Gets the whole crew '''
        pilots = self.getPilots
        flight_att = IO_API().loadFlightAttFromFile()

        total_crew = pilots + flight_att

        return total_crew

 
    def getPilots(self):
        ''' Gets pilot from all the pilots (crew)'''
        pilots = IO_API().loadPilotFromFile()

        return pilots
        
 
    def addPilot(self):
        ''' Adds pilot to pilots (crew)'''
        # input from UI layer
        new_pilot_str = LL_API().inputForNewPilot()

        return new_pilot_str


 
    def editPilot(self):
        ''' Edits information of a pilot '''
        pass
 
    def addFlightAttendant(self):
        ''' Adds flight attendant to flight attendants (crew)'''
        
 
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