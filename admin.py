from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app
from database import db

from user.models import User

admin = Admin(app, name='workshop', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))