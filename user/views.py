from app import app

from flask import jsonify
from flask_restful import Resource

from .models import User

__all__ = ('hello_world', 'UserListing')

@app.route('/')
def hello_world():
    return jsonify({'data': 'Hello, world!'})


class UserListing(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'username': user.username} for user in users]