import base64
import json
from flask import url_for


def parse(response):
    return json.loads(response.data.decode('utf-8'))


def test_app(client, db, user_data):
    """
    Otestuje, ze nase aplikace dela co ma.
    """
    # Zalozime uzivatele.
    json_data = json.dumps({'username': user_data['username'], 'password': user_data['password']})
    response = client.post(url_for('user_create'), data=json_data, content_type='application/json')
    parsed_response = parse(response)
    # Uspesne jsme vytvorili uzivatele.
    assert parsed_response['status_code'] == 200
    # Mame nejake ID.
    assert parsed_response['id']
    user_id = parsed_response['id']

    # Zkusime se prihlasit pres HTTP Basic auth a ziskat token.
    login = base64.b64encode(bytes(user_data['username'] + ":" + user_data['password'], 'ascii')).decode('ascii')
    response = client.get(url_for('user_token'), headers={'Authorization': 'Basic ' + login})
    parsed_response = parse(response)
    # Uspesne jsme ziskali token.
    assert parsed_response['status_code'] == 200
    # Mame nejaky token.
    assert parsed_response['token']

    # Zkusime se dostat na nejakou zabezpecenou URL - pregenerovat token, ale pomoci tokenu.
    login = base64.b64encode(bytes(parsed_response['token'] + ":" , 'ascii')).decode('ascii')
    response = client.get(url_for('user_token'), headers={'Authorization': 'Basic ' + login})
    parsed_response = parse(response)
    # Uspesne jsme ziskali token.
    assert parsed_response['status_code'] == 200
    # Mame nejaky token.
    assert parsed_response['token']

    # Zkusime vylistovat vsechny uzivatele.
    parsed_response = parse(client.get(url_for('user_listing')))
    # Uspesne jsme vylistovali uzivatele.
    assert parsed_response['status_code'] == 200
    assert len(parsed_response['data']) == 1

    # Zkusime ziskat udaje prvniho uzivatele z predchoziho vypisu.
    parsed_response = parse(client.get(url_for('user', user_id=parsed_response['data'][0]['id'])))
    # Nasli jsme uzivatele.
    assert parsed_response['status_code'] == 200
    # Je to stjeny uzivatel ktereho jsme vytvorili.
    assert parsed_response['data']['username'] == user_data['username']