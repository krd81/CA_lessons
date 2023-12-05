from main import ma
from marshmallow import fields

class CastSchema(ma.Schema):
    actors = fields.Nested('ActorSchema', only=['f_name', 'l_name']) 
    movies = fields.Nested('MovieSchema', only=['title']) 
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'title')

# Single Schema: returns cast of one movie
cast_schema = CastSchema()
