import os

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from app_project.ext.database import db

basedir = os.path.dirname(os.path.realpath(__file__))
MIGRATION_DIR = os.path.join(basedir, "../migrations")

# Initialize extensions here

# CORS (Cross-Origin Resource Sharing) extension for handling cross-origin requests
cors = CORS()

# Flask-Migrate extension for database migrations
migrate = Migrate()

# Flask-JWT-Extended extension for JSON Web Tokens (JWT) authentication
jwt = JWTManager()

# Flask-Bcrypt extension that provides bcrypt hashing utilities e.g. Your passwords
flask_bcrypt = Bcrypt()


# Talisman is a Flask extension for HTTP security headers.
# talisman = Talisman()

def init_app(app):
    cors.init_app(app)
    migrate.init_app(app, db, MIGRATION_DIR)
    jwt.init_app(app)
    flask_bcrypt.init_app(app)
    # talisman.init_app(app)
