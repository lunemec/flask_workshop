from flask import Flask

from bootstrap import register_bootstrap
from log import register_log
from database import register_db
from user import register_user
from user.admin import register_admin


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'd76b9af7-0caf-4749-b671-65912beea187'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    register_bootstrap(app)
    register_log(app)
    register_db(app)
    register_user(app)
    register_admin(app)

    return app
