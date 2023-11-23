from flask import Flask, request
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
        fields = ('id', 'f_name', 'l_name', 'gender', 'country', 'dob')


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)


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
            # password = 'abc123'
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


# @app.route('/movies/update')
# @jwt_required()

@app.route('/movies/add', methods = ['POST'])
def add_movie():
    new_movie = MovieSchema().load(request.json)

    movie = Movie(
        title = new_movie['title'],
        genre = new_movie['genre'],
        length = new_movie['length'],
        year = new_movie['year']
    )
    db.session.add(movie)
    db.session.commit()
    print(f'New movie "{movie.title}" added to database')

    return {'message': 'Success', 'movie': MovieSchema().dump(movie)}, 201


@app.route('/actors/add', methods = ['POST'])
def add_actor():
    new_actor = ActorSchema().load(request.json)

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

    return {'message': 'Success', 'actor': ActorSchema().dump(actor)}, 201



@app.route('/')
def index():
    return 'Hello World!!'