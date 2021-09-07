from api import api, app
from api.resources.quote import QuoteResource
from api.resources.author import AuthorResource
from api.resources.user import UserResource
from config import Config


api.add_resource(QuoteResource,
                 '/authors/<int:author_id>/quotes/<int:quote_id>',
                 '/authors/<int:author_id>/quotes',
                 '/quotes'
                 )
api.add_resource(AuthorResource,
                 '/authors/<int:author_id>',
                 '/authors')
api.add_resource(UserResource,
                 '/user/<int:user_id>',
                 '/users')

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
