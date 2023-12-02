from main import ma
from marshmallow import fields

class ReviewSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])
    movie = fields.Nested('MovieSchema', only=['title'])

    class Meta:
        fields = ('id', 'message', 'user', 'movie')


review_schema = ReviewSchema()

reviews_schema = ReviewSchema(many=True)
