import json

def test_hello_world(client):
    result = client.get('/')
    assert json.loads(result.data.decode('utf-8')) == {'data': 'Hello, world!'}