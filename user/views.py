from app import app

from flask import jsonify

@app.route('/')
def hello_world():
    return jsonify({'data': 'Hello, world!'})