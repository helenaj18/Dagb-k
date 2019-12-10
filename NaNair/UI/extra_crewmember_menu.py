from UI.crewUI import CrewUI
from API.LL_API import LL_API

class AddExtraCrewmemberMenu:

    def startAddExtraCrewMenu(self,voyage,crew_on_voyage_list):
        print('Voyage {} fully staffed'.format(voyage.getVoyageID()))
        print('Do you want to add an extra crew member?')
        print('1 - Yes')
        print('2 - No')
        selection = input().strip()
        if selection == '1':
            CrewUI().showNotWorkingCrew(voyage.getDepartureTime())
            print()

            if 'empty' in crew_on_voyage_list[-2:]:
                if 'empty' in crew_on_voyage_list[-1]:
                    crew_member = CrewUI().queryShowNotWorkingCrew()
                    if crew_member:
                        voyage.setFlightAttOne(crew_member)
                    else:
                        return 
                    
                elif 'empty' in crew_on_voyage_list[-2]:
                    crew_member = CrewUI().queryShowNotWorkingCrew()
                    if crew_member:
                        voyage.setFlightAttTwo(crew_member)
                    else:
                        return 
                
                LL_API().change_voyage(voyage)
                    
        elif selection == '2':
            return 

    #def setEmpty(self,voyage):
