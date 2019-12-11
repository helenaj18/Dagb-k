from API.LL_API import LL_API
from ModelClasses.destination_model import Destination
import string

class DestinationUI:

    def showAllDestinations(self):
        '''Shows all destinations of NanAir'''

        # Gets a list of all destination instances 
        destinations = LL_API().get_destinations()

        header_str = '\n{:<15}{:<15}{:<10}{:<12}{:<20}{:<12}'.format('Airport Code',
                                                                    'Destination',
                                                                    'Duration',
                                                                    'Distance',
                                                                    'Emergency Contact ',
                                                                    'Phone Number')
        print(header_str)
        print('-'*len(header_str))

        # Go through all destination instances and print them
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
        '''Gets one destination by destination code '''

        all_destinations = LL_API().get_destinations()

        for destination in all_destinations:
            if destination.getDestinationAirport() == dest_code:
                return destination
        else:
            return None

  
    def changeEmergencyContactName(self):
        '''Changes emergency contact name'''

        print()
        airport_code = input('Enter airport code (IATA - 3 letters): ').upper().strip()
        
        # Verifies if the airport code is valid
        check = LL_API().checkDestInput(airport_code)   
        
        while check == False:
            print('Please enter a valid destination!')
            airport_code = input('Enter airport code (IATA - 3 letters): ').upper().strip()
            # Verifies if the airport code is valid
            check = LL_API().checkDestInput(airport_code) 

        # Gets new emergency contact name and verifies the input at the same time
        new_emergency_contact = self.getEmergencyContactName()  
        destination_instance = self.getOneDestination(airport_code)
        destination_instance.setEmergencyContactName(new_emergency_contact)

        LL_API().changeEmergencyContact(destination_instance)

        print('\nNew Emergency Contact ({}) for {} has been saved.\n'.format(new_emergency_contact,
                                                                            destination_instance.getDestinationName()))


    def changeEmergencyContactPhoneNumber(self):
        '''Changes emergency contact phone number'''

        print()
        airport_code = input('Enter airport code (IATA - 3 letters): ').strip()

        # Verifies if the airport code is valid
        check = LL_API().checkDestInput(airport_code) 

        while check == False:
            print('Please enter a valid destination!')
            airport_code = input('Enter airport code (IATA - 3 letters): ').upper().strip()
            # Verifies if the airport code is valid
            check = LL_API().checkDestInput(airport_code)   
        
        # Gets new emergency phone number and verifies the input at the same time
        new_emergency_phone = self.getDestinationEmergencyPhoneNumber() 
        destination_instance = self.getOneDestination(airport_code)
        destination_instance.setEmergencyContactPhone(new_emergency_phone)

        LL_API().changeEmergencyContact(destination_instance)

        print('\nNew Emergency Phone Number ({}) for {} has been saved.\n'.format(new_emergency_phone,
                                                                                destination_instance.getDestinationName()))

    
    def addDestination(self):
        '''Gets information needed to add a new destination'''

        print()
        destination_airport = self.getDestinationAirport()
        destination_name = self.getDestinationName()
        destination_distance = self.getDistance()
        flight_duration_str = self.getDuration()
        emergency_contact_name = self.getEmergencyContactName()
        emergency_contact_phone = self.getDestinationEmergencyPhoneNumber()

        # Make a destination instance
        new_destination = Destination(destination_name,\
            destination_airport,flight_duration_str, \
                destination_distance,emergency_contact_name,\
                    emergency_contact_phone)
        
        LL_API().addDestination(new_destination)

        print()
        print('~'*45)
        print('{:^45}'.format('Destination successfully added!')) 
        print('~'*45)


    def getDestinationName(self):
        '''Gets a name of a destination from user'''

        while True:
            destination_name = input('Name of destination: ').capitalize().strip()
            for letter in destination_name:
                # The destination name can't have digits
                if letter.isdigit() or letter in string.punctuation:
                    print('\nInvalid destination name, please enter only letters!\n')
                    break
            else:
                if len(destination_name) != 0:
                    return destination_name
                else:
                    print('\nThe destination name is required!\n')


    def getEmergencyContactName(self):
        '''Gets emergency contact name from user'''

        while True:
            emergency_contact_name = input('Enter the emergency contact name: ').capitalize().strip()
            for letter in emergency_contact_name:
                # The emergency contact name can't have 
                # digits or a punctuation
                if letter.isdigit() or letter in string.punctuation:
                    print('Invalid name, please enter only letters!')
                    break
            else:
                if emergency_contact_name != '':
                    return emergency_contact_name
                else:
                    print('\nThe name is required!\n')


    def getDestinationAirport(self):
        '''Gets destination airport code from user'''
        
        while True:
            destination_airport = input('Destination airport code (3char airport code): ').upper().strip()

            # Checks if the destination already exists
            check = LL_API().checkDestInput(destination_airport)
            
            if check == False:
                for letter in destination_airport:
                    # The airport code can't contain 
                    # digits or a punctuation
                    if letter.isdigit() or letter in string.punctuation:
                        print('\nInvalid airport code!\n')
                        break
                else:
                    if len(destination_airport) == 3:
                        return destination_airport
                    else:
                        print('\nInvalid airport code\n')
            else:
                print('\nDestination already exists!\n')
    

    def getDuration(self):
        ''''Gets destination duration from user'''

        print('Enter flight duration')

        flight_duration_hours_str = input('Hours: ').strip()
        flight_duration_minutes_str = input('Minutes: ').strip()

        # Verifies if the date is valid
        LL_API().verifyTime(flight_duration_hours_str,flight_duration_minutes_str)

        # If the minute string is of length 1, add an extra 0
        if len(flight_duration_minutes_str) == 1:
            flight_duration_str = flight_duration_hours_str + 'h0'+flight_duration_minutes_str + 'm'
        else:
            flight_duration_str = flight_duration_hours_str + 'h'+flight_duration_minutes_str + 'm'
            
        return flight_duration_str
    

    def getDistance(self):
        '''Gets destination distance from user'''

        while True:
            destination_distance = input('Distance in km: ').strip()
            if self.checkIfInt(destination_distance):
                destination_distance += 'km'
                return destination_distance
            else:
                print('\nInvalid distance!\n')
    
    def getDestinationEmergencyPhoneNumber(self):
        '''Gets the destination's emergency 
           contact's phone number from user'''

        while True:
            emergency_contact_phone = input("Enter the emergency contact's phone number: ").strip()
            if self.checkIfInt(emergency_contact_phone):
                if len(emergency_contact_phone) == 7:
                    return emergency_contact_phone
                else:
                    print('\nInvalid phone number!\n')
            else:
                print('\nInvalid phone number!\n')


    def checkIfInt(self,a_str):
        '''Checks if a string is an integer'''

        try:
            int(a_str)
            return True
        except ValueError:
            return False




