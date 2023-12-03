'''
TO DO:
[x] All controllers require view 1 item and an UPDATE endpoint
[x] Change the DB query in each to be filter instead of where
[x] Add authentication to create/edit/delete routes
[ ] Add search function to each of the controllers
[x] Add schema to exclude 'id' and anything else that shouldn't be changed
[ ] Add director CRUD routes (list directors with their films)
[ ] Find code to control what attribute is returned from get_jwt_identity()
[x] Print routes command: print(app.url_map)
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)
    # configuring our app:
    app.config.from_object('config.app_config')
    # creating our database object! This allows us to use our ORM
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    # import the controllers and activate the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    print(app.url_map)

    return app

# Token exists but is incorrect/expired
@jwt.invalid_token_loader
# Token not present
@jwt.unauthorized_loader
def unauthorised_user(error):
    print(error)
    return {'error': 'User is unauthorised'}, 401
