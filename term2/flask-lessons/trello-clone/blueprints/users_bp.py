from flask import Blueprint, request
from models.user import User, UserSchema
from flask_jwt_extended import create_access_token, jwt_required
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from setup import db, bcrypt
from auth import admin_required

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
        token = create_access_token(identity=user.id, expires_delta = timedelta(hours = 2))

        # 5. Return the token (to the client) - use dictionary so that both token and user can be returned
        return {'token': token, 'user': UserSchema(exclude=['password', 'cards']).dump(user)}
    else:
        return {'error' : 'Invalid email or password'}, 401
    

# Get all users
@users_bp.route('/')
@jwt_required()
def all_users():
    admin_required()
    # select * from users;
    # stmt = db.select(User).where(db.or_(User.status != 'Done', User.id > 0)).order_by(User.title.desc())
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=['password']).dump(users)

# Get one user
@users_bp.route('/<int:id>')
@jwt_required()
def one_user(id):
    stmt = db.select(User).filter_by(id=id) # same as .where(User.id == id)
    user = db.session.scalar(stmt)
    if user:
        # print(user.User)
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': 'User not found'}, 404
