from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError
# from jsonpickle import encode as json
from datetime import date, timedelta
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://tomato:abc123@127.0.0.1:5432/ripe_tomatoes_db"
# app.config['JWT_SECRET_KEY'] = 'Ministry of Silly Walks' 




db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)












@app.errorhandler(422)
def unauthorised(err):
    
    return {'message': err.message}



@app.route('/')
def index():
    return 'Hello World!!'