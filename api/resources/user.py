from api import Resource, reqparse, db
from api.models.user import UserModel

class UserResource(Resource):
    def post(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        username = UserModel(user_data["username"], user_data["password"])
        db.session.add(username)
        db.session.commit()
        return