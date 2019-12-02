# velkomin 

# UI LAYER 

class CrewUI:

    def __init__(self):
        pass

    def __str__(self):
        pass 
    
    def show_crew(self):
        '''' Shows full list of crew, pilots and flight attendants'''
        pass

    def show_working_crew(self):
        ''' Shows full list of working crew atm '''        
        pass

    def show_all_pilots(self):
        ''' Shows full list of pilots regestered'''
        pass

    def show_one_pilot(self, pilot_ID):
        ''' Shows details for a specific pilot'''
        pass 

    def show_by_licence(self, licence_ID):
        ''' Shows a list of pilots by their licence '''
        pass

    def show_all_flight_att(self):
        ''' Shows a full list of all pilots regestered''' 
        pass
  
    def show_one_flight_att(self, flight_att_ID):
        ''' Shows details for a specific flight attendant'''
        pass

    def show_scedule(self, flight_att_ID):
        ''' Shows the scedule for a specific flight attendant '''
        pass

class DestinationUI:

    def __init__(self):
        pass

    def __str__(self):
        pass 

    def show_all_destinations(self):
        '''Shows all destinations of NanAir'''
        pass

    def show_one_destination(self,destination_ID):
        '''Shows information about one destination'''
        pass


class AirplaneUI:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def show_all_planes(self):
        '''Shows information about all airplanes NanAir owns'''
        pass

    def show_one_plane(self, plane_ID):
        '''Shows information about one specific airplane'''
        pass



class VoyageUI:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def show_all_voyages(self,time_period_str):
        '''Shows all voyages for a current time period'''
        pass

    def show_one_voyage(self,voyage_ID):
        '''Shows one specific voyage'''
        pass


# LOGIC LAYER

class DestinationLL:
    def __init__(self):
        pass
 
    def get_destination(self):
        ''' Gets destination from Destination class'''
        pass
 
 
class CrewLL:
 
    def __init__(self):
        pass
 
    def get_crew(self):
        ''' Gets the whole crew '''
        pass
 
    def get_pilots(self):
        ''' Gets pilot from all the pilots (crew)'''
        pass
 
    def add_pilot(self):
        ''' Adds pilot to pilots (crew)'''
        pass
 
    def edit_pilot(self):
        ''' Edits information of a pilot '''
        pass
 
    def add_flight_attendant(self):
        ''' Adds flight attendant to flight attendants (crew)'''
        pass
 
    def edit_flight_attendant(self):
        ''' Edits information of a flight attendant '''
        pass
 
    def get_working_crew(self):
        ''' Gets the working crew '''
        pass

class VoyageLL:
    ''' LL class for voyage '''
    def __init__(self, voyage,voyageIO):
        self.voyage = voyage
        self.voyageIO = voyageIO
        pass
 
    def get_voyage(self,ID):
        pass
 
    def add_voyage(self):
        pass
 
 
class AirplaneLL:
    ''' LL class for airplane '''
    def __init__(self, airplane, airplaneIO):
        self.airplane = airplane
        self.airplaneIO = airplaneIO
 
    def get_airplanes(self):
        pass
   
    def add_airplane(self):
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
        



# IO LAYER 

class DestinationIO:
    def __init__(self, filename):
        self.__destination_filename = filename

    def load_destination_from_file(self):
        '''Fetches destination from a file'''
        pass

    def change_destination_from_file(self):
        '''Change the destination or other destination info in file'''
        pass

    def add_destination_from_file(self):
        '''Adds the destination into file'''
        pass


class PilotIO:
    def __init__(self, filename):
        self.__pilot_filename = filename
    
    def load_pilot_from_file(self):
        '''Fetches pilot info from file'''
        pass

    def change_pilot_from_file(self):
        '''Change pilot info in file'''
        pass

    def add_pilot_from_file(self):
        '''Add pilot info into file'''
        pass

class AttendantIO:

    def __init__(self, filename):
        self.__flight_att_filename = filename

    def load_flight_att_from_file(self):
        '''Gets info of flight attendant from file'''
        pass

    def change_flight_att_from_file(self):
        '''Changes the info of flight attendant'''
        pass

    def add_flight_att_from_file(self):
        '''Adds flight attendant info into file'''
        pass


class AirplaneIO:

    def __init__(self,filename):
        self.__airplane_filename = filename

    def load_airplane_from_file(self):
        '''Loads existing airplanes from the file'''
        pass

    def change_airplane_from_file(self):
        '''Changes an existing airplane in the file'''
        pass

    def add_airplane_from_file(self):
        '''Adds a new airplane to the file'''
        pass


class VoyageIO:

    def __init__(self,filename):
        self.__voyage_filename = filename

    def load_voyage_from_file(self):
        '''Loads existing voyages from the file'''
        pass

    def change_voyage_from_file(self):
        '''Changes an existing voyage in the file'''
        pass

    def add_voyage_from_file(self):
        '''Adds a new voyage to the file'''
        pass