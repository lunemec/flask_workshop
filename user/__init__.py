from flask import Blueprint
from flask_restful import Api

from .views import *


def register_user(app):

    api = Api(app, prefix='/user')
    api.add_resource(UserDetail, '/<int:user_id>', endpoint='user')
    api.add_resource(UserCreate, '/create', endpoint='user_create')
    api.add_resource(UserToken, '/token', endpoint='user_token')
    api.add_resource(UserListing, '/list', endpoint='user_listing')

    user_blueprint = Blueprint('web_user', __name__, template_folder='templates', url_prefix='/web/user')
    user_blueprint.add_url_rule('/list', view_func=user_listing, endpoint='web_user_listing')
    user_blueprint.add_url_rule('/<int:user_id>', view_func=user_detail, endpoint='web_user_detail')
    app.register_blueprint(user_blueprint)
