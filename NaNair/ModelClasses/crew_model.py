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

    def setAddress(self, new_address):
        self.__address = new_address
        return self.__address
    
    def setPhonenumber(self, new_phonenumber):
        self.__phonenumber = new_phonenumber
        return self.__phonenumber

    def setEmail(self, new_email):
        self.__email = new_email
        return self.__email

    def __str__(self):
        pass
       

    