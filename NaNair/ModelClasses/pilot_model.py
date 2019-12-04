from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', pilot_license='', captain=False):
        Crew.__init__(name, crewID, address, phonenumber, email)
        self.pilot_license = pilot_license
        self.captain = captain
 