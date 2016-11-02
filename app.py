from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd76b9af7-0caf-4749-b671-65912beea187'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)