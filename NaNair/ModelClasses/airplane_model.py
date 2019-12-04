class Airplane:
    def __init__(self, planeInsignia, planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan):
        self.planeInsignia = planeInsignia
        self.planeTypeID = planeTypeId
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.emptyWeight = emptyWeight
        self.maxTakeoffWeight = maxTakeoffWeight
        self.unitThrust = unitThrust
        self.serviceCeiling = serviceCeiling
        self.length = length
        self.height = height
        self.wingspan = wingspan


    def __str__(self):
        return self.planeInsignia+','+self.planeTypeID+','+self.manufacturer+','+self.model+','+\
        self.capacity+','+self.emptyWeight+','+self.maxTakeoffWeight+','+self.unitThrust+','+self.serviceCeiling+','+\
        self.length+','+self.height+','+self.wingspan

