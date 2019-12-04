class Airplane:
    def __init__(self, planeInsignia, planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan):
        self.__planeInsignia = planeInsignia
        self.__planeTypeID = planeTypeId
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


    def __str__(self):
        return self.__planeInsignia+','+self.__planeTypeID+','+self.__manufacturer+','+self.__model+','+\
        self.__capacity+','+self.__emptyWeight+','+self.__maxTakeoffWeight+','+self.__unitThrust+','+self.__serviceCeiling+','+\
        self.__length+','+self.__height+','+self.__wingspan

