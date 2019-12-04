from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', pilot_license='', captain=False):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.pilot_license = pilot_license
        self.captain = captain
 
    def __str__(self):
        string = '{:<25}{:<20}'.format(self.name,self.crewID)

        if self.captain:
            string += '{:<10}'.format('Captain')
        else:
            string += '{:<10}'.format('Co-pilot')

        return string



