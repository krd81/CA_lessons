from main import ma
from marshmallow import fields

class DirectorSchema(ma.Schema):
    movies = fields.Nested('MovieSchema', many=True, only=['title'])
    class Meta:
        fields = ('id', 'name', 'country', 'movies')


# Single Schema: Returns one director
director_schema = DirectorSchema()

# Multiple Schema: Returns multiple directors ???
directors_schema = DirectorSchema(many=True)

# Create/Edit Director Schema
director_schema_no_id = DirectorSchema(exclude=['id'])

# Name only
director_schema_name = DirectorSchema(only=['name'])