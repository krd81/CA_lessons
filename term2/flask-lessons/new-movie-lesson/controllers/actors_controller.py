from flask import Blueprint, request
from main import db, unauthorised_user
from models.actor import Actor
from schemas.actor_schema import *
from flask_jwt_extended import jwt_required

actors = Blueprint('actors', __name__, url_prefix='/actors')
unauthorised_user

# The GET route endpoint (get ALL actors)
@actors.route('/')
def all_actors():
    # Select the required records
    results = db.select(Actor)
    actors = db.session.scalars(results).all()
    return actors_schema.dump(actors)


# The GET route endpoint (get one actor)
@actors.route('/<int:actor_id>')
def get_actor(actor_id):
    stmt = db.select(Actor).filter_by(id=actor_id)
    actor = db.session.scalar(stmt)
    if not actor:
        return {'message' : 'Actor ID not found - please try again'}, 404
    else:
        return actor_schema.dump(actor), 200



# The POST route endpoint (ADD actor)
@actors.route('/', methods = ['POST'])
@jwt_required()
def add_actor():
    new_actor = actor_schema_no_id.load(request.json)

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

    return actor_schema.dump(actor), 201

# The PUT route endpoint (EDIT actor)
@actors.route('/<int:actor_id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def edit_actor(actor_id):
    update_info = actor_schema_no_id.load(request.json)
    stmt = db.select(Actor).filter_by(id=actor_id)
    actor = db.session.scalar(stmt)
    if not actor:
        return {'message' : 'Actor ID not found - please try again'}, 404
    else:
        actor.f_name = update_info.get('f_name', actor.f_name)
        actor.l_name = update_info.get('l_name', actor.l_name)
        actor.gender = update_info.get('gender', actor.gender)
        actor.country = update_info.get('country', actor.country)
        actor.dob = update_info.get('dob', actor.dob)
        db.session.commit()
        print(f'{actor.f_name} {actor.l_name} has been updated.')
        return actor_schema.dump(actor), 200

    


# The DELETE route endpoint
@actors.route('/<int:actor_id>', methods = ['DELETE'])
@jwt_required()
def delete_actor(actor_id):
    
    stmt = db.select(Actor).filter_by(id=actor_id)
    actor = db.session.scalar(stmt)
    if not actor:
        return {'message' : 'Actor ID not found - please try again'}, 404
    else:
        actor_name = f'{actor.f_name} {actor.l_name}'
        db.session.delete(actor)
        db.session.commit()
        print(f'{actor_name} has been deleted.')
        return {}, 200
