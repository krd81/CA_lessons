from flask import Blueprint, request
from main import db, unauthorised_user
from models.director import Director
from schemas.director_schema import *
from flask_jwt_extended import jwt_required

directors = Blueprint('directors', __name__, url_prefix='/directors')
unauthorised_user

# The GET route endpoint (get ALL directors)
@directors.route('/')
def all_directors():
    # Select the required records
    results = db.select(Director)
    directors = db.session.scalars(results).all()
    return directors_schema.dump(directors)


# The GET route endpoint (get one director)
@directors.route('/<int:director_id>')
def get_director(director_id):
    stmt = db.select(Director).filter_by(id=director_id)
    director = db.session.scalar(stmt)
    if not director:
        return {'message' : 'Director ID not found - please try again'}, 404
    else:
        return director_schema.dump(director), 200



# The POST route endpoint (ADD director)
@directors.route('/', methods = ['POST'])
@jwt_required()
def add_director():
    new_director = director_schema_no_id.load(request.json)

    director = Director(
        name = new_director['name'],
        country = new_director['country']
    )

    db.session.add(director)
    db.session.commit()
    print(f'New director "{director.name}" added to database')

    return director_schema.dump(director), 201

# The PUT route endpoint (EDIT director)
@directors.route('/<int:director_id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def edit_director(director_id):
    update_info = director_schema_no_id.load(request.json)
    stmt = db.select(Director).filter_by(id=director_id)
    director = db.session.scalar(stmt)
    if not director:
        return {'message' : 'Director ID not found - please try again'}, 404
    else:
        director.name = update_info.get('name', director.name)
        director.country = update_info.get('country', director.country)
        db.session.commit()
        print(f'"{director.name}" has been updated.')
        return director_schema.dump(director), 200

    


# The DELETE route endpoint
@directors.route('/<int:director_id>', methods = ['DELETE'])
@jwt_required()
def delete_director(director_id):
    
    stmt = db.select(Director).filter_by(id=director_id)
    director = db.session.scalar(stmt)
    if not director:
        return {'message' : 'Director ID not found - please try again'}, 404
    else:
        director_name = f'{director.name}'
        db.session.delete(director)
        db.session.commit()
        print(f'{director_name} has been deleted.')
        return {}, 200
