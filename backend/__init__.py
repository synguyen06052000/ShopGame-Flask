from flask import Flask, request, Blueprint
from backend.user.controller import user
from backend.admin.controller import admin
from flask_login import LoginManager, login_manager
from .extension import db, ma
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import timedelta
import os

upload_folder = os.path.join('static', 'Image')


def create_db(app):
    if not os.path.exists("backend/backend.db"):
        with app.app_context():
            db.create_all()
        print("Created db!")
def create_app(config_file = "config.py"):
    app = Flask(__name__,template_folder='templates', static_folder='static')
    CORS(app = app)
    app.config.from_pyfile(config_file)
    app.config['UPLOAD_FOLDER'] = upload_folder
    db.init_app(app)
    ma.init_app(app)
    
    from .model import User
    
    app.register_blueprint(user)
    app.register_blueprint(admin)
    create_db(app)
    
    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)
    app.permanent_session_lifetime = timedelta(days=0, seconds=0, microseconds=0, milliseconds=10, minutes=0, hours=0, weeks=0)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
 
    return app