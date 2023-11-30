from main import ma

class DirectorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'country')


# Single Schema: Returns one director
director_schema = DirectorSchema()

# Multiple Schema: Returns multiple actors
directors_schema = DirectorSchema(many=True)

# Create/Edit Movie Schema
director_schema_no_id = DirectorSchema(exclude=['id'])