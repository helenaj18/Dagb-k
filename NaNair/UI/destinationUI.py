from API.LL_API import LL_API

class DestinationUI:

    def showAllDestinations(self):
        '''Shows all destinations of NanAir'''
        destinations = LL_API().get_destinations()

        header_str = '{:<15}{:<15}{:<10}{:<12}{:<20}{:<12}'.format('Airport Code','Destination','Duration','Distance','Emergency Contact ','Phone Number')
        print(header_str)
        print('-'*len(header_str))
        for destination in destinations:
            dest = destination.getDestinationName()
            code = destination.getDestinationAirport()
            distance = destination.getDestinationDistance()
            contact = destination.getDestinationContact()
            emergency_phone_number = destination.getDestinationEmergencyPhoneNumber()
            duration = destination.getDestinationDuration()
            

            format_str = '{:<15}{:<15}{:<10}{:<12}{:<15}{:>12}'.format(code,dest,duration,distance,contact,emergency_phone_number)
            print(format_str)



