from IO.destinationIO import DestinationIO
from IO.pilotIO import PilotIO
from IO.attendantIO import AttendantIO
from IO.voyageIO import VoyageIO
from IO.airplaneIO import AirplaneIO

from LL.crewLL import CrewLL


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
        return PilotIO().loadPilotFromFile()


    def changePilot(self, info):
        return PilotIO().changePilotInFile(info)


    def addPilot(self, new_employee_str):
        return PilotIO().addPilotToFile(new_employee_str)

    
    def loadFlightAttFromFile(self):
        return AttendantIO().loadFlightAttFromFile()


    def changeFlightAttInFile(self):
        return AttendantIO().changeFlightAttInFile()


    def addFlightAttToFile(self):
        return AttendantIO().addFlightAttToFile()


    def getFlightAttInputToAdd(self):
        return CrewLL().editFlightAttendant()

    def getAllStaff(self):
        return AttendantIO().read_file()


    # VOYAGES

    def loadVoyageFromFile(self):
        return VoyageIO().addVoyageToFile()


    def changeVoyageInFile(self):
        return VoyageIO().changeVoyageInFile()


    def addVoyageToFile(self):
        return VoyageIO().addVoyageToFile()


    # VOYAGE

    def loadAirplaneFromFile(self):
        return AirplaneIO().loadAirplaneFromFile()


    def changeAirplaneInFile(self):
        return AirplaneIO().change_airplane_in_file()


    def addAirplaneToFile(self):
        return AirplaneIO().add_airplane_to_file()
