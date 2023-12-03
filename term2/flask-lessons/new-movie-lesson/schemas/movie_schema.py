from main import ma
from marshmallow import fields, pre_load, post_load
from models.movies import Movie

class MovieSchema(ma.Schema):
    director = fields.Nested('DirectorSchema')
    reviews = fields.Nested('ReviewSchema', exclude=['movie'])
    class Meta:
        fields = ('id', 'title', 'genre', 'length', 'year', 'director', 'reviews')
        load_relationships = True

    @post_load
    def make_movie_process(self, data, many **kwargs):
        return Movie(**data)
        
    @pre_load
    def pre_load_process(self, data, many, **kwargs):
        director_id = data.get('director', {}).get('id')
        if director_id is None:
            return data
        return {"director_id" : director_id}


# Single Schema: Returns one movie
movie_schema = MovieSchema()

# Multiple Schema: Returns multiple movies
movies_schema = MovieSchema(many=True)

# Create/Edit Movie Schema
movie_schema_no_id = MovieSchema(exclude=['id'])

# Show reviews only
movie_reviews_schema = MovieSchema(many=True, only=['reviews'])