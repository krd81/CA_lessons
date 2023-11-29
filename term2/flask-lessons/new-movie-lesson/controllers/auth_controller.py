from flask import Blueprint, request
from models.users import User
from schemas.user_schema import *
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from datetime import date, timedelta
from main import db, bcrypt
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/auth')

# Signup/Regiser: POST route endpoint
@auth.route('/signup', methods = ['POST'])
def signup():
    try:
        current_user = user_schema_pw.load(request.json)
        if (len(current_user['password']) < 8 or len(current_user['password']) > 12):
            return {'error' : 'Password must be between 8 and 12 characters long'}, 409
        else:
            # Create new user
            user = User(
                username = current_user['username'],
                password = bcrypt.generate_password_hash(current_user['password']).decode('utf8')
            )
            # Add and commit the new user to the database
            db.session.add(user)
            db.session.commit()

            token = create_access_token(identity=user.username, additional_claims={'id': user.id}, expires_delta = timedelta(hours = 2))
            # Return JWT / user        
            return {'token' : token, 'user' : user_schema_private.dump(user)}, 201
    except IntegrityError:
        return {'error' : 'Another user has already registered that username'}, 409
    

# Signin / Login: POST route endpoint
@auth.route('/signin', methods = ['POST'])
def signin():
    current_user = UserSchema().load(request.json)

    stmt = db.select(User).where(User.username == current_user['username'])
    user = db.session.scalar(stmt)

    if user and bcrypt.check_password_hash(user.password, current_user['password']):
        token = create_access_token(identity=user.username, additional_claims={'id': user.id}, expires_delta = timedelta(hours = 2))
        return {'token' : token, 'user' : user_schema_private.dump(user)}, 200
    else:
        return {'error' : 'Username or password is incorrect'}, 409
