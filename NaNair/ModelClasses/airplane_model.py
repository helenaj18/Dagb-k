FORMAT_LENGTH_const = 20

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
        format_str = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(self.planeInsignia,self.planeTypeID,self.manufacturer,self.model,\
        self.capacity,self.length,self.height,self.wingspan)
        
        return format_str



    def formatAirplanes(self):
        '''Formats Airplane lists'''
        
        print('#'*20)
        print('{:^20}'.format('WELCOME'))
        print('#'*20)
        print()
