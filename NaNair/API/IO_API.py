from IO.destinationIO import DestinationIO
from IO.crewIO import CrewIO
from IO.voyageIO import VoyageIO
from IO.airplaneIO import AirplaneIO


class IO_API:
    '''API class for IO'''

    # DESTINATION 

    def loadDestinationFromFile(self):
        return DestinationIO().loadDestinationFromFile()

    def changeEmergencyPhone(self,destination_name,new_emergency_contact):
        return DestinationIO.changeEmergencyPhone()

    def changeEmergencyContact(self,destination_name,new_emergency_phone):
        return DestinationIO.changeEmergencyContact()

    def addDestinationToFile(self):
        return DestinationIO.addDestinationToFile()


    #CREW

    def loadPilotFromFile(self):
        return CrewIO().loadPilotFromFile()


    def changeCrewFile(self, info):
        return CrewIO().changeCrewFile(info)


    def addPilot(self, new_employee_str):
        return CrewIO().addPilotToFile(new_employee_str)

    
    def loadFlightAttFromFile(self):
        return CrewIO().loadFlightAttFromFile()



    def addFlightAttToFile(self, new_employee_str):
        return CrewIO().addFlightAttToFile(new_employee_str)


    def getAllStaff(self):
        return CrewIO().read_file()


    # VOYAGES

    def loadVoyageFromFile(self):
        return VoyageIO().loadVoyageFromFile()
    
    def read_file(self):
        return VoyageIO().read_file()


    def changeVoyageInFile(self):
        return VoyageIO().changeVoyageInFile()


    def addVoyageToFile(self,new_voyage_str):
        return VoyageIO().addVoyageToFile(new_voyage_str)


    # VOYAGE

    def loadAirplaneFromFile(self):
        return AirplaneIO().loadAirplaneFromFile()


    def changeAirplaneInFile(self):
        return AirplaneIO().change_airplane_in_file()


    def addAirplaneToFile(self):
        return AirplaneIO().add_airplane_to_file()
