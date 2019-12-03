from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL
from LL.crewLL import CrewLL
from LL.voyageLL import VoyageLL

#from UI.crewUI import CrewUI

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
        return CrewLL().getCrew()

    def get_pilots(self):
        ''' Fetches all pilots '''
        return CrewLL().getPilots()

     ### VANTAR 
    

    ### VOYAGE LL 

    def change_voyage(self,new_datetime_str,flight_number):
        return VoyageLL().changeDateTimeOfVoyage(new_datetime_str,flight_number)




    # def inputForNewPilot(self):
    #     '''Fetches input from UI layer and puts it in LL layer'''
    #     return CrewUI().addPilot() #some string

    # def NewPilot(self, PilotData):
    #     '''Fetches input from UI layer and puts it in LL layer'''
    #     return CrewLL().addPilot(PilotData) #some string


    # def inputForEditedPilot(self):
    #     '''Gets input from UI layer and sends it to LL layer'''
    #     return CrewUI().inputForEditedPilot() #some list

    # def inputforNewFlightAtt(self):
    #     '''Sends info for new flight attendant'''
    #     return CrewUI().addFlightAtt() #string


    ## DESTINATION LL

    def get_destinations(self):
        '''Gets all destinations NaN Air flies to'''
        return DestinationLL().getDestination()

#LL_API.show_all_planes()