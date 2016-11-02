import json

def test_hello_world(app):
    result = app.get('/')
    assert json.loads(result.data.decode('utf-8')) == {'data': 'Hello, world!'}