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
    
    def setPhonenumber(self, new_phonenumber):
        self.__address = new_phonenumber
    
    def setEmail(self, new_email):
        self.__address = new_email

    def __str__(self):
        pass
        # def a_string(self):
        #     return '{},{},'.format(self.__crewID,self.__name)
        # def b_string(self):
        #     return '{},{},{}'.format(self.__address,self.__phonenumber,self.__email)
        # #return 'CREW MEMBER'

    