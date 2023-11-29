from flask import Blueprint, request
from main import db
from models.movies import Movie
from schemas.movie_schema import *
from flask_jwt_extended import jwt_required


movies = Blueprint('movies', __name__, url_prefix='/movies')

# The GET route endpoint (ALL movies)
@movies.route('/')
def all_movies():
    # Select the required records
    results = db.select(Movie)
    movies = db.session.scalars(results).all()
    return movies_schema.dump(movies)


# The GET route endpoint (1 movie)
@movies.route('/<int:movie_id>')
def get_movie(movie_id):
    # Select the required records
    results = db.select(Movie).filter_by(id=movie_id)
    movies = db.session.scalars(results).all()
    return movies_schema.dump(movies)


# The POST route endpoint (ADD movie)
@movies.route('/', methods = ['POST'])
@jwt_required()
def add_movie():
    if not jwt_required():
        print('User is not logged in!')
        return {'message': 'You must be a registered user to perform this operation.'}, 422
    new_movie = create_movie_schema.load(request.json)

    movie = Movie(
        title = new_movie['title'],
        genre = new_movie['genre'],
        length = new_movie['length'],
        year = new_movie['year']
    )
    db.session.add(movie)
    db.session.commit()
    print(f'New movie "{movie.title}" added to database')

    return movie_schema.dump(movie), 201


# The PUT route endpoint (EDIT movie)
@movies.route('/<int:movie_id>', methods = ['PUT', 'PATCH'])
def edit_movie(movie_id):
    update_info = create_movie_schema.load(request.json)
    stmt = db.select(Movie).filter_by(id=movie_id)
    movie = db.session.scalar(stmt)
    if not movie:
        return {'message' : 'Movie ID not found - please try again'}, 404
    else:
        movie.title = update_info.get('title', movie.title)
        movie.genre = update_info.get('genre', movie.genre)
        movie.length = update_info.get('length', movie.length)
        movie.year = update_info.get('year', movie.year)
        db.session.commit()
        print(f'{movie.title} has been updated.')
        return movie_schema.dump(movie), 200



# The DELETE route endpoint
@movies.route('/<int:movie_id>', methods = ['DELETE'])
@jwt_required()
def delete_movie(movie_id):
    if not jwt_required():
        return {'message': 'You must be a registered user to perform this operation.'}, 422
    
    stmt = db.select(Movie).filter_by(id=movie_id)
    movie = db.session.scalar(stmt)
    if not movie:
        return {'message' : 'Movie ID not found - please try again'}, 404
    movie_title = movie.title
    db.session.delete(movie)

    print(f'{movie_title} has been deleted.')
    return {}, 200




