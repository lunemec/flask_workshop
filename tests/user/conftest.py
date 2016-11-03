import pytest

from user.models import User

__all__ = ('user_data', 'user')


@pytest.fixture
def user_data():
    return {'username': 'Test client', 'password': 'my_awesome_password'}

@pytest.fixture
def user(db, user_data):
    user = User(username=user_data['username'])
    user.hash_password(user_data['password'])
    db.session.add(user)
    db.session.commit()
    return user