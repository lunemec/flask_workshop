import json

from flask import url_for


def test_list_empty(db, client):
    result = client.get(url_for('user_listing'))
    assert json.loads(result.data.decode('utf-8')) == {'status_code': 200, 'data': []}


def test_list_one(client, user):
    result = client.get(url_for('user_listing'))
    json_data = json.loads(result.data.decode('utf-8'))
    assert json_data['status_code'] == 200
    assert len(json_data['data']) == 1
    assert json_data['data'][0]['username'] == user.username