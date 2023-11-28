from flask import abort
from flask_jwt_extended import get_jwt_identity
from setup import db
from models.user import User


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