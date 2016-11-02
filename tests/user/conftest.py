import pytest

from user.models import User


@pytest.fixture
def user(db):
    user = User(username='Test client', password_hash='some_awesome_hash') 
    db.session.add(user)
    db.session.commit()
    return user