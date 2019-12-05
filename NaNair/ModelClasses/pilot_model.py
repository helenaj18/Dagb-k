from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', pilot_license='', captain=0):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__pilot_license = pilot_license
        self.__captain = bool(int(captain))

    def getLicense(self):
        return self.__pilot_license

    def getCaptainBool(self):
        return self.__captain
 
    def __str__(self):
        string = '{:<25}{:<20}'.format(self._Crew__name,self._Crew__crewID)

        if self.__captain:
            string += '{:<25}'.format('Captain')
        else:
            string += '{:<25}'.format('Co-pilot')
        
        string += '{:<20}'.format(self.__pilot_license)

        return string



