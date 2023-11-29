# Blueprints should create instances of classes and replace what 
# would have been @app methods in the original un-modularised version

from flask import Blueprint
from setup import db, bcrypt
from models.card import Card
from models.user import User
from datetime import date

# 'db' needs to be called in the command line so choose a meaningful name
db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

@db_commands.cli.command('seed')
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
    db.session.add_all(users)
    db.session.commit()


    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create ERD',
            status = 'Done',
            date_created = date.today(),
            user_id = users[0].id
        ),
        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement CRUD queries',
            status = 'In Progress',
            date_created = date.today(),
            user_id = users[1].id
        ),
        Card(
            title = 'Marshmallow',
            description = 'Stage 3 - Implement JSONify of models',
            status = 'In Progress',
            date_created = date.today(),
            user_id = users[0].id
        )]
    
    db.session.add_all(cards)
    db.session.commit()
    print('Database seeded')


@db_commands.cli.command('all_cards')
def all_cards():
    # select * from cards;
    stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    # stmt = db.select(Card).order_by(Card.title)
    cards = db.session.scalars(stmt)
    # print(cards.all())
    for card in cards:
        print(card.__dict__)
