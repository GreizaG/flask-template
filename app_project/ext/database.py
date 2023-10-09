from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy's extension for database operations
db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
