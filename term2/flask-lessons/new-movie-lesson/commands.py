from main import db
from flask import Blueprint
from main import bcrypt
from models.movies import Movie
from models.actors import Actor
from models.users import User
from datetime import date

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")


@db_commands.cli.command("seed")
def db_seed():
    movies = [
        Movie(
            title = "Barbie",
            genre = "Comedy",
            length = "114",
            year = "2023"
        ),
        Movie(
            title = "Oppenheimer",
            genre = "Drama",
            length = "180",
            year = "2023"
        ),
        Movie(
            title = "The Little Mermaid",
            genre = "Animation",
            length = "135",
            year = "2023"
        ),
        Movie(
            title = "Avatar: The Way of Water",
            genre = "Action",
            length = "192",
            year = "2022"
        ),]


    actors = [
        Actor(
            f_name = "Julia",
            l_name = "Roberts",
            gender = "Female",
            country = "USA",
            dob = "1967/10/28"
        ),
        Actor(
            f_name = "Tom",
            l_name = "Hanks",
            gender = "Male",
            country = "USA",
            dob = "1956/07/09"
        ),
       Actor(
            f_name = "Chloe Grace",
            l_name = "Moretz",
            gender = "Female",
            country = "USA",
            dob = "1997/02/10"
        ),
       Actor(
            f_name = "Matthew",
            l_name = "Perry",
            gender = "Male",
            country = "Canada",
            dob = "1969/08/19"
        ),
       Actor(
            f_name = "Adam",
            l_name = "Sandler",
            gender = "Male",
            country = "USA",
            dob = "1966/09/09"
        ),        
       Actor(
            f_name = "Margot",
            l_name = "Robbie",
            gender = "Female",
            country = "Australia",
            dob = "1990/07/02"
        ),]
    
    users = [
        User(
            username = 'admin',
            password = bcrypt.generate_password_hash('abc123').decode('utf8')
        ),

    ]


    db.session.add_all(movies)
    db.session.add_all(actors)
    db.session.add_all(users)
    db.session.commit()

    print("Database seeded")
