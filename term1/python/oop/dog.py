# my_dog = { 'name': 'Ted', 'age': 15, 'breed': 'Border Collie' }

class Dog:
    def __init__(self, spam, eggs):
        self.name = spam
        self.age = eggs
        self.state = 'sleeping'

    def greet(self, prefix):
        # print(f'spam: {spam}')
        print(f'{prefix}, {self.name}!')