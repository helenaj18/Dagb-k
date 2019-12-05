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
        for crew_member in crew:
            if crew_id == crew_member.getCrewID():
                return crew_member
 
    def getOnePilotID(self, pilotID):
        ''' Gets pilot from all the pilots (crew)'''
        pilots = self.getPilots()

        for pilot in pilots:
            if pilotID == pilot.getCrewID():
                return pilot
    
    def getOneFlightAttID(self, flight_att_id):
        flight_att = self.getFlightAtt()

        for one_att in flight_att:
            if flight_att_id == one_att.getCrewID():
                return one_att
    
    def getLicensedPilots(self, pilot_license):
        pilots = self.getPilots()

        licensedPilots = []

        for pilot in pilots:
            if pilot_license == pilot.getLicense():
                licensedPilots.append(pilot)
        
        return licensedPilots

        
 
    def addPilot(self, PilotData):
        ''' Adds pilot to pilots (crew)'''
        # input from UI layer is PilotData

        # Format a pilotData lagað...

        return IO_API().addPilot(PilotData)


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


    def addFlightAttendant(self, info):
        ''' Adds flight attendant to flight attendants (crew)'''
        #tekur input fra UI

        # format a info lagað...

        return IO_API().addFlightAttToFile(info)
 
 
    def getWorkingCrew(self,date_str):
        ''' Gets the working crew '''
        # pilots = IO_API().loadPilotFromFile()
        # flight_atts = IO_API().loadFlightAttFromFile()
        # crew = pilots + flight_atts
        voyage_list = VoyageLL().getVoyage(date_str,date_str)
        working_crew_list = []

        for voyage in voyage_list:
            crew_on_voyage_list = voyage.getCrewOnVoyage()
            working_crew_list.append(crew_on_voyage_list)

        return working_crew_list
    

