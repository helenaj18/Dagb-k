from ModelClasses.crew_model import Crew

class Pilot(Crew):
    def __init__(self, name, crewID, address='', phonenumber='', email='', pilot_license='', captain=0,role=''):
        Crew.__init__(self, name, crewID, address, phonenumber, email)
        self.__pilot_license = pilot_license
        self.__captain = bool(int(captain))
        self.__role = 'Pilot'

    # GET METHODS
    def getLicense(self):
        '''Gets pilots license'''
        return self.__pilot_license

    def canFly(self, type_of_airplane):
        '''Returns True if the license of 
        the pilot is the same as the airplane type,
        else False'''
        return self.getLicense() == type_of_airplane

    def getRole(self):
        '''Gets the role of the pilot'''
        return self.__role
        
    def getBool(self):
        '''Gets the bool that returns True if
        the pilot is a captain, else false'''
        return self.__captain
    
    # SET METHODS

    def setLicense(self,new_license):
        '''Sets a new license'''
        self.__pilot_license = new_license
        return self.__pilot_license

    def setRank(self, new_rank):
        '''Sets a new rank'''
        self.__captain = new_rank
        return self.__captain
    
    def changeCaptainBool(self):
        '''If pilot is a captain (and captain = True) this method will make him a
        copilot (captain = False) and reverse'''

        if self.__captain == True:
            self.__captain = False
        else:
            self.__captain = True
 



