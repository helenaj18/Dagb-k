from UI.crewUI import CrewUI

class DisplayMenuAirplaneType:
    
    def startDisplayLicensedPilots(self):

        while True:
            print('Please pick one license of the following:')
            print('1 - NAFokkerF100')
            print('2 - NAFokkerF28')
            print('3 - NABAE146')
            print()
            selection = input()

            while selection != '1' and selection != '2' and selection != '3':
                print('Invalid selection')
                selection = input()

            if selection == '1':
                license_ID = 'NAFokkerF100'
            elif selection == '2':
                license_ID = 'NAFokkerF28'
            else:
                license_ID = 'NABAE146'
            
            return CrewUI().showByLicense(license_ID)

