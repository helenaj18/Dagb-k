class AircraftTypeModel:

    def __init__(self,planeTypeId,manufacturer,model,capacity,emptyWeight,\
        maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan):

        self.__planeTypeId = planeTypeId
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
        return self.__planeTypeId
    

    def getplaneTypeID(self):
        return self.__planeTypeId
    
    def getManufacturer(self):
        return self.__manufacturer
    
    def getCapacity(self):
        return self.__capacity