from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', pilot_license='', captain=0):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__pilot_license = pilot_license
        self.__captain = bool(int(captain))

    def getLicense(self):
        return self.__pilot_license

    def getCaptain(self):
        return self.__captain
 



