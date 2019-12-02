#from LL import airplaneLL, crewLL, destinationLL, flightroute,voyageLL
#from UI import airplaneUI, crewUI, destinationUI, voyageUI
# from LL.airplaneLL import airplaneLL

class LL_API:

    def show_all_planes(self):
        print('''Fetches all airplanes and returns it''')
        #return AirplaneLL.getAirplanes(parameter)
        return 'Næs!'
    
    def show_one_plane(self):
        '''Fetches one specific plane and returns it'''
        return airplaneLL.getAirplanes(parameter)
    
    def get_crew(self):
        pass
