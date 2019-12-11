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
        '''Gets plane type ID'''
        return self.__planeTypeID

    def get_planeInsignia(self):
        '''Gets plane insignia'''
        return self.__planeInsignia

    def get_planeManufacturer(self):
        '''Gets plane manufacturer'''
        return self.__manufacturer

    def get_planeModel(self):
        '''Gets plane model'''
        return self.__model

    def get_planeCapacity(self):
        '''Gets plane capacity'''
        return self.__capacity
    