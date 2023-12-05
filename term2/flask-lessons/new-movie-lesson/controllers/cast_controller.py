# cast_controller allows movies to be connected with actors
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from main import db, unauthorised_user
# from models.movie import Movie
# from schemas.movie_schema import *
# from models.actor import Actor
# from schemas.actor_schema import *
from models.cast import Cast
from schemas.cast_schema import *


# from controllers.reviews_controller import reviews

cast = Blueprint('cast', __name__, url_prefix='/<int:movie>/cast')
unauthorised_user

# The POST route endpoint (ADD cast)
@cast.route('/', methods = ['POST'])
@jwt_required()
def add_cast(movie):
    new_cast = CastSchema().load(request.json)

    cast = Cast(
        actors_id = new_cast['actor_id'],
        movie_id = movie
    )

    db.session.add(cast)
    db.session.commit()
    return cast_schema.dump(cast), 201



# The POST route endpoint (DELETE cast)
@cast.route('/<int:cast_id>', methods = ['DELETE'])
@jwt_required()
def delete_cast(movie, cast_id):
    stmt = db.select(Cast).filter_by(id=cast_id)
    cast = db.session.scalar(stmt)
    if not cast:
        return {'message' : 'Cast ID not found - please try again'}, 404
    else:    
        db.session.delete(cast)
        db.session.commit()

        return {}, 200

