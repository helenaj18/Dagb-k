from IO.destinationIO import DestinationIO
from IO.pilotIO import PilotIO
from IO.attendantIO import AttendantIO
from IO.voyageIO import VoyageIO
from IO.airplaneIO import AirplaneIO


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


    def addPilotToFile(self):
        return PilotIO().addPilotToFile()

    
    def loadFlightAttFromFile(self):
        return AttendantIO().loadFlightAttFromFile()


    def changeFlightAttInFile(self):
        return AttendantIO().changeFlightAttInFile()


    def addFlightAttToFile(self):
        return AttendantIO().addFlightAttToFile()


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
