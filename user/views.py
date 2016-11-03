import traceback
from app import app

from flask import jsonify, request
from flask_restful import Resource

from .control import list_users, get_user, create_user
from .exceptions import UserNotFound, UnspecifiedError, InvalidArguments, UserAlreadyExists

__all__ = ('UserDetail', 'UserCreate', 'UserListing')


class UserDetail(Resource):
    def get(self, user_id):
        try:
            data = get_user(user_id)
            return {'status_code': 200, 'data': data}
        except UserNotFound:
            return {'status_code': 404}
        except UnspecifiedError as e:
            return {'status_code': 500, 'info': str(e)}


class UserCreate(Resource):
    def post(self):
        if request.json is not None:
            username = request.json.get('username')
            password = request.json.get('password')
        else:
            return {'status_code': 400, 'info': 'JSON data not provided.'}
        try:
            user_id = create_user(username, password)
        except InvalidArguments:
            return {'status_code': 400, 'info': 'Username or password not provided.'}
        except UserAlreadyExists:
            return {'status_code': 400, 'info': 'User already exists.'}
        except UnspecifiedError as e:
            return {'status_code': 500, 'info': str(e)}

        return {'status_code': 200, 'id': user_id}


class UserListing(Resource):
    def get(self):
        return {'status_code': 200, 'data': list_users()}