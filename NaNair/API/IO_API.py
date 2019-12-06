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
    
    def loadFlightAttFromFile(self):
        return CrewIO().loadFlightAttFromFile()


    def changeCrewFile(self,new_employee_list):
        return CrewIO().changeCrewFile(new_employee_list)


    def addPilot(self, new_employee_str):
        return CrewIO().addPilotToFile(new_employee_str)

    
    def addCrew(self, new_employee_str):
        return CrewIO().addCrewToFile(new_employee_str)
 

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


    def addAirplaneToFile(self,planeInsignia,planeTypeId,manufacturer,seats):
        return AirplaneIO().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)
