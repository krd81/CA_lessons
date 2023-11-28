from main import ma

class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'genre', 'length', 'year')

# Single Schema: Returns one movie
movie_schema = MovieSchema()

# Multiple Schema: Returns multiple movies
movies_schema = MovieSchema(many=True)