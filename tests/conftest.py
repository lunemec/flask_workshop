import pytest

from database import db as test_db
import workshop

from tests.user.conftest import *

TEST_DB = 'sqlite://'


@pytest.yield_fixture
def app(request):
    with workshop.app.test_request_context():
        workshop.app.config['TESTING'] = True
        yield workshop.app


@pytest.yield_fixture
def db(request, app):
    app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB

    test_db.init_app(app)
    test_db.create_all()
    yield test_db


@pytest.fixture
def client(request, app):
    return app.test_client()