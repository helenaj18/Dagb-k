from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', pilot_license='', captain=0):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.pilot_license = pilot_license
        self.captain = bool(int(captain))
 
    def __str__(self):
        string = '{:<25}{:<20}{:<20}'.format(self.name,self.crewID,self.pilot_license)

        if self.captain:
            string += '{:<10}'.format('Captain')
        else:
            string += '{:<10}'.format('Co-pilot')

        return string



