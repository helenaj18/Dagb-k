class AddExtraCrewmemberMenu:

    def startAddExtraCrewMenu(self):
        print('Voyage {} fully staffed'.format(voyage.getVoyageID()))
        print('Do you want to add an extra crew member?')
        print('1 - Yes')
        print('2 - No')
        selection = input()
        if selection == '1':

            if 'empty' in crew_on_voyage_list[-2:]:
                if 'empty' in crew_on_voyage_list[-1]:
                    crew_member = CrewUI().queryShowNotWorkingCrew()
                        
                    voyage.setFlightAttOne(crew_member)
                elif 'empty' in crew_on_voyage_list[-2]:
                    crew_member = CrewUI().queryShowNotWorkingCrew()
                    voyage.setFlightAttTwo(crew_member)
        elif selection == '2':
            return 