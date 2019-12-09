from API.LL_API import LL_API
from ModelClasses.destination_model import Destination

class DestinationUI:

    def showAllDestinations(self):
        '''Shows all destinations of NanAir'''
        destinations = LL_API().get_destinations()

        header_str = '{:<15}{:<15}{:<10}{:<12}{:<20}{:<12}'.format('Airport Code',
                                                                    'Destination',
                                                                    'Duration',
                                                                    'Distance',
                                                                    'Emergency Contact ',
                                                                    'Phone Number')
        print(header_str)
        print('-'*len(header_str))
        for destination in destinations:
            dest = destination.getDestinationName()
            code = destination.getDestinationAirport()
            distance = destination.getDestinationDistance()
            contact = destination.getDestinationContact()
            emergency_phone_number = destination.getDestinationEmergencyPhoneNumber()
            duration = destination.getDestinationDuration()
            

            format_str = '{:<15}{:<15}{:<10}{:<12}{:<15}{:>12}'.format(code,
                                                                        dest,
                                                                        duration,
                                                                        distance,
                                                                        contact,
                                                                        emergency_phone_number)
            
            print(format_str)
    
    
    def getOneDestination(self, dest_code):

        all_destinations = LL_API().get_destinations()

        for destination in all_destinations:
            if destination.getDestinationAirport() == dest_code:
                return destination
        else:
            return None

  
    def changeEmergencyContactName(self):

        airport_code = input('Enter airport code (IATA): ').upper()
        
        check = LL_API().checkDestInput(dest)
        
        while check == False:
            print('Please enter a valid destination!')
            dest = input().upper()
            check = LL_API().checkDestInput(dest)

        new_emergency_contact = input('Enter name of new emergency contact: ')

        destination_instance = self.getOneDestination(airport_code)
        destination_instance.setEmergencyContactName(new_emergency_contact)

        LL_API().changeEmergencyContact(destination_instance)

        print('\nNew Emergency Contact ({}) for {} has been saved.\n'.format(new_emergency_contact,
                                                                            destination_instance.getDestinationName()))


    def changeEmergencyContactPhoneNumber(self):
        
        airport_code = input('Enter airport code (IATA): ')
        new_emergency_phone = input('Enter new emergency phone number: ') 

        destination_instance = self.getOneDestination(airport_code)
        destination_instance.setEmergencyContactPhone(new_emergency_phone)

        LL_API().changeEmergencyContact(destination_instance)

        print('\nNew Emergency Phone Number ({}) for {} has been saved.\n'.format(new_emergency_phone,
                                                                                destination_instance.getDestinationName()))

    
    def addDestination(self):
        '''Gets information needed to add a new destination'''
        destination_airport = self.getDestinationAirport()
        destination_name = self.getDestinationName()
        destination_distance = self.getDistance()
        flight_duration_str = self.getDuration()
        emergency_contact_name = self.getEmergencyContactName()
        emergency_contact_phone = self.getDestinationEmergencyPhoneNumber()

        new_destination = Destination(destination_name,\
            destination_airport,flight_duration_str, \
                destination_distance,emergency_contact_name,\
                    emergency_contact_phone)
        
        LL_API().addDestination(new_destination)
        
        print('Destination successfully added!')


    def getDestinationName(self):
        while True:
            destination_name = input('Name of destination: ').capitalize()
            for letter in destination_name:
                if letter.isdigit():
                    print('Invalid destination name, please enter only letters!')
                    break
            else:
                return destination_name


    def getEmergencyContactName(self):
        while True:
            emergency_contact_name = input('Enter the emergency contact name: ').capitalize()
            for letter in emergency_contact_name:
                if letter.isdigit():
                    print('Invalid name, please enter only letters!')
                    break
            else:
                return emergency_contact_name


    def getDestinationAirport(self):
        '''Gets destination airport code from user'''
        while True:
            destination_airport = input('Destination airport code (3char airport code): ').upper()
            for letter in destination_airport:
                if letter.isdigit():
                    print('Invalid airport code!')
                    break
            else:
                if len(destination_airport) == 3:
                    return destination_airport
                else:
                    print('Invalid airport code')
    

    def getDuration(self):
        ''''Gets destination duration from user'''
        print('Enter flight duration')

        flight_duration_hours_str = input('Hours: ')
        flight_duration_minutes_str = input('Minutes: ')

        LL_API().verifyTime(flight_duration_hours_str,flight_duration_minutes_str)

        if len(flight_duration_minutes_str) == 1:
            flight_duration_str = flight_duration_hours_str + 'h0'+flight_duration_minutes_str + 'm'
        else:
            flight_duration_str = flight_duration_hours_str + 'h'+flight_duration_minutes_str + 'm'
            
        return flight_duration_str
    

    def getDistance(self):
        '''Gets destination distance from user'''
        while True:
            destination_distance = input('Distance in km: ')
            if self.checkIfInt(destination_distance):
                destination_distance += 'km'
                return destination_distance
            else:
                print('Invalid distance')
    
    def getDestinationEmergencyPhoneNumber(self):
        '''Gets the destination's emergency 
           contact's phone number from user'''
        while True:
            emergency_contact_phone = input("Enter the emergency contact's phone number: ")
            if self.checkIfInt(emergency_contact_phone):
                if len(emergency_contact_phone) == 7:
                    return emergency_contact_phone
                else:
                    print('Invalid phone number')
            else:
                print('Invalid phone number')


    def checkIfInt(self,a_str):
        try:
            int(a_str)
            return True
        except ValueError:
            return False




