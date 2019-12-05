#from API.IO_API import IO_API
from API.IO_API import IO_API
from IO.crewIO import CrewIO
from LL.voyageLL import VoyageLL

class CrewLL:

    SSN_const = 0
    NAME_const = 1
    ROLE_const = 2
    RANK_const = 3
    LICENSE_const = 4
    ADDRESS_const = 5
    PHONENUMBER_const = 6
    EMAIL_const = 7

    def __init__(self):

        self.employees_list = IO_API().getAllStaff()
        self.pilots_list = IO_API().loadPilotFromFile()

 
    def getPilots(self):
        ''' Gets the pilots '''

        return IO_API().loadPilotFromFile()
    
    
    def getFlightAtt(self):
        ''' Gets the flight attendants '''

        return IO_API().loadFlightAttFromFile()


    def getCrew(self):
        ''' Gets the whole crew '''

        pilots = self.getPilots()
        flight_att = self.getFlightAtt()

        return pilots + flight_att
    
    def getOneCrewMember(self,crew_id):
        crew = self.getCrew()
        while True:
            for crew_member in crew:
                if crew_id == crew_member.getCrewID():
                    return crew_member
            else: 
                return None
 
    
    def getLicensedPilots(self, pilot_license):
        pilots = self.getPilots()

        licensedPilots = []

        for pilot in pilots:
            if pilot_license == pilot.getLicense():
                licensedPilots.append(pilot)
        
        return licensedPilots

 
    def addCrew(self, CrewData):
        ''' makes string of crew member to add to file'''

        if CrewData[2] == '1':
            CrewData.insert(CrewLL.ROLE_const, 'Pilot')
            CrewData[CrewLL.RANK_const] = '1'

        elif CrewData[2] == '2':
            CrewData.insert(CrewLL.ROLE_const, 'Pilot')
            CrewData[CrewLL.RANK_const] = '0'
        
        elif CrewData[2] == '3':
            CrewData.insert(CrewLL.ROLE_const, 'Cabincrew')
            CrewData.insert(CrewLL.LICENSE_const, 'N/A')
            CrewData[CrewLL.RANK_const] = '1'
        
        else:
            CrewData.insert(CrewLL.ROLE_const, 'Cabincrew')
            CrewData.insert(CrewLL.LICENSE_const, 'N/A')
            CrewData[CrewLL.RANK_const] = '0'


        new_employee_str = ','.join(CrewData)

        return IO_API().addCrew(new_employee_str)


    def ChangeEmailAddress(self,personal_id,new_email_address):
        '''Changes the email address of a single pilot'''
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][CrewLL.EMAIL_const] = new_email_address  

        #  change crew file in pilotIO changes the whole crew list
        IO_API().changeCrewFile(self.employees_list)


    def ChangeHomeAddress(self,personal_id,new_home_address):
        '''Changes the Emergency Contact for destination in file'''
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][CrewLL.ADDRESS_const] = new_home_address  
        
        IO_API().changeCrewFile(self.employees_list)

    def ChangePhoneNumber(self,personal_id,new_phone_number):
        '''Changes the Emergency Contact for destination in file'''
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][CrewLL.PHONENUMBER_const] = new_phone_number
        
        IO_API().changeCrewFile(self.employees_list)
    
    def ChangePilotLicense(self,personal_id,new_license):
        '''Changes the License of the pilot in file'''

        for i in range(len(self.pilots_list)):
            if personal_id == self.pilots_list[i][0]:
                if self.pilots_list[i][CrewLL.LICENSE_const] != 'N/A':
                    self.pilots_list[i][CrewLL.LICENSE_const] = new_license
                else:
                    print('Not a pilot!')
        
        IO_API().changeCrewFile(self.pilots_list)

    def sortPilotsByLicense(self):
        '''Sorts all pilots by their license'''

        pilot_list = self.getPilots()
        sorted_pilots_list = []

        licenses = set()
        # make a set of all licenses to iterate through
        for pilot in pilot_list:
            licenses.add( pilot.getLicense())

        for a_license in licenses:
            for pilot in pilot_list:
                if pilot.getLicense() == a_license:
                    sorted_pilots_list.append(pilot)
        
        return sorted_pilots_list
 
 
    def getWorkingCrew(self,date_str):
        ''' Gets the working crew '''
        # pilots = IO_API().loadPilotFromFile()
        # flight_atts = IO_API().loadFlightAttFromFile()
        # crew = pilots + flight_atts
        voyage_list = VoyageLL().getVoyageInDateRange(date_str,date_str)
        working_crew_list = []
        format_str = ''

        for voyage in voyage_list:
            crew_on_voyage_list = voyage.getCrewOnVoyage()
            destination_of_voyage = voyage.getDestination()
            working_crew_list.append((crew_on_voyage_list,destination_of_voyage))
        
        self.working_crew_list = working_crew_list

    def getFormatString(self,date_str):

        self.getWorkingCrew(date_str)
        
        for working_crew_per_voyage in self.working_crew_list:
            destination_instance = working_crew_per_voyage[1]
            destination_name = destination_instance.getDestinationName()

            for crew_id in working_crew_per_voyage[0]:
                if crew_id != 'empty':
                    crew_member = self.getOneCrewMember(crew_id)
                    crew_name = crew_member.getName()
                    crew_address = crew_member.getAddress()
                    crew_phone = crew_member.getPhoneNumber()
                    format_str += '{:<20}{:<20}{:<20}{:<20}{:<20}\n'.format(crew_name,crew_id,crew_address,crew_phone,destination_name)
    

