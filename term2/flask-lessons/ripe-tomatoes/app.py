from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://tomato:abc123@127.0.0.1:5432/ripe_tomatoes_db'

print(app.config)

db = SQLAlchemy(app)
print(db)

class Card(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    genre = db.Column(db.String(100))
    length = db.Column(db.String(4))
    release_year = db.Column(db.String(4))


class Card(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    dob = db.Column(db.Date()) # dd/mm/yyyy


@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

@app.cli.command('db_seed')
def db_seed():
    card = Card(
        title = 'Oppenheimer',
        genre = 'Drama',
        length = '180',
        release_year = '2023',
    )

    card = Card(
        title = 'Barbie',
        genre = 'Comedy',
        length = '114',
        release_year = '2023',
    )

    card = Card(
        f_name = 'Julia',
        l_name = 'Roberts',
        gender = 'Female',
        dob = '28/10/1967'
    )

    card = Card(
        f_name = 'Tom',
        l_name = 'Hanks',
        gender = 'Male',
        dob = '09/07/1956' 
    )

    card = Card(
        f_name = 'Millie Bobby',
        l_name = 'Brown',
        gender = 'Female',
        dob = '19/02/2004' 
    )

    card = Card(
        f_name = 'Chloe Grace',
        l_name = 'Moretz',
        gender = 'Female',
        dob = '10/02/1997' 
    )


    db.session.add(card)
    # db.session.add(card)
    db.session.commit()
    print('Database seeded')


@app.route('/')
def index():
    return 'Hello World!'