from main import db
from flask import Blueprint
from main import bcrypt
from models.movie import Movie
from models.actor import Actor
from models.cast import Cast
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
        Director(
            name = "Sam Mendes",
            country = "UK"
        ),
    ]

    db.session.add_all(directors)
    db.session.commit()


    movies = [
        Movie(
            # 0
            title = "Barbie",
            genre = "Comedy",
            length = "114",
            year = "2023",
            director_id = directors[0].id
        ),
        Movie(
            # 1
            title = "Oppenheimer",
            genre = "Drama",
            length = "180",
            year = "2023",
            director_id = directors[1].id
        ),
        Movie(
            # 2
            title = "The Little Mermaid",
            genre = "Animation",
            length = "135",
            year = "2023",
            director_id = directors[2].id
        ),
        Movie(
            # 3
            title = "Avatar: The Way of Water",
            genre = "Action",
            length = "192",
            year = "2022",
            director_id = directors[3].id
        ),
        Movie(
            # 4
            title = "Titantic",
            genre = "Drama",
            length = "194",
            year = "1998",
            director_id = directors[3].id
        ),
        Movie(
            # 5
            title = "Revolutionary Road",
            genre = "Drama",
            length = "119",
            year = "2008",
            director_id = directors[4].id
        ),
        '''Movie(
            title = "",
            genre = "",
            length = "",
            year = "",
            director_id = ""
        ),
        Movie(
            title = "",
            genre = "",
            length = "",
            year = "",
            director_id = ""
        ), '''        
        ]

    db.session.add_all(movies)
    db.session.commit()


    actors = [
        Actor(
            # 0
            f_name = "Harry",
            l_name = "Styles",
            gender = "Male",
            country = "UK",
            dob = "1994/02/01"
        ),
        Actor(
            # 1
            f_name = "Leonardo",
            l_name = "DiCaprio",
            gender = "Male",
            country = "USA",
            dob = "1956/07/09"
        ),
       Actor(
           # 2
            f_name = "Kate",
            l_name = "Winslet",
            gender = "Female",
            country = "UK",
            dob = "1975/10/05"
        ),
       Actor(
           # 3
            f_name = "Zoe",
            l_name = "Saldana",
            gender = "Female",
            country = "USA",
            dob = "1978/06/19"
        ),
       Actor(
           # 4
            f_name = "Sam",
            l_name = "Worthington",
            gender = "Male",
            country = "UK",
            dob = "1976/08/02"
        ),        
       Actor(
           # 5
            f_name = "Margot",
            l_name = "Robbie",
            gender = "Female",
            country = "Australia",
            dob = "1990/07/02"
        ),
        Actor(
            # 6
            f_name = "Daisy",
            l_name = "Edgar-Jones",
            gender = "Female",
            country = "UK",
            dob = "1998/05/24"
        ),
        Actor(
            # 7
            f_name = "Halle",
            l_name = "Bailey",
            gender = "Female",
            country = "USA",
            dob = "2000/03/27"
        ),
        Actor(
            # 8
            f_name = "Taylor John",
            l_name = "Smith",
            gender = "Male",
            country = "USA",
            dob = "1995/05/13"
        ),
        '''Actor(
            f_name = "",
            l_name = "",
            gender = "",
            country = "",
            dob = ""
        ),
        Actor(
            f_name = "",
            l_name = "",
            gender = "",
            country = "",
            dob = ""
        ),
        Actor(
            f_name = "",
            l_name = "",
            gender = "",
            country = "",
            dob = ""
        ), '''

        ]


    db.session.add_all(actors)
    db.session.commit()

    cast = [
        Cast(
            actors_id = actors[0].id,
            movies_id = movies[5].id
        ),
        Cast(
            actors_id = actors[3].id,
            movies_id = movies[3].id
        ),
        Cast(
            actors_id = actors[4].id,
            movies_id = movies[3].id
        ),
        Cast(
            actors_id = actors[1].id,
            movies_id = movies[4].id
        ),
        Cast(
            actors_id = actors[2].id,
            movies_id = movies[4].id
        ),
        Cast(
            actors_id = actors[1].id,
            movies_id = movies[5].id
        ),
        Cast(
            actors_id = actors[2].id,
            movies_id = movies[5].id
        ),
        Cast(
            actors_id = actors[2].id,
            movies_id = movies[3].id
        ),
        Cast(
            actors_id = actors[3].id,
            movies_id = movies[2].id
        ),
    ]

    db.session.add_all(cast)
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


   	
