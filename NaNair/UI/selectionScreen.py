some_recipe = [ 
    {'option': 'a', 'reason': 'see list of flights'},
    {'option':'k','reason':'find one flight'  
    }
]

some_question = 'What do you want to do? '

class SelectionScreen:
    def __init__(self, question, options):
        self.question = question
        self.options = options
        self.customer_input = None
        while not self.validate_customer_input():
            self.customer_input = self.show_menu()

    def show_menu(self):
        for item in self.options: 
            print('Select {} to {}'.format(item['option'],item['reason']))
        print('Press q to go back')
        return input(self.question)

    def validate_customer_input(self):
        if self.customer_input is None:
            return False
        elif self.customer_input == 'q':
            return True
        else: 
            for item in self.options: 
                if item['option'].lower() == self.customer_input.lower():
                    return True
        
        return False

myScreen = SelectionScreen(some_question, some_recipe)
