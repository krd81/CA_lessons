from setup import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.cards_bp import cards_bp

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(cards_bp)


print(app.url_map)
# get_jwt_identity is a simple way to obtain the token, decode it and return the sub (i.e. subject) of the token