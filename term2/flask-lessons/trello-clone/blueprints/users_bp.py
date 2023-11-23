from flask import Blueprint, request
from flask import request
from models.user import User, UserSchema
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from setup import db, bcrypt

users_bp = Blueprint('users', __name__, url_prefix="/users")


# Routes need to have a resource type
# This is an entity that is being tracked by the api
@users_bp.route('/register', methods = ['POST'])
def register():
    try:
        # Parse the incoming POST body through the schema
        user_info = UserSchema(exclude = ['id', 'is_admin']).load(request.json)
        
        # Create a new user with the parsed data
        user = User(
            email = user_info['email'],
            password = bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
            name = user_info.get('name', '')
        )
        
        # Add and commit the new user to the database
        db.session.add(user)
        db.session.commit()

        print(user.__dict__)
        # Return the new user
        return UserSchema(exclude = ['password']).dump(user), 201
    except IntegrityError:
        return {'error' : 'Email address already in use'}, 409


@users_bp.route('/login', methods = ['POST'])
def login():
    # 1. Parse incoming POST body through the schema
    user_info = UserSchema(exclude=['id', 'name', 'is_admin']).load(request.json)
    # 2. Select user with email that matches the one in the POST body
    stmt = db.select(User).where(User.email == user_info['email'])
    user = db.session.scalar(stmt)
    # 3. Check password hash
    if user and bcrypt.check_password_hash(user.password, user_info['password']):
        # 4. Create JWT token NOTE: additional fields can be added in the additional claims, if unsure what to include in token
        # token = create_access_token(identity=user.email, additional_claims={'email': user.email, 'name': user.name})
        token = create_access_token(identity=user.email, expires_delta = timedelta(hours = 2))

        # 5. Return the token (to the client) - use dictionary so that both token and user can be returned
        return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
    else:
        return {'error' : 'Invalid email or password'}, 401
    
