from API.LL_API import LL_API

class DestinationUI:

    def __init__(self):
        pass

    def __str__(self):
        pass 

    def showAllDestinations(self):
        '''Shows all destinations of NanAir'''
        destinations = LL_API().get_destinations()
        for item in destinations:
            print(item)

