from main import ma
from marshmallow import fields


class MovieSchema(ma.Schema):
    director = fields.Nested('DirectorSchema', only=['name'])   
    reviews = fields.Nested('ReviewSchema', many=True, only=['user', 'message'])
    cast = fields.Nested('CastSchema', many=True, exclude=['movie_id'])

    class Meta:
        fields = ('id', 'title', 'genre', 'length', 'year', 'director_id', 'cast', 'reviews')




# Single Schema: Returns one movie
movie_schema = MovieSchema()

# Multiple Schema: Returns multiple movies
movies_schema = MovieSchema(many=True)

# Create/Edit Movie Schema
movie_schema_no_id = MovieSchema(exclude=['id'])
