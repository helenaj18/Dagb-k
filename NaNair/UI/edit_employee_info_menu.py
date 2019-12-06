from UI.crewUI import CrewUI


class EditEmployeeMenu:
    def __init__(self):
        pass

    def printEditEmployeeMenu(self,crew_id):
        #crew_member = LL_API().get_crew_member_by_id(crew_id)
        print('What would you like to change?')
        print()
        #try:
        #    employee.getCaptain()
        print('1 - Address')
        print('2 - Phone number')
        print('3 - Email')
        print('4 - Rank')
        print('5 - License')
        print()
        #except AttributeError:
            # print('1 - Address')
            # print('2 - Phone number')
            # print('3 - Email')
            # print('4 - Rank')
            # print()

    def editSelection(self,crew_id):
        self.printEditEmployeeMenu(crew_id)
        
        
        selection = input()
        if selection == '1':
            new_address = input("New address: ")
            CrewUI().changeEmployeeAddress(crew_id, new_address)

        elif selection == '2':
            new_phonenumber = input('New Phone number: ')
            CrewUI().changeEmployeePhonenumber(crew_id, new_phonenumber)

        elif selection == '3':
            new_email_address = input('New email: ')
            CrewUI().changeEmployeeEmail(crew_id, new_email_address)

        elif selection == '4':
            new_rank = input('Rank: ')

        elif selection == '5':
            new_license = input('License: ')
            CrewUI().changePilotLicense(crew_id,new_license)

        else:
            print("Invalid input")  