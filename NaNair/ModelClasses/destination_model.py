class Destination:
    def __init__(self,name,airport,distance,duration,contact,emergency_phone_number):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration

    def getName(self):
        return self.__name

    def getAirport(self):
        return self.__airport

    def getDuration(self):
        return self.__duration

        
#id,destination,flight duration,distance,emergency name,emergency phone
    def __str__(self):
        format_str = '{:<15}{:<15}{:<10}{:<12}{:<15}{:>12}'.format(self.__name,self.__airport,self.__distance,self.__duration,self.__contact,self.__emergency_phone_number)
        
        return format_str


