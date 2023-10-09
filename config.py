import os


class Config:
    """Common configurations"""
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:////tmp/test.db").replace("postgres://", "postgresql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')  # Set the JWT secret key for authentication
    SECRET_KEY = os.getenv("FLASK_APP_SECRET_KEY")  # Set the secret key for the Flask App
    STATIC_FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))  # Define the directory for static files
    PORT = int(os.getenv('PORT', 3001))  # Set the port for the application, default is 3001


class DevelopmentConfig(Config):
    """Configuration settings for development"""
    DEBUG = True


class ProductionConfig(Config):
    """Configuration settings for development"""
    DEBUG = False


class TestingConfig(Config):
    """Configuration settings for development"""
    pass


config_by_name = {
    'development': DevelopmentConfig,  # Development configuration
    'production': ProductionConfig,  # Production configuration
    'testing': TestingConfig  # Testing configuration
}
