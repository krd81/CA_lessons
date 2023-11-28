from main import ma

class ActorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'gender', 'country', 'dob')


# Single Schema: Returns one actor
actor_schema = ActorSchema()

# Multiple Schema: Returns multiple actors
actors_schema = ActorSchema(many=True)
