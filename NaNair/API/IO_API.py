from IO.destinationIO import DestinationIO
from IO.crewIO import CrewIO
from IO.voyageIO import VoyageIO
from IO.airplaneIO import AirplaneIO


class IO_API:
    '''API class for IO'''

    # DESTINATION 

    def loadDestinationFromFile(self):
        '''Returns an instance list of all destinations'''
        return DestinationIO().loadDestinationFromFile()

    def changeDestinationFile(self,destination):
        '''Inserts a changed instance into file'''
        return DestinationIO().changeDestinationFile(destination)

    def addDestinationToFile(self,new_destination):
        '''Adds new destination into file'''
        return DestinationIO().addDestinationToFile(new_destination)


    #CREW

    def loadCrewFromFile(self):
        '''Returns an instance list of all crew members'''
        return CrewIO().loadCrewFromFile()

    def changeCrewInfo(self,employee):
        '''Inserts a changed instance into file'''
        return CrewIO().changeCrewFile(employee)
    
    def addCrew(self, new_employee_str):
        '''Adds new crew member into file'''
        return CrewIO().addCrewToFile(new_employee_str)
 



    # VOYAGES

    def loadVoyageFromFile(self):
        '''Returns an instance list of all voyages'''
        return VoyageIO().loadVoyageFromFile()
    

    def changeVoyageFile(self,voyage):
        '''Inserts a changed instance into file'''
        return VoyageIO().changeVoyageFile(voyage)


    def addVoyageToFile(self,new_voyage_str):
        '''Adds new voyage into file'''
        return VoyageIO().addVoyageToFile(new_voyage_str)


    # AIRPLANE

    def loadAirplaneFromFile(self):
        '''Returns an instance list of all airplanes'''
        return AirplaneIO().loadAirplaneFromFile()


    def changeAirplaneInFile(self):
        '''Inserts a changed instance into file'''
        return AirplaneIO().change_airplane_in_file()


    def addAirplaneToFile(self,planeInsignia,planeTypeId,manufacturer,seats):
        '''Adds new airplane into file'''
        return AirplaneIO().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)
