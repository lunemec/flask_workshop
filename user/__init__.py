from flask_restful import Api

from app import app
from .views import *

api = Api(app, prefix='/user')
api.add_resource(UserListing, '/listing', endpoint='user_listing')