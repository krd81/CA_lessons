from flask import Blueprint, request
from main import db, unauthorised_user
from models.review import Review
from schemas.review_schema import *
from flask_jwt_extended import jwt_required, get_jwt_identity
# NEEDS FURTHER WORK TO UPDATE ROUTES TO INCLUDE MOVIE ID #

reviews = Blueprint('reviews', __name__, url_prefix='/<int:reviewed_movie_id>/reviews')
unauthorised_user

# The GET route endpoint (ALL reviews for an individual movie)
@reviews.route('/')
def all_reviews(reviewed_movie_id):
    # Select the required records
    stmt = db.select(Review).filter_by(movie_id=reviewed_movie_id)
    reviews = db.session.scalars(stmt).all()
    return reviews_schema.dump(reviews)

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
def add_review(reviewed_movie_id):
    new_review = ReviewSchema(exclude=['id']).load(request.json)
    review = Review(
        message = new_review['message'],
        user_id = get_jwt_identity(),
        movie_id = reviewed_movie_id
    )
    db.session.add(review)
    db.session.commit()
    print(f'New review for "{review.movie}" added to database')

    return review_schema.dump(review), 201


# The PUT route endpoint (EDIT review)
@reviews.route('/<int:review_id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def edit_review(reviewed_movie_id, review_id):
    update_info = review_schema.load(request.json)
    stmt = db.select(Review).filter_by(id=review_id)
    review = db.session.scalar(stmt)
    if not review:
        return {'message' : 'Review ID not found - please try again'}, 404
    else:
        review.message = update_info.get('message', review.message)
        # Movie cannot be changed - if the movie was wrong, the review would need to be deleted and re-created 
        # review.movie = update_info.get('movie', review.movie)         
        db.session.commit()
        print(f'Review {review.id} for {review.movie} has been updated.')
        return review_schema.dump(review), 200



# The DELETE route endpoint
@reviews.route('/<int:review_id>', methods = ['DELETE'])
@jwt_required()
def delete_review(reviewed_movie_id, review_id): 
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




