form_fields = {
    'type': {
        'type': 'text',
        'question': 'What is the type of the airplane'
    },
    'seats': {
        'type': 'int',
        'question': 'How many seats are available'
    },
    'yearMade': {
        'type': 'date',
        'question': 'What year was the plane manufactured'
    }
}

class Formzy:
    def __init__(self, fields):
        self.return_dictionary = {}
        for key, value in fields.items():
            self.return_dictionary[key] = self.ask_question_field(value)


    def ask_question_field(self, field):
        if field['type'] == 'text':
            return input(field['question'])
        elif field['type'] == 'int':
            return int(input(field['question']))
        elif field['type'] == 'date':
            day = input('What is the day? ')
            month = input('What is the month? ')
            year = input('What is the year? ')
            return year

    
    def get_input_values(self):
        return self.return_dictionary

my_formzy = Formzy(form_fields)
print(my_formzy.get_input_values())