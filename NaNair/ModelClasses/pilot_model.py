from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', pilot_license='', captain=0):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__pilot_license = pilot_license
        self.__captain = bool(captain)
        self.__role = 'Pilot'


    def __str__(self):
        pass

    def getLicense(self):
        return self.__pilot_license

    def getCaptain(self):
        return self.__captain
    
    def getRole(self):
        return self.__role
        
    def getBool(self):
        return self.__captain
    
    def setAddress(self, new_address):
        self.__address = new_address
        return self.__address
    
    def setEmailAddress(self, new_email_address):
        self.__email = new_email_address
        return self.__email

    def setPhonenumber(self, new_phone_number):
        self.__phonenumber = new_phone_number
        return self.__phonenumber
    
    def changeCaptainBool(self): #fannst setcaptain of oljost ef hann er nu þegar captain
        '''If pilot is a captain (and captain = True) this method will make him a
        copilot (captain = False) and reverse'''

        if self.__captain == True:
            self.__captain = False
        else:
            self.__captain = True
 



