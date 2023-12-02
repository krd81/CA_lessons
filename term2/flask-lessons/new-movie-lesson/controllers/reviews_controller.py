from flask import Blueprint, request
from main import db, unauthorised_user
from models.reviews import Review
from models.movies import Movie
from schemas.review_schema import *
from schemas.movie_schema import *
from flask_jwt_extended import jwt_required, get_jwt_identity


reviews = Blueprint('reviews', __name__, url_prefix='/<int:movie_id>/reviews')
unauthorised_user

# The GET route endpoint (ALL reviews for an individual movie)
@reviews.route('/')
def all_reviews(movie_id):
    # Select the required records
    stmt = db.select(Movie).filter_by(id=movie_id)
    reviews = db.session.scalars(stmt).all()
    return movie_reviews_schema.dump(reviews)

'''
# The GET route endpoint (1 review) - NOT REQUIRED
@reviews.route('/<int:review_id>')
def get_review(movie_id, review_id):
    # Select the required records
    stmt = db.select(Review).filter_by(id=review_id)
    review = db.session.scalar(stmt)
    if not review:
        return {'message' : 'Review ID not found - please try again'}, 404
    else:    
        return review_schema.dump(review), 200

'''



# The POST route endpoint (ADD review)
@reviews.route('/', methods = ['POST'])
@jwt_required()
def add_review(movie_id):
    stmt = db.select(Movie).filter_by(id=movie_id)
    new_review = ReviewSchema(exclude=['id']).load(request.json)
    review = Review(
        message = new_review['message'],
        user = get_jwt_identity(),
        movie = stmt       
    )
    db.session.add(review)
    db.session.commit()
    print(f'New review for "{stmt.title}" added to database')

    return review_schema.dump(review), 201


# The PUT route endpoint (EDIT review)
@reviews.route('/<int:review_id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def edit_review(movie_id, review_id):
    update_info = review_schema_no_id.load(request.json)
    stmt = db.select(Review).filter_by(id=review_id)
    review = db.session.scalar(stmt)
    if not review:
        return {'message' : 'Review ID not found - please try again'}, 404
    else:
        review.title = update_info.get('title', review.title)
        review.genre = update_info.get('genre', review.genre)
        review.length = update_info.get('length', review.length)
        review.year = update_info.get('year', review.year)
        db.session.commit()
        print(f'{review.title} has been updated.')
        return review_schema.dump(review), 200



# The DELETE route endpoint
@reviews.route('/<int:review_id>', methods = ['DELETE'])
@jwt_required()
def delete_review(movie_id, review_id): 
    stmt = db.select(Review).filter_by(id=review_id)
    review = db.session.scalar(stmt)
    if not review:
        return {'message' : 'Review ID not found - please try again'}, 404
    else:    
        review_title = review.title
        db.session.delete(review)
        db.session.commit()

        print(f'{review_title} has been deleted.')
        return {}, 200




