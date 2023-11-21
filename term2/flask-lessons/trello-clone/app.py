from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello'

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
print(db)

class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    status = db.Column(db.Text())
    date_created = db.Column(db.Date())

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable = False, unique = True) # Will add validation later
    password = db.Column(db.String, nullable = False) # Will be stored encrypted using 1-way hash
    is_admin = db.Column(db.Boolean, default = False) # Will be used later for authorisation

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')


@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

@app.cli.command('db_seed')
def db_seed():
    users = [
        User(
            email = 'admin@spam.com',
            password = bcrypt.generate_password_hash('spinynorman').decode('utf8'),
            is_admin = True
        ),
        User(
            name = 'John Cleese',
            email = 'cleese@spam.com',
            password = bcrypt.generate_password_hash('tisbutascratch').decode('utf8')
        )
    ]


    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create ERD',
            status = 'Done',
            date_created = date.today()
        ),
        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement CRUD queries',
            status = 'In Progress',
            date_created = date.today()
        ),
        Card(
            title = 'Marshmallow',
            description = 'Stage 3 - Implement JSONify of models',
            status = 'In Progress',
            date_created = date.today()
        ),]
    
    db.session.add_all(cards)
    db.session.add_all(users)
    db.session.commit()
    print('Database seeded')


@app.cli.command('all_cards')
def all_cards():
    # select * from cards;
    stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    # stmt = db.select(Card).order_by(Card.title)
    cards = db.session.scalars(stmt)
    # print(cards.all())
    for card in cards:
        print(card.__dict__)

# Routes need to have a resource type
# This is an entity that is being tracked by the api
@app.route('/users/not_register', methods = ['POST'])
def not_register():
    user_info = UserSchema(exclude = ['id']).load(request.json)
    
    user = User(
        email = user_info['email'],
        password = bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
        name = user_info.get('name', '')
    )
    
    # Add and commit the new user to the database
    db.session.add(user)
    db.session.commit()

    print(user.__dict__)
    # Return the new user
    return UserSchema(exclude = ['password']).dump(user), 201


@app.route('/users/register', methods = ['POST'])
def register():
    user_info = request.json
    print(user_info)
    return 'ok', 201
    

@app.route('/cards')
def all_cards():
    # select * from cards;
    stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 0)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)



@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

