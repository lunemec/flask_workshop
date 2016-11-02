import json
from flask import url_for


def test_get_one(client, user):
    result = client.get(url_for('user', user_id=user.id))
    json_data = json.loads(result.data.decode('utf-8'))
    assert json_data == {'id': user.id, 'username': user.username, 'password_hash': user.password_hash}