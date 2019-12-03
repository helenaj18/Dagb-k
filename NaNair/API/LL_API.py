#from LL import airplaneLL, crewLL, destinationLL, flightroute,voyageLL
#from UI import airplaneUI, crewUI, destinationUI, voyageUI
from LL.airplaneLL import AirplaneLL

class LL_API:

    def show_all_planes(self):
        print('''Fetches all airplanes and returns it''')
        
        AirplaneLL().getAirplanes()
        return 
    
    def show_one_plane(self,plane_ID = ''):
        '''Fetches one specific plane and returns it'''
        return AirplaneLL().getOneAirplane(plane_ID)
    
    def get_crew(self):
        ''' Fetches all crew members'''
        pass

#LL_API.show_all_planes()