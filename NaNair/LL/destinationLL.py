from API.IO_API import IO_API
from IO.destinationIO import DestinationIO
from ModelClasses.destination_model import Destination
from LL.airplaneLL import AirplaneLL

class DestinationLL:

    def getDestination(self): 
        ''' Gets destination from Destination class'''

        return IO_API().loadDestinationFromFile()

    def addDestination(self):
        '''Gets information about a new destination
           and adds it to destination file'''

        while True:
            destination_airport = input('Destination airport code (3char airport code): ').upper()

            if len(destination_airport) == 3:
                destination_name = input('Name of destination: ').capitalize()
                
                print('Enter flight duration')

                flight_duration_hours_str = input('Hours: ')
                flight_duration_minutes_str = input('Minutes: ')

                AirplaneLL().verifyTime(flight_duration_hours_str,flight_duration_minutes_str)

                flight_duration_str = flight_duration_hours_str + 'h' + flight_duration_minutes_str + 'm'


                while True:

                    destination_distance = input('Distance in km: ')

                    if self.checkIfInt(destination_distance):
                        destination_distance += 'km'
                    
                        emergency_contact_name = input('Enter the emergency contact name: ').capitalize()

                        while True:
                            emergency_contact_phone = input("Enter the emergency contact's phone number: ")

                            if self.checkIfInt(emergency_contact_phone):
                                if len(emergency_contact_phone) == 7:
                                    new_destination = Destination(destination_name,destination_airport,\
                                        flight_duration_str, destination_distance,emergency_contact_name,\
                                            emergency_contact_phone)

                                    return IO_API().addDestinationToFile(new_destination)

                                else:
                                    print('Invalid phone number')

                            else:
                                print('Invalid phone number')
                    else:
                        print('Invalid distance')
                         
            else:
                print('Invalid airport code')

    def checkIfInt(self,a_str):
        try:
            int(a_str)
            return True
        except ValueError:
            return False


    def changeDestinationFile(self, new_dest_instance):
        return IO_API().changeDestinationFile(new_dest_instance)

    # def changeEmergencyContactName(self,destination_name,new_emergency_contact):
    #     '''Changes the Emergency Contact name for destination in file'''
    #     destination_list = IO_API().loadDestinationFromFile()
    #     new_destination_list = []

    #     #Reads every line until it finds the same name of the airport as the input (destinantion_name)
    #     #and then changes the airports emergency contact to the same as the input (new_emergency_contact)
    #     for destination in destination_list:
    #         if destination_name == destination.getDestinationAirport():
    #             destination.setEmergencyContactName(new_emergency_contact)
    #         new_destination_list.append(destination)

    #     #Sends destination list to DestinationIO to overwrite the file with new information       
    #     DestinationIO().changeDestinationFile(new_destination_list)
    

    # def changeEmergencyContactPhone(self,destination_name,new_emergency_phone):
    #     '''Changes the Emergency Contact Phone number for destination in file'''
    #     destination_list = IO_API().loadDestinationFromFile()
    #     new_destination_list = []

    #     #Reads every line until it finds the same name of the airport as the input (destinantion_name)
    #     #and then changes the airports emergency phone number to the same as the input (new_emergency_phone)
    #     for destination in destination_list:
    #         if destination_name == destination.getDestinationAirport():
    #             destination.setEmergencyContactPhone(new_emergency_phone)
    #         new_destination_list.append(destination)
        
    #     #Sends destination list to DestinationIO to overwrite the file with new information
    #     DestinationIO().changeDestinationFile(new_destination_list)
        





