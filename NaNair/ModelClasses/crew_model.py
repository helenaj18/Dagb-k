class Crew:
    def __init__(self, name, crewID, address ='', phonenumber='', email=''):
        self.__name = name
        self.__crewID = crewID
        self.__address = address
        self.__phonenumber = phonenumber
        self.__email = email

    def __str__(self):
        return str(self.__crewID) + str(self.__name) + str(self.__address) + str(self.__phonenumber) + str(self.__email)

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

    