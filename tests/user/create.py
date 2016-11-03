import json
from flask import url_for


def test_create_user(client, db, user_data):
    json_data = json.dumps({'username': user_data['username'], 'password': user_data['password']})
    response =  client.post(url_for('user_create'), data=json_data, content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))
    assert json_response['status_code'] == 200
    assert json_response['id'] == 1


def test_create_not_json(client, db, user_data):
    response = client.post(url_for('user_create'))
    json_response = json.loads(response.data.decode('utf-8'))

    assert json_response['status_code'] == 400
    assert json_response['info'] == 'JSON data not provided.'


def test_create_user_exists(client, user, user_data):
    json_data = json.dumps({'username': user_data['username'], 'password': user_data['password']})
    response =  client.post(url_for('user_create'), data=json_data, content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))
    assert json_response['status_code'] == 400
    assert json_response['info'] == 'User already exists.'


def test_create_user_no_password(client, db, user_data):
    json_data = json.dumps({'username': user_data['username']})
    response =  client.post(url_for('user_create'), data=json_data, content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))
    assert json_response['status_code'] == 400
    assert json_response['info'] == 'Username or password not provided.'