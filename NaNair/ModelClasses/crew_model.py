class Crew:
    def __init__(self, name, crewID, address ='', phonenumber='', email=''):
        self.__name = name
        self.__crewID = crewID
        self.__address = address
        self.__phonenumber = phonenumber
        self.__email = email


    def getName(self):
        '''Gets name of crew member'''
        return self.__name
    
    def getCrewID(self):
        '''Gets id of crew member'''
        return self.__crewID
    
    def getAddress(self):
        '''Gets address of crew member'''
        return self.__address
    
    def getPhoneNumber(self):
        '''Gets phone number of crew member'''
        return self.__phonenumber

    def getEmail(self):
        '''Gets email of crew member'''
        return self.__email

    def setAddress(self, new_address):
        '''Sets new address for crew member'''
        self.__address = new_address
        return self.__address
    
    def setPhonenumber(self, new_phonenumber):
        '''Sets new phone number for crew member'''
        self.__phonenumber = new_phonenumber
        return self.__phonenumber

    def setEmail(self, new_email):
        '''Sets new email for crew member'''
        self.__email = new_email
        return self.__email
       

    