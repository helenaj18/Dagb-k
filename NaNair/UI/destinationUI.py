class DestinationUI:

    def __init__(self):
        pass

    def __str__(self):
        pass 

    def showAllDestinations(self):
        '''Shows all destinations of NanAir'''
        
        print(LL_API().get_destination())

