from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from user.models import User


def register_admin(app):
    admin = Admin(app, name='workshop', template_mode='bootstrap3')
    admin.add_view(ModelView(User, app.db.session))