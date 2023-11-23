from flask import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.card import Card, CardSchema
from models.user import User
from setup import *
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp


def admin_required():
     # Pseudo code to check is the user is an admin
    # 1. Get the identity of the user via the token
    user_email = get_jwt_identity()
    # 2. Compare user's email against the database
    stmt = db.select(User).where(User.email == user_email)
    # 3.Create instance of user from the user retrieved from the database
    user = db.session.scalar(stmt)
    # 4. If user is not an admin, an error will be returned to the client
    if not user.is_admin:
        return abort(401)

@app.errorhandler(401)
def unauthorised(err):
    return {'error': "You are not authorised to access this resource"}

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)

@app.route('/cards')
@jwt_required()
def all_cards():
    admin_required()
    # select * from cards;
    stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 0)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)



@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

# get_jwt_identity is a simple way to obtain the token, decode it and return the sub (i.e. subject) of the token