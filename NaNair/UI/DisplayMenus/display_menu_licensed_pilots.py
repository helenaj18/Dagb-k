from UI.crewUI import CrewUI
from UI.airplaneUI import AirplaneUI

class DisplayMenuAirplaneType:
    
    def startDisplayLicensedPilots(self):
        '''Display menu for licensed pilots'''

        success = False
        airplane_types = AirplaneUI().getAirplaneTypes()

        while True:
            print('\nPlease pick one license of the following:\n')

            counter = 1
            for airplane_type in airplane_types:
                print('{} - {}'.format(counter,airplane_type))
                counter += 1

            selection = input('\nPlease choose one of the above: ').strip()

            for i in range(1,counter+1):
                if selection == str(i):
                    license_ID = airplane_types[i-1].getplaneTypeID()
                    success = True
                    return CrewUI().showByLicense(license_ID)

            if not success:
                print('\nInvalid selection!\n')
