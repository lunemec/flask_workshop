from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def register_db(app):    
    db.init_app(app)
    # Alias pro snadny pristup.
    app.db = db