import dog

# dog1 = dog.create('Ted', 15, 'Border Collie')
# dog2 = dog.create('Loki', 3, 'Border Collie')

# dog.walk(dog1)
# dog.walk(dog2)
# dog.walk(42)

dog1 = dog.Dog('Ted', 15)    # create a new instance of Dog
# dog1.name = 'Ted' # creates a new attribute

dog2 = dog.Dog('Loki', 3)

print(f'dog1: {dog1.__dict__}')
print(f'dog2: {dog2.__dict__}')
dog1.greet('Goodbye')
dog2.greet('Hello')