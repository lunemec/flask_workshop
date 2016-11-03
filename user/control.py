from app import app

from .exceptions import UserNotFound, UnspecifiedError
from .models import User


def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            raise UserNotFound()
        return {'id': user.id, 'username': user.username, 'password_hash': user.password_hash}
    except UserNotFound:
        app.logger.info('User not found.', extra={'id': user_id})
        raise
    except Exception as e:
        app.logger.exception('Error while getting user.', extra={'id': user_id})
        raise UnspecifiedError(e) 


def list_users():
    users = User.query.all()
    return [{'id': user.id, 'username': user.username} for user in users]