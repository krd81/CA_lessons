from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length
from flask_jwt_extended import create_access_token, jwt_required


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default='Anonymous')
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    cards = db.relationship('Card', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')


class UserSchema(ma.Schema):
    # cards = fields.List(fields.Nested('CardSchema', exclude=['user']))
    cards = fields.Nested('CardSchema', exclude=['user'], many=True)
    email = fields.Email(required=True) # This validates the incoming data via load(request.json) is correct
    password =fields.String(required=True, validate=Length(min=8, error='Password must be 8 least 8 characters'))

    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'cards')

