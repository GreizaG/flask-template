from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app_project.ext.database import db
from app_project.models.user import User

admin = Admin()


def init_app(app):
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin.name = 'Flask Admin'
    admin.template_mode = 'bootstrap3'
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
