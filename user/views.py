import traceback
from app import app

from flask import jsonify
from flask_restful import Resource

from .control import list_users, get_user
from .exceptions import UserNotFound, UnspecifiedError

__all__ = ('UserDetail', 'UserListing')


class UserDetail(Resource):
    def get(self, user_id):
        try:
            data = get_user(user_id)
            return {'status_code': 200, 'data': data}
        except UserNotFound:
            return {'status_code': 404}
        except UnspecifiedError as e:
            return {'status_code': 500, 'info': str(e)}


class UserListing(Resource):
    def get(self):
        return {'status_code': 200, 'data': list_users()}