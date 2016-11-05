from base64 import b64encode, encodebytes
import json
import random

from flask import url_for


def help_http_basic_encode_header(s):
    return b64encode(s.encode()).decode('utf-8')


def help_http_basic_create_header(username, password):
    authorization_string = '{}:{}'.format(username, password)
    headers = {'Authorization': 'Basic ' + help_http_basic_encode_header(authorization_string)}
    return headers


def test_get_one(client, user, user_data):
    headers = help_http_basic_create_header(user_data['username'], user_data['password'])
    result_token = client.get(url_for('user_token'), headers=headers)

    headers = help_http_basic_create_header(json.loads(result_token.data.decode('utf-8'))['token'], '')
    result = client.get(url_for('user', user_id=user.id), headers=headers)

    json_data = json.loads(result.data.decode('utf-8'))
    assert json_data == {
        'status_code': 200, 
        'data': {'id': user.id, 'username': user.username, 'password_hash': user.password_hash}
    }


def test_not_found(client, user, user_data):
    headers = help_http_basic_create_header(user_data['username'], user_data['password'])
    result_token = client.get(url_for('user_token'), headers=headers)

    headers = help_http_basic_create_header(json.loads(result_token.data.decode('utf-8'))['token'], '')

    result = client.get(url_for('user', user_id=random.randint(10, 99999)), headers=headers)
    json_data = json.loads(result.data.decode('utf-8'))
    assert json_data == {'status_code': 404}


def test_unspecified_error(app, client):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/unknown.db'
    result = client.get(url_for('user', user_id=1))
    json_data = json.loads(result.data.decode('utf-8'))

    assert json_data['status_code'] == 500
    assert 'info' in json_data