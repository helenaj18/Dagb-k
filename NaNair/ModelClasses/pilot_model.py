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

    def setLicense(self, new_license):
        self.__pilot_license = new_license
    
    def changeCaptainBool(self): #fannst setcaptain of oljost ef hann er nu þegar captain
        '''If pilot is a captain (and captain = True) this method will make him a
        copilot (captain = False) and reverse'''

        if self.__captain == True:
            self.__captain = False
        else:
            self.__captain = True
 



