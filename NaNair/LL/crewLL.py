from API.IO_API import IO_API
from IO.pilotIO import PilotIO
from IO.attendantIO import AttendantIO

class CrewLL:
 
    def __init__(self):
        SSN_const = 0
        NAME_const = 1
        ROLE_const = 2
        RANK_const = 3
        LICENSE_const = 4
        ADDRESS_const = 5
        PHONENUMBER_const = 6
        EMAIL_const = 7

        self.employees_list = IO_API().readPilotFile()
        self.pilots_list = IO_API().loadPilotFromFile()

 
    def getCrew(self):
        ''' Gets the whole crew '''
        crew = IO_API().loadFlightAttFromFile()

        # format a crew lagað...

        return total_crew

 
    def getPilots(self):
        ''' Gets pilot from all the pilots (crew)'''
        pilots = IO_API().loadPilotFromFile()

        #format a pilots lagað...

        return pilots
        
 
    def addPilot(self, PilotData):
        ''' Adds pilot to pilots (crew)'''
        # input from UI layer is PilotData

        # Format a pilotData lagað...

        return IO_API().addPilot(PilotData)


 
    def editPilot(self, info):
        ''' Takes input from UI layer of info to edit, formats it and 
        sends to IO layer'''
        
        # format a info lagað ef þarf...

        return IO_API().addPilot(info)

    def ChangeEmailAddress(self,personal_id,new_email_address):
        '''Changes the email address of a single pilot'''
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][EMAIL_const] = new_email_address  

       #  change crew file in pilotIO changes the whole crew list
       PilotIO().changeCrewFile(self.employees_list)


    def ChangeHomeAddress(self,personal_id,new_home_address):
        '''Changes the Emergency Contact for destination in file'''
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][ADDRESS_const] = new_home_address  
        
        PilotIO().changeCrewFile(self.employees_list)

    def ChangePhoneNumber(self,personal_id,new_phone_number):
        '''Changes the Emergency Contact for destination in file'''
        for i in range(len(self.employees_list)):
            if personal_id == self.employees_list[i][0]:
                self.employees_list[i][PHONENUMBER_const] = new_phone_number
        
        PilotIO().changeCrewFile(self.employees_list)
    
    def ChangePilotLicense(self,personal_id,new_license):
        '''Changes the License of the pilot in file'''

        for i in range(len(self.pilots_list)):
            if personal_id == self.pilots_list[i][0]:
                self.pilots_list[i][LICENSE_const] = new_license
        
        PilotIO().changePilotFile(self.pilots_list)



    def addFlightAttendant(self):
        ''' Adds flight attendant to flight attendants (crew)'''
        info_to_add = LL_API().inputForNewFlightAtt()

        # format a info lagað...

        return info_to_add
 
    def editFlightAttendant(self):
        ''' Edits information of a flight attendant '''
        pass
 
    def getWorkingCrew(self):
        ''' Gets the working crew '''
        pass


class Crew:
    def __init__(self, name, crewID, address, landline, mobile, email):
        self.name = name
        self.crewID = crewID
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.email = email


class Pilot(Crew):
    def __init__(self, pilot_license, captain):
        self.pilotl_icense = pilot_license
        self.captain = captain
 
 
class FlightAttendant(Crew):
    def __init__(self, head_flight_att):
        self.head_flight_att = True