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

def get_home():
     return render_template("base.html",btn_login = "Đăng nhập", btn_register = "Đăng ký")
def get_form_register():
    return render_template("register.html")
def get_form_login():
    return render_template("login.html")

def handle_login_post():
    data = request.json
    print(request.json['username'], request.json['password'])
    if data:
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username).first()
        print(user.password, password)
        if user:
            # if check_password_hash(user.password, password):
            if user.password == password:
                session.permanent = True
                # login_user(user, remember=True)
                print("Login success!")
                return jsonify({"message": "Login success!"}), 200
            else:
                return jsonify({"message": "Wrong!"}), 400
        else:
            return jsonify({"message": "User exist!"}), 400
    return render_template("login.html", user=current_user)

def handle_register_post():
    data = request.json
    if data:
        username = request.json['username']
        password = request.json['password']
        phonenumber = request.json['phonenumber']
        balance = 0
        role = 0
        datejoin = datetime.today()
        # pwd = generate_password_hash(password, method="sha256")
        new_user = User(username, password, phonenumber, balance, role, datejoin)
        try:
            db.session.add(new_user)
            db.session.commit()
            print("Register success!")
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add user!"}), 400
    return render_template("register.html")
def get_user_by_id_service(id):
    user = User.query.get(id)
    if user:
        return user_schema.jsonify(user)
    else:
        return jsonify({"message": "Not found user"}), 404
