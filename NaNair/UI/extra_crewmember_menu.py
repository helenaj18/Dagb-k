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
                        if self.checkIfCrewmemberWorking(voyage,crew_member):
                            raise Exception('Flight attendant is assigned to another voyage on the same date\n\
                                please chose another flight attendant\n')
                        voyage.setFlightAttOne(crew_member)
                    else:
                        return 
                    
                elif 'empty' in crew_on_voyage_list[-2]:
                    crew_member = CrewUI().queryShowNotWorkingCrew()
                    if crew_member:
                        if self.checkIfCrewmemberWorking(voyage,crew_member):
                            raise Exception('Flight attendant is assigned to another voyage on the same date\n\
                                please chose another flight attendant\n')
                        voyage.setFlightAttTwo(crew_member)
                    else:
                        return 
                
                LL_API().change_voyage(voyage)
                    
        elif selection == '2':
            return 

    #def setEmpty(self,voyage):

    def checkIfCrewmemberWorking(self,voyage,crew_member):
        voyage_departuredate_str = voyage.getDepartureTime()
        voyage_departure_datetime = LL_API().revertDatetimeStrtoDatetime(voyage_departuredate_str)

        voyage_arrivaldate_str = voyage.getArrivalTimeHome()
        voyage_arrival_datetime = LL_API().revertDatetimeStrtoDatetime(voyage_arrivaldate_str)


        voyages_on_date = LL_API().get_all_voyages_in_date_range(voyage_departure_datetime,voyage_arrival_datetime)

        for voyage in voyages_on_date:
            if crew_member.getCrewID() in voyage.getCrewOnVoyage():
                return True


