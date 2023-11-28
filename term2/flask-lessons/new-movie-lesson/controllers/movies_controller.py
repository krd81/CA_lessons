from flask import Blueprint, request
from main import db
from models.movies import Movie
from schemas.movie_schema import movie_schema, movies_schema
from flask_jwt_extended import jwt_required


movies = Blueprint('movies', __name__, url_prefix='/movies')

# The GET route endpoint
@movies.route('/')
def all_movies():
    # Select the required records
    results = db.select(Movie)
    movies = db.session.scalars(results).all()
    return movies_schema.dump(movies)

# The POST route endpoint
@movies.route('/', methods = ['POST'])
@jwt_required()
def add_movie():
    if not jwt_required():
        print('User is not logged in!')
        return {'message': 'You must be a registered user to perform this operation.'}, 422
    new_movie = movie_schema.load(request.json)

    movie = Movie(
        title = new_movie['title'],
        genre = new_movie['genre'],
        length = new_movie['length'],
        year = new_movie['year']
    )
    db.session.add(movie)
    db.session.commit()
    print(f'New movie "{movie.title}" added to database')

    return {'message': 'Success', 'movie': movie_schema.dump(movie)}, 201



# The DELETE route endpoint
@movies.route('/<int:movie_id>', methods = ['DELETE'])
@jwt_required()
def delete_movie(movie_id):
    if not jwt_required():
        return {'message': 'You must be a registered user to perform this operation.'}, 422
    
    stmt = db.select(Movie).where(Movie.id == movie_id)
    movie = db.session.scalar(stmt)
    if not movie:
        return {'message' : 'Movie ID not found - please try again'}, 404
    movie_title = movie.title
    db.session.delete(movie)

    return {'message' : f'{movie_title} has been deleted.'}, 200




