
class ListClass:
    ''' List item in a dictionary'''

    def __init__(self, fields, objects):
        for item in objects:
            for field in fields:
                print(item[field], end=' ')
            print('\n')
        input('Press any key to continue ')


airplanes = [
   {'type': 'B737', 'name' : 'TF Frost', 'seats': 250},
   {'type': 'Fokker 50', 'name' : 'TF gay', 'seats': 50},
   {'type': 'BAE 146', 'name' : 'TF cool', 'seats': 150} 
]

fields_to_print = ['type','name']

ListClass(fields_to_print, airplanes)