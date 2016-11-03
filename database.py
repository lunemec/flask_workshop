from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def register_db(app):    
    db.init_app(app)
    migrate.init_app(app, db)
    # Alias pro snadny pristup.
    app.db = db
