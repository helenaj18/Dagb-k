from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL
from LL.crewLL import CrewLL
from LL.voyageLL import VoyageLL

#from UI.crewUI import CrewUI

class LL_API:

    ### AIRPLANE LL 
    def showAllPlanes(self):
        '''Returns a list of airplane instances''' 
        return AirplaneLL().getAirplanes() 
    
    def getAirplanebyInsignia(self, planeInsignia):
        return AirplaneLL().getAirplanebyInsignia(planeInsignia)

    def showAirplanesByType(self, planeTypeId = ''):
        '''Returns a list of airplane instances that have a type inputted by user'''
        return AirplaneLL().getAirplanesByType(planeTypeId)

    def showAirplanesByDateTime(self,date_str):
        '''Returns a tuple of lists of instances. First tuple is planes that are not available,
        the second is planes that are available at the time  inputted by user.'''
        return AirplaneLL().getAirplanesByDateTime(date_str)
    
    def verifyDate(self,year_str,month_str,day_str):
        '''Checks if date is valid. If it is not valid, it will ask user to input another date.'''
        return AirplaneLL().verifyDate(year_str,month_str,day_str)

    def verifyTime(self,hour_str,minute_str):
        '''Checks if time is valid. If it is not valid, it will ask user to input another time.'''
        return AirplaneLL().verifyTime(hour_str,minute_str)
    
    def addAirplane(self):
        ''' Sends info for new ariplane to be added'''
        return AirplaneLL().addAirplane()

    def getAirplaneInsignia(self):
        return AirplaneLL().getAirplaneInsignia()


    def revertDatetimeStrtoDatetime(self,datetime_str):
        return AirplaneLL().revertDatetimeStrtoDatetime(datetime_str)


    ### CREW LL 
    
    def get_crew(self):
        ''' Fetches all crew members and returns a list of instances.'''
        return CrewLL().getCrew()

    def get_pilots(self):
        ''' Fetches all pilots and returns a list of instances.'''
        return CrewLL().getPilots()
    
    def get_flight_att(self):
        '''Returns a list of instances of all flight attendants.'''
        return CrewLL().getFlightAtt()

    def get_working_crew(self,datetime_object):
        return CrewLL().getWorkingCrew(datetime_object)
    
    def get_not_working_crew(self,datetime_object):
        return CrewLL().getNotWorkingCrew(datetime_object)
    
    def get_work_schedule(self,start_date,end_date,crew_id):
        return CrewLL().getWorkSchedule(start_date,end_date,crew_id)

    def get_pilot_by_id(self, pilot_id):
        return CrewLL().getOnePilotID(pilot_id)

    def flight_att_by_id(self, flight_att_id):
        return CrewLL().getOneFlightAttID(flight_att_id)
    
    def get_crew_member_by_id(self,crew_id):
        return CrewLL().getOneCrewMember(crew_id)
    
    def get_licensed_pilots(self, pilot_license):
        return CrewLL().getLicensedPilots(pilot_license)
    
    def sortPilotsByLicense(self):
        
        return CrewLL().sortPilotsByLicense()

    def addCrew(self, info_list):
        return CrewLL().addCrew(info_list)
    

    def changeCrewInfo(self,employee):
        return CrewLL().ChangeCrewInfo(employee)


     ### VANTAR 
    

    ### VOYAGE LL 
 
    def change_voyage(self,voyage):
        return VoyageLL().changeVoyageFile(voyage)

    def add_voyage(self,destination, time, plane):
        return VoyageLL().addVoyage(destination,time, plane)

    def get_all_voyages_in_date_range(self,start_date,end_date):
        return VoyageLL().getVoyageInDateRange(start_date,end_date)

    def get_voyage_duration(self,voyage):
        return VoyageLL().getVoyageDuration(voyage)

    def checkDestInput(self, dest_input):
        return VoyageLL().checkDestInput(dest_input)
    
    def showPlanesForNewVoyage(self, time):
        return VoyageLL().getAvailablePlanes(time)
    
    def checkPlaneInput(self, plane, list_of_planes):
        return VoyageLL().checkPlaneInput(plane, list_of_planes)

    def checkTimeInput(self, year, month, day, hour, min):
        return VoyageLL().checkTimeInput(year, month, day, hour, min)
        
    def getOneVoyage(self,voyage_id):
        return VoyageLL().getOneVoyage(voyage_id)

    def checkIfTakenDate(self, time_datetime):
        return VoyageLL().checkIfTakenTime(time_datetime)

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
    
    def changeDestinationEmergencyContact(self):
        destination_name = input('Enter airport code (IATA): ')
        new_emergency_contact = input('Enter new emergency contact: ')
        print('\nNew Emergency Contact ({}) for {} has been saved.\n'.format(new_emergency_contact,destination_name))
        
        return DestinationLL().changeEmergencyContactName(destination_name,new_emergency_contact)

    def changeDestinationEmergencyPhone(self):
        destination_name = input('Enter airport code (IATA): ')
        new_emergency_phone = input('Enter new emergency phone number: ') 
        print('\nNew Emergency Phone Number ({}) for {} has been saved.\n'.format(new_emergency_phone,destination_name))
               
        return DestinationLL().changeEmergencyContactPhone(destination_name,new_emergency_phone)

    def addDestination(self,new_destination):
        return DestinationLL().addDestination(new_destination)
        
#LL_API.show_all_planes()