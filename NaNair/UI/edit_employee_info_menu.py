from UI.crewUI import CrewUI


class EditEmployeeMenu:
    def __init__(self):
        pass

    def startEditEmployeeMenu(self):
        print('What would you like to change?')
        print()
        try:
            employee.getCaptain()
            print('1 - Address')
            print('2 - Phone number')
            print('3 - Email')
            print('4 - Rank')
            print('5 - License')
            print()
        except AttributeError:
            print('1 - Address')
            print('2 - Phone number')
            print('3 - Email')
            print('4 - Rank')
            print()

    def editSelection(self):
        selection = input()
        if selection == '1':
            new_address = input("New address: ")
            CrewUI()

        elif selection == '2':
            new_phonenumber = input('New Phone number: ')

        elif selection == '3':
            new_email = input('New email: ')

        elif selection == '4':
            new_rank = input('Rank: ')

        elif selection == '5':
            new_license = input('License: ')

        else:
            print("Invalid input")  