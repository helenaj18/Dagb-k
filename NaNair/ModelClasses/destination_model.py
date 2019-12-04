class Destination:
    def __init__(self,name,airport,distance,contact,emergency_phone_number,duration):
        self.__name = name
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__emergency_phone_number = emergency_phone_number
        self.__duration = duration

    def __str__(self):
        
        return str(self.__name) +','+str(self.__airport) + ','+str(self.__distance)+','+str(self.__contact)+','+str(self.__emergency_phone_number)+','+str(self.__duration)

