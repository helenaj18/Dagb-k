from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, pilot_license, captain):
        self.pilot_license = pilot_license
        self.captain = captain
 