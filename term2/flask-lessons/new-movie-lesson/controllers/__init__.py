from controllers.auth_controller import auth
from controllers.movies_controller import movies
from controllers.actors_controller import actors
from controllers.directors_controller import directors

registerable_controllers = [
    auth,
    movies,
    actors,
    directors
]