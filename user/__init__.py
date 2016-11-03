from flask_restful import Api
from .views import *


def register_user(app):

    api = Api(app, prefix='/user')
    api.add_resource(UserDetail, '/<int:user_id>', endpoint='user')
    api.add_resource(UserCreate, '/create', endpoint='user_create')
    api.add_resource(UserToken, '/token', endpoint='user_token')
    api.add_resource(UserListing, '/list', endpoint='user_listing')