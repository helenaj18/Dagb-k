from API.LL_API import LL_API

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



