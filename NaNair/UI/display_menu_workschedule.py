from UI.crewUI import CrewUI
from API.LL_API import LL_API
import datetime

class DisplayMenuWorkSchedule():

    def startDisplayMenuWorkSchedule(self):
        user_id = input('Enter employee ID: ')
        print('Enter the "From date" for work schedule')
        start_year_int = int(input('Year: '))
        start_month_int = int(input('Month: '))
        start_day_int = int(input('Day: '))
        start_date = datetime.datetime(start_year_int,start_month_int,start_day_int,0,0,0).isoformat()
        print('Enter the "To date" for work schedule')
        end_year_int = int(input('Year: '))
        end_month_int = int(input('Month: '))
        end_day_int = int(input('Day: '))
        end_date = datetime.datetime(end_year_int,end_month_int,end_day_int,0,0,0).isoformat()

        employee = LL_API().get_crew_member_by_id(user_id)
        name = employee.getName()
        #working_crew_list
        name_header_str = '{:<10} {:<10}'.format(name,user_id)
        header_str = 'Working Schedule {}-{}'.format(str(start_day_int)+str(start_month_int)+str(start_day_int),str(end_year_int)+str(end_month_int)+str(end_day_int))
        print(name_header_str)
        print(header_str)
        print(len(header_str)*'-')

        for working_crew_per_voyage in working_crew_list:
            destination_instance = working_crew_per_voyage[1]
            destination_name = destination_instance.getDestinationName()

            for crew_id in working_crew_per_voyage[0]:
                if crew_id != 'empty':
                    crew_member = LL_API().get_work_schedule(start_date,end_date)
                    crew_name = crew_member.getName()
                    crew_address = crew_member.getAddress()
                    crew_phone = crew_member.getPhoneNumber()
                    format_str = '{:<20}{:<20}{:<20}{:<20}{:<20}'.format(crew_name,crew_id,crew_address,crew_phone,destination_name)
                    print(format_str)
            print()