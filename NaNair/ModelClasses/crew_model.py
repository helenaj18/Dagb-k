class Crew:
    def __init__(self, name, crewID, address ='', phonenumber='', email=''):
        self.__name = name
        self.__crewID = crewID
        self.__address = address
        self.__phonenumber = phonenumber
        self.__email = email

    def getName(self):
        return self.__name
    
    def getCrewID(self):
        return self.__crewID
    
    def getAddress(self):
        return self.__address
    
    def getPhoneNumber(self):
        return self.__phonenumber

    def getEmail(self):
        return self.__email