from .exceptions import UserNotFound, UnspecifiedError
from .models import User


def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            raise UserNotFound()
        return {'id': user.id, 'username': user.username, 'password_hash': user.password_hash}
    except UserNotFound:
        raise
    except Exception as e:
        raise UnspecifiedError(e) 


def list_users():
    users = User.query.all()
    return [{'id': user.id, 'username': user.username} for user in users]