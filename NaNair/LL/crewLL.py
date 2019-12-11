
from API.IO_API import IO_API
from IO.crewIO import CrewIO
from LL.voyageLL import VoyageLL
from ModelClasses.flight_att_model import FlightAttendant
from ModelClasses.pilot_model import Pilot
from LL.airplaneLL import AirplaneLL
import datetime

class CrewLL:

    
    ROLE_const = 2
    RANK_const = 3
    LICENSE_const = 4

    def getCrew(self):
        ''' Returns a list of class instances for all crew '''
        return IO_API().loadCrewFromFile()

    def getPilots(self):
        ''' Gets a list of pilot instances '''
        crew_list = self.getCrew()
        pilot_list = []

        # Iterates through a list of all crew members 
        # and appends the pilots to pilot list
        for employee in crew_list:
            if type(employee) == Pilot:
                pilot_list.append(employee)

        return pilot_list
    
    
    def getFlightAtt(self):
        ''' Gets a list of flight 
        attendants instances '''
        crew_list = self.getCrew()
        flight_att_list = []

        # Iterates through a list of all crew members 
        # and appends the flight attendants to flith attendants list
        for employee in crew_list:
            if type(employee) == FlightAttendant:
                flight_att_list.append(employee)
        
        return flight_att_list


    

    def getOneCrewMember(self,input_crew_id):
        ''' Returns a crew member instance
        which holds given ID number, returns None if 
        the crew member isn't found'''

        crew = self.getCrew()
        # Iterates through a list of all crew members 
        # and finds member with given ID

        while True:
            for crew_member in crew:
                crew_id = crew_member.getCrewID()
                if input_crew_id == crew_id:
                    return crew_member
            else: 
                return None
 
    
    def getLicensedPilots(self, pilot_license):
        '''Takes in a pilot license and finds all pilots 
        who have the inputted license.
        Returns a list of pilot instances'''

        pilots_instances_list = self.getPilots()
        licensedPilots = []

        # Checks all pilots if they have inputted license. 
        # If they do they are added to a list
        for pilot in pilots_instances_list:
            if pilot_license == pilot.getLicense():
                licensedPilots.append(pilot)
        
        return licensedPilots
 
 
    def addCrew(self, CrewData):
        '''Takes in a list of data and formats 
        it to a string to add to file.'''

        # Add necessary data that can be found from user input

        # If 'Captain' was selected in UI layer
        if CrewData[self.ROLE_const] == '1': 
            CrewData.insert(self.ROLE_const, 'Pilot')
            CrewData[self.RANK_const] = '1'

        # If 'Copilot' was selected in UI layer
        elif CrewData[self.ROLE_const] == '2':
            CrewData.insert(self.ROLE_const, 'Pilot')
            CrewData[self.RANK_const] = '0'

        # If 'Head service manager' was selected in UI layer
        elif CrewData[self.ROLE_const] == '3':
            CrewData.insert(self.ROLE_const, 'Cabincrew')
            CrewData.insert(self.LICENSE_const, 'N/A')
            CrewData[self.RANK_const] = '1'
        
        # If 'Flight Attendant' was selected in UI layer
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
        '''Sorts all pilots by their license, 
        returns a list of sorted pilots'''

        pilot_list = self.getPilots()
        sorted_pilots_list = []

        licenses = set()
        # Make a set of all licenses to iterate through
        for pilot in pilot_list:
            licenses.add(pilot.getLicense())

        # Checks if a pilot has a specific license and append them to a list if so  
        for a_license in licenses:
            for pilot in pilot_list:
                if pilot.getLicense() == a_license:
                    sorted_pilots_list.append(pilot)
        
        return sorted_pilots_list
 
    def doesIDExist(self, crew_id):
        '''Checks if a crew member already exists 
        (the inputted id is taken). Returns true if so, else false'''

        crew_instance_list = IO_API().loadCrewFromFile()
        BoolCheck = False

        for crew_member in crew_instance_list:
            if crew_member.getCrewID() == crew_id:
                BoolCheck = True
        
        return BoolCheck


    def getWorkingCrew(self,datetime_object):
        ''' Returns a list of tuples where each tuple 
        is a working crew member and the destination he's going to'''
        
        working_crew_list = []

        # Gets a list of tuples where each tuple is a list of IDs for the 
        # people working on a voyage that on inputted date and 
        # the destination they're going to

        working_crew_voyage_info_list = self.getWorkingCrewIdList(datetime_object)


        if working_crew_voyage_info_list != None:
            for working_crew_per_voyage_info in working_crew_voyage_info_list:
                destination_instance = working_crew_per_voyage_info[1]
                destination_name = destination_instance.getDestinationName()

                for crew_id in working_crew_per_voyage_info[0]:
                    if crew_id != 'empty':
                        crew_member = self.getOneCrewMember(crew_id)
                        working_crew_list.append((crew_member,destination_name))
            
            return working_crew_list

        # If no one is working on the inputted date
        else:
            return None


    def getWorkingCrewIdList(self,datetime_object):
        '''Takes in a date and returns a list of tuples where each tuple is
        a list of IDs for the people working on a voyage that day and 
        the destination they're going to'''

        # Voyages on a specific date:
        voyage_list = VoyageLL().getVoyageInDateRange(datetime_object,datetime_object)
        self.working_crew_voyage_info_list = []
        
        # Iterates through voyages on a specific date and adds the IDs of working crew 
        # to list as well as the voyage destination
        if voyage_list != None:
            for voyage in voyage_list:
                crew_on_voyage_list = voyage.getCrewOnVoyage()
                destination_of_voyage = voyage.getDestination()
                self.working_crew_voyage_info_list.append((crew_on_voyage_list,destination_of_voyage))

            if len(self.working_crew_voyage_info_list) != 0:
                return self.working_crew_voyage_info_list
            # If no crew was assigned to the voyages
            else:
                return None
        # If there are no voyages on a chosen date
        else:
            return None


    def getNotWorkingCrew(self,datetime_object):
        '''Gets a list of instances of crew members
           that are not working on a specific day'''
        # Gets a list of tuples where each tuple is a crew 
        # instance and the destination they're going to
        working_crew_info_list = self.getWorkingCrew(datetime_object)

        working_crew_id_list = []
        not_working_crew_list = []
        all_crew = IO_API().loadCrewFromFile()

        if working_crew_info_list:
            # Gets a list of all id's of the working crew
            for crew_member, destination in working_crew_info_list:
                working_crew_id_list.append(crew_member.getCrewID())

            # Checks if the crew memeber is in the working list, 
            # if not, the crew member is added to list of not 
            # working crew members

            for crew_member in all_crew:
                if crew_member.getCrewID() not in working_crew_id_list:
                    not_working_crew_list.append(crew_member)

            return not_working_crew_list
        
        else:
            # All crew members are available if
            # workin_crew_info_list is empty
            return all_crew

    def getQualifiedCrew(self, depart_time, plane_insignia):
        '''Returns a list of crew instances that is both qualified for a specific plane 
        and is not working'''

        plane_instance = AirplaneLL().getAirplanebyInsignia(plane_insignia)
        plane_license = plane_instance.get_planeTypeID()

        
        depart_datetime = AirplaneLL().revertDatetimeStrtoDatetime(depart_time)

        not_working_list = self.getNotWorkingCrew(depart_datetime)
        licensed_pilots_list = self.getLicensedPilots(plane_license)

        if len( licensed_pilots_list ) != 0:
            licensed_pilots_id_list = []

            for pilot in licensed_pilots_list:
                licensed_pilots_id_list.append(pilot.getCrewID())

            qualified_crew_list = []

            # Appends only pilots that are not working and have a specific license
            # Appends all flight attendants that are not working
            for crew_member in not_working_list:
                if type(crew_member) == Pilot:
                    if crew_member.getCrewID() in licensed_pilots_id_list:
                        qualified_crew_list.append(crew_member)
                else:
                    qualified_crew_list.append(crew_member)
            
            return qualified_crew_list
        else:
            return None


    # Erum við að nota?
    # def appendNotWorkingCrewList(self,crew_instance_list,not_working_crew_id_list):
    #     '''Checks if the crew member is in the working list, if not, the crew member is added
    #     to list of not working crew members'''

    #     for crew_member in crew_instance_list:
    #         crew_id = crew_member.getCrewID()
    #         if crew_id not in self.working_crew_voyage_info_list:
    #             not_working_crew_id_list.append(crew_id)


    def getWorkSchedule(self,start_date,end_date,crew_id):
        '''Gets a work schedule list with all voyage instances
        for an employee in a specific date range. 
        Returns None if the employee has no voyages in the date range'''

        voyage_list = VoyageLL().getVoyageInDateRange(start_date,end_date)

        if voyage_list != None:
            work_schedule_list = []

            # Go through all the voyages and check
            # if the crew member is working
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
    
