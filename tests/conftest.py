import pytest

import workshop


@pytest.fixture
def app(request):
    workshop.app.config['TESTING'] = True
    return workshop.app.test_client()