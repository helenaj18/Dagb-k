from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL
from LL.crewLL import CrewLL
from LL.voyageLL import VoyageLL

#from UI.crewUI import CrewUI

class LL_API:

    ### AIRPLANE LL 
    def showAllPlanes(self):
        
        return AirplaneLL().getAirplanes() 
    
    def showAirplanesByType(self, planeTypeId = ''):
        '''Gets a list of airplanes by type'''
        return AirplaneLL().getAirplanesByType(planeTypeId)
    
    def addAirplane(self):
        ''' Sends info for new ariplane to be added'''
        return AirplaneLL().addAirplane()

    ### CREW LL 
    
    def get_crew(self):
        ''' Fetches all crew members'''
        return CrewLL().getCrew()

    def get_pilots(self):
        ''' Fetches all pilots '''
        return CrewLL().getPilots()
    
    def get_flight_att(self):
        return CrewLL().getFlightAtt()

    def get_working_crew(self):
        return CrewLL.getWorkingCrew()

    def get_pilot_by_id(self, pilot_id):
        return CrewLL().getOnePilotID(pilot_id)

    def flight_att_by_id(self, flight_att_id):
        return CrewLL().getOneFlightAttID(flight_att_id)
    
    def get_licensed_pilots(self, pilot_license):
        return CrewLL().getLicensedPilots(pilot_license)




     ### VANTAR 
    

    ### VOYAGE LL 

    def change_voyage(self,new_datetime_str,flight_number): # BÆTA INN EH TIME PERIOD
        return VoyageLL().changeDateTimeOfVoyage(new_datetime_str,flight_number)

    def add_voyage(self,destination, time):
        return VoyageLL().addVoyage(destination,time)

    def get_all_voyages(self):
        return VoyageLL().getVoyage()
        


    ### DESTINATION LL

    


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