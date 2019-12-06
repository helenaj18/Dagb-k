from UI.crewUI import CrewUI
from API.LL_API import LL_API


class EditEmployeeMenu:
    def __init__(self):
        pass

    def printEditEmployeeMenu(self,crew_id,employee):
        #crew_member = LL_API().get_crew_member_by_id(crew_id)
        print('What would you like to change?')
        print()
        if type(employee) == Pilot:
        #    employee.getCaptain()
            print('1 - Address')
            print('2 - Phone number')
            print('3 - Email')
            print('4 - Rank')
            print('5 - License')
            
        elif type(employee) == Pilot:
            print('1 - Address')
            print('2 - Phone number')
            print('3 - Email')
            print('4 - Rank')
            
        print()

    def editSelection(self,crew_id):
        employee = LL_API().get_crew_member_by_id(crew_id)
        self.printEditEmployeeMenu(crew_id,employee)
        
        
        selection = input()
        if selection == '1':
            new_address = input("New address: ")
            #employee.changeEmployeeAddress(new_address)
            employee.setAdress(new_address)
            CrewUI().changeEmployeeInfo(employee)

        elif selection == '2':
            new_phonenumber = input('New Phone number: ')
            employee.setPhonenumber(new_phonenumber)
            CrewUI().changeEmployeeInfo(employee)

        elif selection == '3':
            new_email_address = input('New email: ')
            employee.setEmail(new_email_address)
            CrewUI().changeEmployeeInfo(employee)

        elif selection == '4':
            new_rank = input('Rank: ')

        elif selection == '5':
            new_license = input('License: ')
            CrewUI().changePilotLicense(crew_id,new_license)

        else:
            print("Invalid input")  