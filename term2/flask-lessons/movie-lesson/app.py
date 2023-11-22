from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError
# from jsonpickle import encode as json
from datetime import date, timedelta
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://tomato:abc123@127.0.0.1:5432/ripe_tomatoes_db"
app.config['JWT_SECRET_KEY'] = 'Ministry of Silly Walks' 

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    length = db.Column(db.String(5))
    year = db.Column(db.String(4))


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'genre', 'length', 'year')
        update_1 = ('id', 'title')
        update_2 = ('id', 'genre')
        update_3 = ('id', 'length')
        update_4 = ('id', 'year')


class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))
    gender = db.Column(db.String(15))
    country = db.Column(db.String(50))
    dob = db.Column(db.Date())


class ActorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'gender', 'country')


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), nullable = False, unique = True)
    password = db.Column(db.String(15), nullable = False)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')

@app.cli.command("db_create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")


@app.cli.command("db_seed")
def db_seed():
    movies = [
        Movie(
            title = "Barbie",
            genre = "Comedy",
            length = "114",
            year = "2023"
        ),
        Movie(
            title = "Oppenheimer",
            genre = "Drama",
            length = "180",
            year = "2023"
        ),
        Movie(
            title = "The Little Mermaid",
            genre = "Animation",
            length = "135",
            year = "2023"
        ),
        Movie(
            title = "Avatar: The Way of Water",
            genre = "Action",
            length = "192",
            year = "2022"
        ),]


    actors = [
        Actor(
            f_name = "Julia",
            l_name = "Roberts",
            gender = "Female",
            country = "USA",
            dob = "1967/10/28"
        ),
        Actor(
            f_name = "Tom",
            l_name = "Hanks",
            gender = "Male",
            country = "USA",
            dob = "1956/07/09"
        ),
       Actor(
            f_name = "Chloe Grace",
            l_name = "Moretz",
            gender = "Female",
            country = "USA",
            dob = "1997/02/10"
        ),
       Actor(
            f_name = "Matthew",
            l_name = "Perry",
            gender = "Male",
            country = "Canada",
            dob = "1969/08/19"
        ),
       Actor(
            f_name = "Adam",
            l_name = "Sandler",
            gender = "Male",
            country = "USA",
            dob = "1966/09/09"
        ),        
       Actor(
            f_name = "Margot",
            l_name = "Robbie",
            gender = "Female",
            country = "Australia",
            dob = "1990/07/02"
        ),]
    
    users = [
        User(
            username = 'admin',
            password = bcrypt.generate_password_hash('abc123').decode('utf8')
        ),

    ]


    db.session.add_all(movies)
    db.session.add_all(actors)
    db.session.add_all(users)
    db.session.commit()

    print("Database seeded")


@app.route('/movies')
def all_movies():
    # Select the required records
    results = db.select(Movie)
    movies = db.session.scalars(results).all()
    return MovieSchema(many=True).dump(movies)


@app.route('/actors')
def all_actors():
    # Select the required records
    results = db.select(Actor)
    actors = db.session.scalars(results).all()
    return ActorSchema(many=True).dump(actors)


@app.route('/auth/signup', methods = ['POST'])
def signup():
    try:
        current_user = UserSchema().load(request.json)
        if (len(current_user['password']) < 8):
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
            return {'token' : token, 'user' : UserSchema(exclude = ['password']).dump(user)}, 201
    except IntegrityError:
        return {'error' : 'Another user has already registered that username'}, 409
    


@app.route('/auth/signin', methods = ['POST'])
def signin():
    current_user = UserSchema().load(request.json)

    stmt = db.select(User).where(User.username == current_user['username'])
    user = db.session.scalar(stmt)

    if user and bcrypt.check_password_hash(user.password, current_user['password']):
        token = create_access_token(identity=user.username, additional_claims={'id': user.id}, expires_delta = timedelta(hours = 2))
        return {'token' : token, 'user' : UserSchema(exclude = ['password']).dump(user)}, 200
    else:
        return {'error' : 'Username or password is incorrect'}, 409


def update_records(table, record, column):
    stmt = db.select(table).where(table.id == record)
    record = db.session.scalar(stmt)


    pass


# Create delete method before attempting update
def delete_records():
    pass

@app.route('/movies/update/<int:movie_id>', methods = ['POST'])
@jwt_required()
def movie_update(movie_id):
    current_username = get_jwt_identity()
    stmt = db.select(User).filter_by(username = current_username)
    user = db.session.scalar(stmt)

    movie = db.select(Movie).filter_by(id = movie_id)

    update_request = MovieSchema().load(request.json)
    update_column = update_request['genre']

    if not user:
        return {'error': 'User not found'}
    else:
        # if not movie:
            # return {'error': 'Movie not found'}
        # else:
            update_records(Movie, movie.id, update_column)



# @app.route('/movies/delete/<int:id>', methods = ['DELETE'])
# @jwt_required()

@app.route('/')
def index():
    return 'Hello World!!'