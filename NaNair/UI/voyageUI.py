from API.LL_API import LL_API

class VoyageUI:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def showAllVoyages(self): # BÆTA INN EH TIME PERIOD
        '''Shows all voyages for a current time period'''
        return LL_API().get_all_voyages()

    def showOneVoyage(self,voyage_ID):
        '''Shows one specific voyage'''
        pass
