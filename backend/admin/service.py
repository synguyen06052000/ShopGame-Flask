from backend.extension import db
from backend.backend_ma import UserSchema
from backend.model import User
from datetime import datetime
from flask import request, jsonify, render_template, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import json

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def get_home_admin():
    return render_template("admin.html")

def get_all_user():
    users = User.query.all()
    if users:
        data = users_schema.jsonify(users)
        return render_template("admin",)
    else:
        return jsonify({"message": "Not found books!"}), 404