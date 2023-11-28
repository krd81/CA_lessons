from flask import Blueprint, request
from main import db
from models.actors import Actor
from schemas.actor_schema import actor_schema, actors_schema
from flask_jwt_extended import jwt_required

actors = Blueprint('actors', __name__, url_prefix='/actors')

# The GET route endpoint
@actors.route('/')
def all_actors():
    # Select the required records
    results = db.select(Actor)
    actors = db.session.scalars(results).all()
    return actors_schema.dump(actors)


# The POST route endpoint
@actors.route('/', methods = ['POST'])
@jwt_required()
def add_actor():
    if not jwt_required():
        return {'message': 'You must be a registered user to perform this operation.'}, 422
    new_actor = actor_schema.load(request.json)

    actor = Actor(
        f_name = new_actor['f_name'],
        l_name = new_actor['l_name'],
        gender = new_actor['gender'],
        country = new_actor['country'],
        dob = new_actor['dob']
    )

    db.session.add(actor)
    db.session.commit()
    print(f'New actor "{actor.f_name} {actor.l_name}" added to database')

    return {'message': 'Success', 'actor': actor_schema.dump(actor)}, 201




# The DELETE route endpoint
@actors.route('/<int:actor_id>', methods = ['DELETE'])
@jwt_required()
def delete_actor(actor_id):
    
    stmt = db.select(Actor).where(Actor.id == actor_id)
    actor = db.session.scalar(stmt)
    if not actor:
        return {'message' : 'Actor ID not found - please try again'}, 404
    actor_name = f'{actor.f_name} {actor.l_name}'
    db.session.delete(actor)

    return {'message' : f'{actor_name} has been deleted.'}, 200
