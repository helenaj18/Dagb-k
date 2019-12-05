FORMAT_LENGTH_const = 20

class Airplane:
    def __init__(self, planeInsignia, planeTypeID,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan):
        self.__planeInsignia = planeInsignia
        self.__planeTypeID = planeTypeID
        self.__manufacturer = manufacturer
        self.__model = model
        self.__capacity = capacity
        self.__emptyWeight = emptyWeight
        self.__maxTakeoffWeight = maxTakeoffWeight
        self.__unitThrust = unitThrust
        self.__serviceCeiling = serviceCeiling
        self.__length = length
        self.__height = height
        self.__wingspan = wingspan


    def get_planeTypeID(self):
        return self.__planeTypeID

    def __str__(self):
        format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(self.__planeInsignia,self.__planeTypeID,self.__manufacturer,self.__model,\
        self.__capacity,self.__length,self.__height,self.__wingspan)
        
        return format_str



    # def formatAirplanes(self):
    #     '''Formats Airplane lists'''
        
    #     print('#'*20)
    #     print('{:^20}'.format('WELCOME'))
    #     print('#'*20)
    #     print()
