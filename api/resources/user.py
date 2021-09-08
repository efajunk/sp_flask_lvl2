from api import Resource, reqparse, db, auth
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            users = UserModel.query.all()
            return users_schema.dump(users), 200

        user = UserModel.query.get(user_id)
        if not user:
            return f"Author id={user_id} not found", 404

        return user_schema.dump(user), 200

    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        user = UserModel(user_data["username"], user_data["password"])
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201
