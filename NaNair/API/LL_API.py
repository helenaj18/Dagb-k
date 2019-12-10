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
    

    def addAirplane(self,planeInsignia,planeTypeID,manufacturer,seats):
        ''' Sends info for new airplane to be added'''
        return AirplaneLL().addAirplane(planeInsignia,planeTypeID,manufacturer,seats)

    def getAirplaneInsigniaList(self):
        '''Returns a list of all airplane insignias.'''
        return AirplaneLL().getAirplaneInsigniaList()


    def revertDatetimeStrtoDatetime(self,datetime_str):
        '''Takes in a datetime string and returns a datetime object'''
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
        '''Returns a formatted string of crew that are working at an inputted time'''
        return CrewLL().getWorkingCrew(datetime_object)
    
    def get_not_working_crew(self,datetime_object):
        '''Returns a list of instances of the crew that is not working on a specific day.'''
        return CrewLL().getNotWorkingCrew(datetime_object)
    

    def get_work_schedule(self,start_date,end_date,crew_id):
        '''Returns a list of instances of the voyages that a specific crew member is working in
        for an inputted date.'''
        return CrewLL().getWorkSchedule(start_date,end_date,crew_id)

    
    def get_crew_member_by_id(self,crew_id):
        '''Returns the class instance for the crew member that has the inputted crew id.'''
        return CrewLL().getOneCrewMember(crew_id)
    

    def get_licensed_pilots(self, pilot_license):
        '''Returns a list of class instances of the pilots that have the inputted license.'''
        return CrewLL().getLicensedPilots(pilot_license)
    

    def sortPilotsByLicense(self):
        '''Returns a list of class instances of all pilots, sorted by their licenses.'''
        return CrewLL().sortPilotsByLicense()


    def addCrew(self, info_list):
        '''Takes a list of information for a specific crew member and adds them to file.'''
        return CrewLL().addCrew(info_list)
    

    def changeCrewInfo(self,employee):
        '''Adds changed info of an existing employee chosen by user to file.'''
        return CrewLL().ChangeCrewInfo(employee)
    
    def getQualifiedCrew(self, depart_time, plane_insignia):
        '''Returns a list of instances of crew that can fly a specific plane at a specific time'''
        return CrewLL().getQualifiedCrew(depart_time, plane_insignia)

    def doesIDExist(self, crew_id):
        '''Checks if a crew member already has inputted ID'''
        return CrewLL().doesIDExist(crew_id)


    

    ### VOYAGE LL 
 
    def change_voyage(self,voyage):
        '''Adds changed info of an existing voyage chosen by user to file. '''
        return VoyageLL().changeVoyageFile(voyage)
    
    def getCompletedVoyagesInRange(self,start_datetime, end_datetime):
        return VoyageLL().getCompletedVoyagesInRange(start_datetime, end_datetime)

    def add_voyage(self,destination, time, plane):
        '''Takes in destination, departure time and plane name and 
        registers a new voyage to file.'''
        return VoyageLL().addVoyage(destination,time, plane)


    def get_all_voyages_in_date_range(self,start_date,end_date):
        '''Returns a list of instances of all voyages in a specific time range inputted by user.'''
        return VoyageLL().getVoyageInDateRange(start_date,end_date)


    def get_voyage_duration(self,voyage):
        '''Returns a tuple of hours, minutes of a round trip to a destination inputted by user.'''
        return VoyageLL().getVoyageDuration(voyage)


    def checkDestInput(self, dest_input):
        '''Checks if destination code input is correct. Returns True if it is correct, 
        otherwise False.'''
        return VoyageLL().checkDestInput(dest_input)
    

    def showPlanesForNewVoyage(self, time):
        '''Returns a list of class instances of those planes that are available at a certain time.'''
        return VoyageLL().getAvailablePlanes(time)
    
    
    def checkPlaneInput(self, plane, list_of_planes):
        '''Checks if inputted plane exists in list of available planes inputted by user.
        Returns true if it exists, otherwise False.'''
        return VoyageLL().checkPlaneInput(plane, list_of_planes)

        
    def getOneVoyage(self,voyage_id):
        '''Returns a class instance of voyage with an inputted ID, if it does not exist, 
        None is returned.'''
        return VoyageLL().getOneVoyage(voyage_id)


    def checkIfTakenDate(self, time_datetime):
        '''Checks if a voyage is registered at an inputted time. Returns True if 
        date is taken, otherwise False.'''
        return VoyageLL().checkIfTakenTime(time_datetime)


    def get_status_of_voyage(self, voyage_instance):
        '''Returns status of voyage at the current time'''
        return VoyageLL().getVoyageStatus(voyage_instance)

    def get_upcoming_voyages(self):
        return VoyageLL().getUpcomingVoyges()


    ## DESTINATION LL

    def get_destinations(self):
        '''Gets all destinations NaN Air flies to and returns a list of class instances'''
        return DestinationLL().getDestination()
    
    def changeEmergencyContact(self, destination_instance):
        '''Takes in an updated instance and writes it into the destinations file'''
        return DestinationLL().changeDestinationFile(destination_instance)

    def addDestination(self,new_destination):
        '''Creates a new destination in file'''
        return DestinationLL().addDestination(new_destination)
        
