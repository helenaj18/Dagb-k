from UI.crewUI import CrewUI

class DisplayMenuAirplaneType:
    
    def startDisplayLicensedPilots(self):

        while True:
            print('Please pick one license of the following:')
            print('1 - NAFokkerF100')
            print('2 - NAFokkerF28')
            print('3 - NABAE146')
            print('m - Back to main menu')
            selection = input()

            while selection != '1' and selection != '2' and selection != '3' and selection != 'm':
                print('Invalid selection')
                selection = input('Try again: ')

            if selection == '1':
                license_ID = 'NAFokkerF100'

            elif selection == '2':
                license_ID = 'NAFokkerF28'

            elif selection == '3':
                license_ID = 'NABAE146'
            
            else:
                # Goes back to main menu
                return
            
            return CrewUI().showByLicense(license_ID)

