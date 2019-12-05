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

# GET METHODS
    def get_planeTypeID(self):
        return self.__planeTypeID

    def get_planeInsignia(self):
        return self.__planeInsignia

    def get_planeManufacturer(self):
        return self.__manufacturer

    def get_planeModel(self):
        return self.__model

    def get_planeCapacity(self):
        return self.__capacity
    
    def get_planeLength(self):
        return self.__length

    def get_planeHeight(self):
        return self.__height
