#from LL import airplaneLL, crewLL, destinationLL, flightroute,voyageLL
#from UI import airplaneUI, crewUI, destinationUI, voyageUI
from LL.airplaneLL import AirplaneLL

class LL_API:

    def show_all_planes(self):
        print('''Fetches all airplanes and returns it''')
        #return AirplaneLL.getAirplanes(parameter)
        AirplaneLL.getAirplanes()
        return 
    
    def show_one_plane(self,plane_id):
        '''Fetches one specific plane and returns it'''
        return #airplaneLL.getAirplanes(plane_id)
    
    def get_crew(self):
        pass

#LL_API.show_all_planes()