from main import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')


# Single Schema: Returns one user
user_schema = UserSchema()

# Multiple Schema: Returns multiple users
users_schema = UserSchema(many=True)
