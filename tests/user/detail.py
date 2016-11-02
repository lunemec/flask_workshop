import json
import random
from flask import url_for


def test_get_one(client, user):
    result = client.get(url_for('user', user_id=user.id))
    json_data = json.loads(result.data.decode('utf-8'))
    assert json_data == {
        'status_code': 200, 
        'data': {'id': user.id, 'username': user.username, 'password_hash': user.password_hash}
    }


def test_not_found(client, user):
    result = client.get(url_for('user', user_id=random.randint(10, 99999)))
    json_data = json.loads(result.data.decode('utf-8'))
    assert json_data == {'status_code': 404}


def test_unspecified_error(client):
    result = client.get(url_for('user', user_id=1))
    json_data = json.loads(result.data.decode('utf-8'))

    assert json_data['status_code'] == 500
    assert 'info' in json_data