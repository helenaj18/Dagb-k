from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL

class LL_API:

    ### AIRPLANE LL 
    def show_all_planes(self):
        print('''Fetches all airplanes and returns it''')
        
        AirplaneLL().getAirplanes()
        return 
    
    def show_one_plane(self,plane_ID = ''):
        '''Fetches one specific plane and returns it'''
        return AirplaneLL().getOneAirplane(plane_ID)
    
    def add_airplane(self):
        ''' Sends info for new ariplane to be added'''
        return AirplaneLL().addAirplane()

    ### CREW LL 
    
    def get_crew(self):
        ''' Fetches all crew members'''

        return AirplaneLL


    ## DESTINATION LL

    def get_destinations(self):
        '''Gets all destinations NaN Air flies to'''
        return DestinationLL().getDestination()

#LL_API.show_all_planes()