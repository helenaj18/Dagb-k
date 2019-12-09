
from API.IO_API import IO_API
from IO.crewIO import CrewIO
from LL.voyageLL import VoyageLL
from ModelClasses.flight_att_model import FlightAttendant
from ModelClasses.pilot_model import Pilot
from LL.airplaneLL import AirplaneLL

class CrewLL:


    ROLE_const = 2
    RANK_const = 3
    LICENSE_const = 4

    def getPilots(self):
        ''' Gets the pilots '''
        crew_list = IO_API().loadCrewFromFile()
        pilot_list = []
        #iterates through crew file and appends the pilots to pilot list
        for employee in crew_list:
            if type(employee) == Pilot:
                pilot_list.append(employee)

        return pilot_list
    
    
    def getFlightAtt(self):
        ''' Gets the flight attendants '''
        crew_list = IO_API().loadCrewFromFile()
        flight_att_list = []
        #iterates through crew file and appends the flight attendants to flith attendants list
        for employee in crew_list:
            if type(employee) == FlightAttendant:
                flight_att_list.append(employee)
        
        return flight_att_list


    def getCrew(self):
        ''' Returns a list of class instances for all crew '''
        return IO_API().loadCrewFromFile()
    

    def getOneCrewMember(self,input_crew_id):
        ''' Returns crew memeber which holds given ID number'''
        crew = self.getCrew()
        #itirates through the crew file and finds memeber with given ID
        while True:
            for crew_member in crew:
                crew_id = crew_member.getCrewID()
                if input_crew_id == crew_id:
                    return crew_member
            else: 
                return None
 
    
    def getLicensedPilots(self, pilot_license):
        '''Takes in a pilot license and finds all pilots who have the inputted license.
        Returns a list of class instances'''
        pilots_instances_list = self.getPilots()
        licensedPilots = []

        # Checks all pilots if they have inputted license. IF they do they are added to a list
        for pilot in pilots_instances_list:
            if pilot_license == pilot.getLicense():
                licensedPilots.append(pilot)
        
        return licensedPilots
 
 
    def addCrew(self, CrewData):
        '''Takes in a list of data and formats it to a string to add to file.
        '''
        # add necessary data that can be found from user input
        # if 'Captain' was selected in UI layer
        if CrewData[2] == '1': 
            CrewData.insert(self.ROLE_const, 'Pilot')
            CrewData[self.RANK_const] = '1'

        # if 'Copilot' was selected in UI layer
        elif CrewData[2] == '2':
            CrewData.insert(self.ROLE_const, 'Pilot')
            CrewData[self.RANK_const] = '0'

        # if 'Head service manager' was selected in UI layer
        elif CrewData[2] == '3':
            CrewData.insert(self.ROLE_const, 'Cabincrew')
            CrewData.insert(self.LICENSE_const, 'N/A')
            CrewData[self.RANK_const] = '1'
        
        # if 'Flight Attendant' was selected in UI layer
        else:
            CrewData.insert(self.ROLE_const, 'Cabincrew')
            CrewData.insert(self.LICENSE_const, 'N/A')
            CrewData[self.RANK_const] = '0'

        new_employee_str = ','.join(CrewData)

        return IO_API().addCrew(new_employee_str)



    def ChangeCrewInfo(self,employee):
        ''' Changes emplpyees information'''
        IO_API().changeCrewInfo(employee)



    def sortPilotsByLicense(self):
        '''Sorts all pilots by their license'''
        pilot_list = self.getPilots()
        sorted_pilots_list = []

        licenses = set()
        # make a set of all licenses to iterate through
        for pilot in pilot_list:
            licenses.add( pilot.getLicense() )

        # checks if a pilot has a specific license and append them to a list if so  
        for a_license in licenses:
            for pilot in pilot_list:
                if pilot.getLicense() == a_license:
                    sorted_pilots_list.append(pilot)
        
        return sorted_pilots_list
 

    def getWorkingCrew(self,datetime_object):
        ''' Returns a string of the working crew on a date inputted by user'''
        
        working_crew_list = []
        # Gets a list of the people working on inputted date and the
        # destination they're going to
        working_crew_id_list = self.getWorkingCrewIdList(datetime_object)

        #format_str = ''

        if working_crew_id_list != None:
            for working_crew_per_voyage in working_crew_id_list:
                destination_instance = working_crew_per_voyage[1]
                destination_name = destination_instance.getDestinationName()

                for crew_id in working_crew_per_voyage[0]:
                    if crew_id != 'empty':
                        crew_member = self.getOneCrewMember(crew_id)
                        working_crew_list.append((crew_member,destination_name))
            
            return working_crew_list

        #if no one is working on the inputted date
        else:
            return None


    def getWorkingCrewIdList(self,datetime_object):
        '''Takes in a date and returns a list of IDs for the people working on that date'''

        # Voyages on a specific date:
        voyage_list = VoyageLL().getVoyageInDateRange(datetime_object,datetime_object)
        self.working_crew_id_list = []
        
        #iterates through voyages on a specific date and adds the IDs of working crew 
        # to list as well as the voyage destination
        if voyage_list != None:
            for voyage in voyage_list:
                crew_on_voyage_list = voyage.getCrewOnVoyage()
                destination_of_voyage = voyage.getDestination()
                self.working_crew_id_list.append((crew_on_voyage_list,destination_of_voyage))

            if len(self.working_crew_id_list) != 0:
                return self.working_crew_id_list
            # if no crew was assigned to the voyages
            else:
                return None
        # if there are no voyages on a chosen date
        else:
            return None


    def getNotWorkingCrew(self,datetime_object):
        '''Gets a list of instances of crew members
           that are not working on a specific day'''
        
        self.getWorkingCrew(datetime_object)
        not_working_crew_list = []
        all_crew = IO_API().loadCrewFromFile()

        #Checks if the crew memeber is in working list, if not, the crew member is added
        # to list of not working crew members
        if len(all_crew) != 0:
            for crew_member in all_crew:
                if crew_member.getCrewID() not in self.working_crew_id_list:
                    not_working_crew_list.append(crew_member)
            return not_working_crew_list
        else:
            return None

    def getQualifiedCrew(self, depart_time, plane_insignia):
        '''Returns a instance list of crew that is both qualified for a specific plane 
        and is not working'''

        plane_instance = AirplaneLL().getAirplanebyInsignia(plane_insignia)
        plane_license = plane_instance.get_planeTypeID()

        depart_datetime = AirplaneLL().revertDatetimeStrtoDatetime(depart_time)

        not_working_list = self.getNotWorkingCrew(depart_datetime)
        licensed_pilots_list = self.getLicensedPilots(plane_license)

        if licensed_pilots_list != []
            licensed_pilots_id_list = []

            for pilot in licensed_pilots_list:
                licensed_pilots_id_list.append(pilot.getCrewID())

            qualified_crew_list = []

            # appends only pilots that are not working and have a specific license
            # appends all flight attendants that are not working
            for crew_member in not_working_list:
                if type(crew_member) == Pilot:
                    if crew_member.getCrewID() in licensed_pilots_id_list:
                        qualified_crew_list.append(crew_member)
                else:
                    qualified_crew_list.append(crew_member)
            
            return qualified_crew_list
        else:
            return None

    def appendNotWorkingCrewList(self,crew_instance_list,not_working_crew_id_list):
        #Checks if the crew memeber is in working list, if not, the crew member is added
        # to list of not working crew members
        for crew_member in crew_instance_list:
            crew_id = crew_member.getCrewID()
            if crew_id not in self.working_crew_id_list:
                not_working_crew_id_list.append(crew_id)


    def getWorkSchedule(self,start_date,end_date,crew_id):
        voyage_list = VoyageLL().getVoyageInDateRange(start_date,end_date)
        if voyage_list != None:
            work_schedule_list = []

            for voyage in voyage_list:
                crew_on_voyage_list = voyage.getCrewOnVoyage()
                for crew_member_id in crew_on_voyage_list:
                    if crew_member_id == crew_id:
                        work_schedule_list.append(voyage)
            if len(work_schedule_list) != 0:
                return work_schedule_list
            else:
                return None
        else:
            return None
    
