class Crew:
    def __init__(self, name, crewID, address ='', phonenumber='', email=''):
        self.name = name
        self.crewID = crewID
        self.address = address
        self.phonenumber = phonenumber
        self.email = email

    def __str__(self):
        return 'Þetta er strengur'