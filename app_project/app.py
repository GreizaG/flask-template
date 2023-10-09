import os

from flask import Flask

from app_project.ext import admin
from app_project.ext import database
from app_project.ext import extensions
from app_project.routes.root_routes import root_bp, root_bp_api_v1
from config import config_by_name


def create_app(config_mode='development'):
    """
    Create and configure the Flask application.

    Args:
        config_mode (str): The name of the configuration to use (default is 'development').

    Returns:
        Flask: The configured Flask app.

    Example:
        ```
        app = create_app('production')
        app.run()
        ```

    Configuration names:
    - 'development': Development configuration.
    - 'production': Production configuration.
    - 'testing': Testing configuration.
    """
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_mode])
    app.url_map.strict_slashes = True

    database.init_app(app)
    extensions.init_app(app)
    admin.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app):
    """
    Register Flask Blueprints with the app_project.

    :param app: The Flask app_project instance.
    """
    app.register_blueprint(root_bp_api_v1)
    app.register_blueprint(root_bp)


# This will only run if we execute 'python app_project/app.py' directly
if __name__ == '__main__':
    # You can set the FLASK_CONFIG environment variable
    config_name = os.getenv('FLASK_CONFIG', 'development')
    app = create_app(config_name)
    # Use the PORT configuration from the app's configration object
    PORT = app.config.get('PORT', 3001)
    app.run(host='0.0.0.0', port=PORT, debug=app.config.get('DEBUG', True))
