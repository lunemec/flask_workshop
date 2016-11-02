import pytest
import random

from user.control import get_user, list_users
from user.exceptions import UnspecifiedError, UserNotFound


def test_list_control(app, user):
    result = list_users()
    assert result == [{'id': 1, 'username': 'Test client'}]


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