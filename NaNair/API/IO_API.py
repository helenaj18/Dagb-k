from IO.destinationIO import DestinationIO
from IO.pilotIO import PilotIO
from IO.attendantIO import AttendantIO
from IO.voyageIO import VoyageIO
from IO.airplaneIO import AirplaneIO

from LL.crewLL import CrewLL


class IO_API:
    '''API class for IO'''

    def loadDestinationFromFile(self):
        return DestinationIO().loadDestinationFromFile()


    def changeEmergencyPhone(self,destination_name,new_emergency_contact):
        return DestinationIO.changeEmergencyPhone()

    def changeEmergencyContact(self,destination_name,new_emergency_phone):
        return DestinationIO.changeEmergencyContact()

    def addDestinationToFile(self):
        return DestinationIO.addDestinationToFile()


    def loadPilotFromFile(self):
        return PilotIO().loadPilotFromFile()


    def changePilotInFile(self):
        return PilotIO().changePilotInFile()


    def getPilotInputToAdd(self):
        return CrewLL().addPilot()
    
    def gefPilotInputToEdit(self):
        return CrewLL().editPilot()

    def addPilotToFile(self, new_employee_str):
        return PilotIO().addPilotToFile(new_employee_str)

    
    def loadFlightAttFromFile(self):
        return AttendantIO().loadFlightAttFromFile()


    def changeFlightAttInFile(self):
        return AttendantIO().changeFlightAttInFile()


    def addFlightAttToFile(self):
        return AttendantIO().addFlightAttToFile()


    def getFlightAttInputToAdd(self):
        return CrewLL().editFlightAttendant()


    def loadVoyageFromFile(self):
        return VoyageIO().addVoyageToFile()


    def changeVoyageInFile(self):
        return VoyageIO().changeVoyageInFile()


    def addVoyageToFile(self):
        return VoyageIO().addVoyageToFile()


    def loadAirplaneFromFile(self):
        return AirplaneIO().load_airplane_from_file()


    def changeAirplaneInFile(self):
        return AirplaneIO().change_airplane_in_file()


    def addAirplaneToFile(self):
        return AirplaneIO().add_airplane_to_file()
