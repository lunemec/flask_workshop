import pytest
import random
import time

from user.control import get_user, create_user, list_users, verify_password
from user.exceptions import UnspecifiedError, UserNotFound, InvalidArguments, UserAlreadyExists
from user.models import User


def test_list_control(app, user, user_data):
    result = list_users()
    assert result == [{'id': 1, 'username': user_data['username']}]


def test_user_not_found(app, user):
    with pytest.raises(UserNotFound):
        get_user(random.randint(10, 9999))


def test_unspecified_error(app, user):
    with pytest.raises(UnspecifiedError):
        get_user(None)

    
def test_user_found(app, user):
    data = get_user(user.id)
    assert data['id'] == user.id
    assert data['username'] == user.username
    assert data['password_hash'] == user.password_hash


def test_create_user(app, db, user_data):
    user_id = create_user(user_data['username'], user_data['password'])
    assert user_id is not None
    created_user_data = get_user(user_id)
    assert created_user_data['username'] == user_data['username']
    assert created_user_data['password_hash']


def test_create_user_invalid_arguments(app, db):
    with pytest.raises(InvalidArguments):
        create_user('username', None)


def test_create_user_already_exists(app, user):
    with pytest.raises(UserAlreadyExists):
        create_user(user.username, 'password')


def test_token_works(app, db, user_data):
    """
    Slozitejsi test, lepe popsat co dela:
        zalozime noveho uzivatele
        vygenerujeme novy token
        overime ze se s nim lze prihlasit
    """
    user_id = create_user(user_data['username'], user_data['password'])
    # Potrebujeme nacist model usera, ne jen dict jeho dat.
    user_model = User.query.get(user_id)
    token = user_model.generate_auth_token()
    token_valid = verify_password(token, None)
    assert token_valid


def test_token_expires(app, db, user_data):
    """
    Slozitejsi test, lepe popsat co dela:
        zalozime noveho uzivatele
        vygenerujeme novy token s platnosti 1s
        overime ze se s nim lze prihlasit
        pockame 2s
        overime ze se s nim uz nelze prihlasit
    """
    user_id = create_user(user_data['username'], user_data['password'])
    # Potrebujeme nacist model usera, ne jen dict jeho dat.
    user_model = User.query.get(user_id)
    token = user_model.generate_auth_token(expiration=1)
    token_valid = verify_password(token, None)
    assert token_valid
    # Na tohle v testech POZOR! 
    time.sleep(2)
    token_valid = verify_password(token, None)
    assert not token_valid