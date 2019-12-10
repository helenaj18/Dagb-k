from UI.crewUI import CrewUI

class DisplayMenuAirplaneType:
    
    def startDisplayLicensedPilots(self):
        '''Display menu for licensed pilots'''

        while True:
            print('\nPlease pick one license of the following:\n')
            print('1 - NAFokkerF100')
            print('2 - NAFokkerF28')
            print('3 - NABAE146')
            print('m - Back to main menu')
            selection = input('\nPlease choose one of the above (1-4 or m): ').strip()

            # if none of the possible options are chosen
            while selection != '1' and selection != '2' and selection != '3' and selection != 'm':
                print('\nInvalid selection!\n')
                selection = input('Try again: ').strip()

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

