from main import ma
from marshmallow import fields

class ActorSchema(ma.Schema):
    cast = fields.Nested('CastSchema', many=True, only=['movie_id'])

    class Meta:
        fields = ('id', 'f_name', 'l_name', 'gender', 'country', 'dob', 'cast')


# Single Schema: Returns one actor
actor_schema = ActorSchema()

# Multiple Schema: Returns multiple actors
actors_schema = ActorSchema(many=True)

# Create/Edit Movie Schema
actor_schema_no_id = ActorSchema(exclude=['id'])