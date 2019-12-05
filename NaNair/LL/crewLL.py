
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
        print(crew)
        while True:
            print('IN GET ONE CREW MENBER')
            for crew_member in crew:
                if crew_id == crew_member.getCrewID():
                    #print("inn í getOneCrewMember prentum crew_member: " , crew_member)
                    return crew_member
            else: 
                print('NOT A CREW MENBER')
                return None
 
    
    def getLicensedPilots(self, pilot_license):
        pilots = self.getPilots()

        licensedPilots = []

        for pilot in pilots:
            if pilot_license == pilot.getLicense():
                licensedPilots.append(pilot)
        
        return licensedPilots

    def makeInstance(info_list):
        '''Makes a pilot or flight attendant instance from list of data'''

        if len(PilotData) == 7:
            #crew member is pilot
            new_employee_instance = Pilot()
            new_employee_instance.setLicense( CrewData[CrewLL.LICENSE_const] )
            
            # rank placement
            if CrewData[ CrewLL.RANK_const ] == '1':
                new_employee_instance.setCaptain(True)
            else: 
                new_employee_instance.setCaptain(False)
        else: # if crew member is flight attendant
            new_employee_instance = FlightAttendant()

            # rank placement
            if CrewData[ CrewLL.RANK_const ] == '3':
                new_employee_instance.setHeadFlightAtt(True)
            else:
                new_employee_instance.setHeadFlightAtt(True)

            
            new_employee_instance.setName( CrewData[ CrewLL.NAME_const ] )
            new_employee_instance.setCrewID( CrewData[ CrewLL.SSN_const ] )
            new_employee_instance.setAddress( CrewData[ CrewLL.ADDRESS_const ] )
            new_employee_instance.setPhone( CrewData[ CrewLL.PHONENUMBER_const ] )
            new_employee_instance.setEmail( CrewData[ CrewLL.EMAIL_const ] )

            return new_employee_instance
 
    def addCrew(self, CrewData):
        ''' makes instance of crew member to add to file'''

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




    def ChangeHomeAddress(self,crew_id,new_home_address):
        '''Changes the home address of crew member'''
        employee = self.getOneCrewMember(crew_id)
        pilots = IO_API().loadPilotFromFile()
        flight_att = IO_API().loadFlightAttFromFile()
        new_employee_list = []

        for pilot in pilots:
            if employee == pilot:
                pilot.setAddress(new_home_address)
            new_employee_list.append(pilot)
        
        for attendant in flight_att:
            if employee == attendant:
                attendant.setAddress(new_home_address)
            new_employee_list.append(attendant)

        IO_API().changeCrewFile(new_employee_list)

    def ChangeEmailAddress(self,crew_id,new_email_address):
        '''Changes the email address of a crew member'''
        employee = self.getOneCrewMember(crew_id)
        pilots = IO_API().loadPilotFromFile()
        flight_att = IO_API().loadFlightAttFromFile()
        new_employee_list = []

        for pilot in pilots:
            if employee == pilot:
                pilot.setEmailAddress(new_email_address)
            new_employee_list.append(pilot)
        
        for attendant in flight_att:
            if employee == attendant:
                attendant.setEmailAddress(new_email_address)
            new_employee_list.append(attendant)

        IO_API().changeCrewFile(new_employee_list)



        # for i in range(len(self.employees_list)):
        #     if personal_id == self.employees_list[i][0]:
        #         self.employees_list[i][CrewLL.ADDRESS_const] = new_home_address  
        
        # IO_API().changeCrewFile(self.employees_list)

    def ChangePhonenumber(self,crew_id,new_phone_number):
        '''Changes the email address of a crew member'''
        employee = self.getOneCrewMember(crew_id)
        pilots = IO_API().loadPilotFromFile()
        flight_att = IO_API().loadFlightAttFromFile()
        new_employee_list = []

        for pilot in pilots:
            if employee == pilot:
                pilot.setPhonenumber(new_phone_number)
            new_employee_list.append(pilot)

        for attendant in flight_att:
            if employee == attendant:
                attendant.setPhonenumber(new_phone_numer)
            new_employee_list.append(attendant)

        IO_API().changeCrewFile(new_employee_list)
    
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
        
        working_crew_id_list = self.getWorkingCrewIdList(date_str)
        format_str = ''
        if working_crew_id_list != None:
            for working_crew_per_voyage in working_crew_id_list:
                destination_instance = working_crew_per_voyage[1]
                destination_name = destination_instance.getDestinationName()

                for crew_id in working_crew_per_voyage[0]:
                    if crew_id != 'empty':
                        crew_member = self.getOneCrewMember(crew_id)
                        format_str += '{:<20}{:<20}{:<20}{:<20}{:<20}\n'.format(crew_member.getName(),crew_id,crew_member.getAddress(),crew_member.getPhoneNumber(),destination_name)
            
            self.working_crew_id_list = working_crew_id_list

            return format_str
        else:
            return None


    def getWorkingCrewIdList(self,date_str):

        voyage_list = VoyageLL().getVoyageInDateRange(date_str,date_str)
        self.working_crew_id_list = []
        if voyage_list != None:
            for voyage in voyage_list:
                crew_on_voyage_list = voyage.getCrewOnVoyage()
                destination_of_voyage = voyage.getDestination()
                self.working_crew_id_list.append((crew_on_voyage_list,destination_of_voyage))

            if len(self.working_crew_id_list) != 0:
                return self.working_crew_id_list
            else:
                return None
        else:
            return None

    def getNotWorkingCrew(self,date_str):
        
        format_str = ''
        self.getWorkingCrew(date_str)
        not_working_crew_id_list = []

        flight_atts = IO_API().loadFlightAttFromFile()
        pilots = IO_API().loadPilotFromFile()

        self.appendNotWorkingCrewList(flight_atts,not_working_crew_id_list)
        self.appendNotWorkingCrewList(pilots,not_working_crew_id_list)
        if len(not_working_crew_id_list) != 0:
            for not_working_crew_id in not_working_crew_id_list:
                crew_member = self.getOneCrewMember(not_working_crew_id)
                format_str += '{:<20}{:<20}{:<20}{:<20}\n'.format(crew_member.getName(),not_working_crew_id,crew_member.getAddress(),crew_member.getPhoneNumber())
            
            return format_str
        else:
            return None


    def appendNotWorkingCrewList(self,crew_instance_list,not_working_crew_id_list):

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
    
