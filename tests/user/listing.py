import json

from flask import url_for


def test_list_empty(db, client):
    result = client.get(url_for('user_listing'))
    assert json.loads(result.data.decode('utf-8')) == []


def test_list_one(client, user):
    result = client.get(url_for('user_listing'))
    json_data = json.loads(result.data.decode('utf-8'))
    assert len(json_data) == 1
    assert json_data[0]['username'] == user.username