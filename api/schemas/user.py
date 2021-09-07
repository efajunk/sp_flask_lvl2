from api import ma
from api.models.user import UserModel


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
