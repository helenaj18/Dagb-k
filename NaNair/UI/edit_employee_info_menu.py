from UI.crewUI import CrewUI


class EditEmployeeMenu:
    def __init__(self):
        pass

    def startEditEmployeeMenu(self):
        print('What would you like to change?')
        print()
    

        print('1 - Address')
        print('2 - Phone number')
        print('3 - Email')
        print('4 - Rank')
        if employee.getCaptain():
            print('5 - License')


    def editSelection(self,crew_id):
        selection = input()
        if selection == '1':
            new_address = input("New address: ")
            CrewUI().changeEmployeeAddress(crew_id, new_address)

        elif selection == '2':
            new_phonenumber = input('New Phone number: ')

        elif selection == '3':
            new_email_address = input('New email: ')
            CrewUI().changeEmployeeEmail(crew_id, new_email_address)

        elif selection == '4':
            new_rank = input('Rank: ')

        elif selection == '5':
            new_license = input('License: ')

        else:
            print("Invalid input")  