from main import db
from flask import Blueprint
from main import bcrypt
from models.movie import Movie
from models.actor import Actor
from models.director import Director
from models.user import User
from models.review import Review
from datetime import date

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")


@db_commands.cli.command("seed")
def db_seed():
    directors = [
        Director(
            name = "Greta Gerwig",
            country = "USA"
        ),
        Director(
            name = "Christopher Nolan",
            country = "UK"
        ),
        Director(
            name = "Rob Marshall",
            country = "USA"
        ),
        Director(
            name = "James Cameron",
            country = "Canada"
        ),
        Director(
            name = "Olivia Wilde",
            country = "UK"
        ),

    ]

    db.session.add_all(directors)
    db.session.commit()


    movies = [
        Movie(
            title = "Barbie",
            genre = "Comedy",
            length = "114",
            year = "2023",
            director_id = directors[0].id
        ),
        Movie(
            title = "Oppenheimer",
            genre = "Drama",
            length = "180",
            year = "2023",
            director_id = directors[1].id
        ),
        Movie(
            title = "The Little Mermaid",
            genre = "Animation",
            length = "135",
            year = "2023",
            director_id = directors[2].id
        ),
        Movie(
            title = "Avatar: The Way of Water",
            genre = "Action",
            length = "192",
            year = "2022",
            director_id = directors[3].id
        ),]

    db.session.add_all(movies)
    db.session.commit()


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


    db.session.add_all(actors)
    db.session.commit()


    users = [
        User(
            username = 'admin',
            password = bcrypt.generate_password_hash('abc123').decode('utf8')
        ),

    ]

    db.session.add_all(users)
    db.session.commit()

    reviews = [
        Review(
            message = 'A fun and uplifting story about feminism, being in charge of your own destiny and how Barbie has inspired this movement',
            movie_id = movies[0].id,
            user_id = users[0].id
        ),
        Review(
            message = 'A live action re-telling of the fairytale classic, with Halle Bailey and Jonah Hauer-King',
            movie_id = movies[2].id,
            user_id = users[0].id
        ),
        Review(
            message = 'The long-awaited sequel to Avatar, which follows the life of Jake and Natiri as their family is exiled from their home on Pandora',
            movie_id = movies[3].id,
            user_id = users[0].id
        )
    ]

    db.session.add_all(reviews)
    db.session.commit()


    print("Database seeded")
