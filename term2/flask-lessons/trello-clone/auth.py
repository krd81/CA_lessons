from flask import abort
from flask_jwt_extended import get_jwt_identity, jwt_required
from setup import db
from models.user import User

@jwt_required()
def authorize(user_id=None):
     # Pseudo code to check is the user is an admin
    # 1. Get the identity of the user via the token
    jwt_user_id = get_jwt_identity()
    # 2. Compare user's email against the database
    stmt = db.select(User).filter_by(id=jwt_user_id)
    # 3.Create instance of user from the user retrieved from the database
    user = db.session.scalar(stmt)
    # 4. If user is not an admin, an error will be returned to the client
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        abort(401)