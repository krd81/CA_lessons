from flask import Blueprint, request
from models.users import User
from schemas.user_schema import *
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from datetime import date, timedelta
from main import db, ma, bcrypt
from flask_jwt_extended import create_access_token, jwt_required


users = Blueprint('users', __name__, url_prefix='/users')

# The GET routes endpoint (show all users)
@users.route('/')
def all_users():
    # Select the required records
    results = db.select(User)
    users = db.session.scalars(results).all()
    return users_schema.dump(users)


# The GET routes endpoint (show one user)
@users.route('/<int:user_id>')
def all_users(user_id):
    # Select the required records
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user:
        return {'message' : 'User ID not found - please try again'}, 404
    else:        
        return user_schema_private.dump(user), 200


# The POST route endpoint (add new user)
@users.route('/', methods = ['POST'])
@jwt_required()
def add_user():
    # *** RE-WRITE ***
    if not jwt_required():
        print('User is not logged in!')
        return {'message': 'You must be a registered user to perform this operation.'}, 422
    new_user = user_schema_pw.load(request.json)

    user = User(
        username = new_user['username'],
        password = bcrypt.generate_password_hash(['password']).decode('utf8')
    )
    db.session.add(user)
    db.session.commit()
    print(f'New user "{user.username}" added to database')

    return {'message': 'Success', 'user': user_schema_private.dump(user)}, 201


# The PUT route endpoint (EDIT user)
@users.route('/<int:user_id>', methods = ['PUT', 'PATCH'])
# @jwt_required()
def edit_user(user_id):
    edit_info = UserSchema(exclude=['id']).load(request.json)
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user:
        return {'message' : 'User ID not found - please try again'}, 404
    else:
        user.username = edit_info.get('username', user.username)
        user.password = edit_info.get('password', user.password)
        return user_schema_private.dump(user), 200



# The DELETE route endpoint
@users.route('/<int:user_id>', methods = ['DELETE'])
@jwt_required()
def delete_user(user_id):
    # *** RE-WRITE ***
    if not jwt_required():
        return {'message': 'You must be a registered user to perform this operation.'}, 422
    
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user:
        return {'message' : 'User ID not found - please try again'}, 404
    else:
        db.session.delete(user)
        return {'message' : f'{user.username} has been deleted.'}, 200


