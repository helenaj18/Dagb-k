from UI.crewUI import CrewUI
from API.LL_API import LL_API
from ModelClasses.flight_att_model import FlightAttendant
from ModelClasses.pilot_model import Pilot
from UI.edit_employee_licence import EditEmployeeLicense


class EditEmployeeMenu:
    def __init__(self):
        pass

    def printEditEmployeeMenu(self,crew_id,employee):
        #crew_member = LL_API().get_crew_member_by_id(crew_id)
        print('What would you like to change?')
        print()
        print('1 - Address')
        print('2 - Phone number')
        print('3 - Email')
        print('4 - Rank')

        if type(employee) == Pilot:
            print('5 - License')
            
        print()

    def editSelection(self,crew_id):
        employee = LL_API().get_crew_member_by_id(crew_id)
        self.printEditEmployeeMenu(crew_id,employee)
        
        
        selection = input()
        if selection == '1':
            ''' The software asks for new home adress and assigns it to the owner of given ID'''
            new_address = CrewUI().getHomeAddress()
            employee.setAddress(new_address)
            CrewUI().changeEmployeeInfo(employee)

        elif selection == '2':
            ''' The software asks for new phone number and assigns it to the owner of given ID'''
            new_phonenumber = CrewUI().getPhoneNumber()
            employee.setPhonenumber(new_phonenumber)
            CrewUI().changeEmployeeInfo(employee)

        elif selection == '3':
            ''' The software asks for new email adress and assigns it to the owner of given ID'''
            new_email_address = CrewUI().getEmail()
            employee.setEmail(new_email_address)
            CrewUI().changeEmployeeInfo(employee)

        elif selection == '4':
            ''' The software asks for new rank and assigns it to the owner of given ID'''
            if type(employee) == Pilot:
                print('Please choose one: ')
                print('0 - Co-pilot')
                print('1 - Captain')
            else: 
                print('Please choose one: ')
                print('0 - Flight attendant')
                print('1 - Head service manager')
            new_rank = input('Rank: ')

            employee.setRank(new_rank)
            CrewUI().changeEmployeeInfo(employee)
            

        elif selection == '5':
            ''' The software asks for new license and assigns it to the owner of given ID'''
            EditEmployeeLicense().startEditEmployeeLicense(employee)

        else:
            print("Invalid input")  