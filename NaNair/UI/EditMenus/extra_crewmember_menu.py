from UI.crewUI import CrewUI
from API.LL_API import LL_API


class AddExtraCrewmemberMenu:
    def startAddExtraCrewMenu(self,voyage,crew_on_voyage_list):
        '''Menu for adding an extra crew member'''

        print('\n'+'~'*45)
        a_str = 'Voyage {} has enough staff!'.format(voyage.getVoyageID())
        print('{:^45}'.format(a_str))
        print('~'*45+'\n')
       
        while True:
            print('-'*45)
            print('{:^45}'.format('Do you want to add an extra crew member?'))
            print('-'*45+'\n')
            print('1 - Yes')
            print('2 - No (Go back)')
            selection = input('\nPlease choose one of the above (1/2): ').strip()

            # add extra crew member is chosen
            if selection == '1':
                # show list of crew that is not working on particular day
                CrewUI().showNotWorkingCrew(voyage.getDepartureTime())
                print()
                
                if 'empty' in crew_on_voyage_list[-2:]:
                    if 'empty' in crew_on_voyage_list[-2]:
                        crew_member = CrewUI().queryShowNotWorkingCrew()
                        if self.isPilot(crew_member):
                            continue

                        if crew_member:
                            if self.checkIfCrewmemberWorking(voyage,crew_member):
                                print('Flight attendant is assigned to another voyage on the same date\n\
                                    please chose another flight attendant\n')
                                continue

                            voyage.setFlightAttOne(crew_member)
                    
                        LL_API().change_voyage(voyage)
                        crew_on_voyage_list = voyage.getCrewOnVoyage()
                        print('\n'+'~'*45)
                        print('{:^45}'.format('Employee successfully added!'))
                        print('\n'+'~'*45)

                        
                    elif 'empty' in crew_on_voyage_list[-1]:
                        crew_member = CrewUI().queryShowNotWorkingCrew()
                        if crew_member:
                            if self.isPilot(crew_member):
                                continue

                            if self.checkIfCrewmemberWorking(voyage,crew_member):
                                print('Flight attendant is assigned to another voyage on the same date\n\
                                    please chose another flight attendant\n')
                                continue

                            voyage.setFlightAttTwo(crew_member)
                    
                        LL_API().change_voyage(voyage)
                        crew_on_voyage_list = voyage.getCrewOnVoyage()
                        print('\n'+'~'*45)
                        print('{:^45}'.format('\nEmployee successfully added!'))
                        print('{:^45}'.format('The voyage is fully staffed!\n'))
                        print('\n'+'~'*45)
                        return

                else:
                    print('\n'+'~'*45)
                    print('The voyage is fully staffed!')
                    print('\n'+'~'*45)
                    return
                        
            elif selection == '2':
                break 

            else: 
                print('\nInvalid selection!\n')


    def isPilot(self,crew_member):
        '''Checks if crewmember is a pilot, prints message 
            and returns True if crewmember is Pilot'''
        if crew_member.getRole() == 'Pilot':
            print('-'*45)
            a_str = '\nCrewmember {} is a Pilot'.format(crew_member.getName())
            print('{:^45}'.format(a_str))
            print('{:^45}'.format('You can only add an extra flight attendant'))
            print('-'*45)
            return True
        return False

    def checkIfCrewmemberWorking(self,voyage,crew_member):
        '''Checks if crewmember is working on the day of the voyage'''
        
        voyage_departuredate_str = voyage.getDepartureTime()
        voyage_departure_datetime = LL_API().revertDatetimeStrtoDatetime(voyage_departuredate_str)

        voyage_arrivaldate_str = voyage.getArrivalTimeHome()
        voyage_arrival_datetime = LL_API().revertDatetimeStrtoDatetime(voyage_arrivaldate_str)


        voyages_on_date = LL_API().get_all_voyages_in_date_range(voyage_departure_datetime,voyage_arrival_datetime)

        for voyage in voyages_on_date:
            if crew_member.getCrewID() in voyage.getCrewOnVoyage():
                return True




