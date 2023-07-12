from flask import Flask, request, Blueprint
from backend.user.controller import user
from backend.admin.controller import admin
from .extension import db, ma
from flask_sqlalchemy import SQLAlchemy
import os


def create_db(app):
    if not os.path.exists("backend/backend.db"):
        with app.app_context():
            db.create_all()
        print("Created db!")
def create_app(config_file = "config.py"):
    app = Flask(__name__,template_folder='templates', static_folder='static')
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(user)
    app.register_blueprint(admin)
    create_db(app)
    return app