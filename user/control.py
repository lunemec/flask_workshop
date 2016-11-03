from app import app
from auth import auth
from database import db

from .exceptions import UserNotFound, UnspecifiedError, InvalidArguments, UserAlreadyExists
from .models import User


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


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


def create_user(username, password):
    try:
        if username is None or password is None:
            raise InvalidArguments('Username or password not provided.')

        if User.query.filter_by(username = username).first() is not None:
            raise UserAlreadyExists()

        user = User(username = username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return user.id
    except (InvalidArguments, UserAlreadyExists):
        raise
    except Exception as e:
        app.logger.exception('Error while creating user.', extra={'username': username})
        raise UnspecifiedError(e)