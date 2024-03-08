use('journal');


db.categories.drop()
db.categories.insertMany([
    {'name': 'Food'},
    {'name': 'Coding'},
    {'name': 'Gaming'},
    {'name': 'Other'}
])

