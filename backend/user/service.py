from backend.extension import db
from backend.backend_ma import UserSchema
from backend.model import User, Acc, Img
from datetime import datetime
from flask import request, jsonify, render_template, session, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import numpy as np
import json

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def get_home():
    return render_template("home.html", user=current_user,file_name1='home1.png')
   
def get_form_register():
    return render_template("register.html")
def get_form_login():
    return render_template("login.html")

def handle_login_post():
    msg_login_error = ""
    if request:
        username = request.form.get('username')
        password = request.form.get('password')
        if not username:
            msg_login_error = "Tài khoản không được bỏ trống"
        elif not password:
            msg_login_error = "Mật khẩu không được bỏ trống"
        else:
            user = User.query.filter_by(username=username).first()
            if user:
                # if check_password_hash(user.password, password):
                if user.password == password:
                    session.permanent = True
                    login_user(user, remember=True)
                    print("Login success", current_user)
                    return redirect(url_for("user.home"))
                else:
                    msg_login_error = "Mật khẩu không chính xác"
            else:
                msg_login_error = "Tài khoản không tồn tại"
    return render_template("login.html", msg_login_error = msg_login_error)

def handle_register_post():
    obj = db.session.query(User).order_by(User.id.desc()).first()
    print(obj)
    msg_register_error = ""
    if request:
        username = request.form.get('username')
        password = request.form.get('password')
        phonenumber = request.form.get('phonenumber')
        password_confirm = request.form.get('password-confirm')
        balance = 0
        role = 0
        datejoin = datetime.today()
        if not username:
            msg_register_error = "Tài khoản không được bỏ trống"
        elif not password:
            msg_register_error = "Tài khoản không được bỏ trống"
        elif not phonenumber:
            msg_register_error = "Hãy điền số điện thoại"
        elif password != password_confirm:
             msg_register_error = "Mật khẩu xác nhận không đúng"
        else:
            new_user = User(username, password, phonenumber, balance, role, datejoin)
            try:
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                print("Register success!")
                return redirect(url_for("user.home"))
            except IndentationError:
                db.session.rollback()
                msg_register_error = "Đăng ký thất bại"
        # pwd = generate_password_hash(password, method="sha256")
    return render_template("register.html", msg_register_error = msg_register_error)
def get_user_by_id_service(id):
    user = User.query.get(id)
    if user:
        return render_template("info_user.html", user = current_user)
    else:
        return jsonify({"message": "Not found user"}), 404

def user_logout():
    logout_user()
    return redirect(url_for("user.home"))

def update_password_by_id(id):
    msg_change_password_error = ""
    user = User.query.get(id)
    new_password = request.form.get("new-password")
    print("Mk ms:", new_password)
    if not new_password:
        msg_change_password_error = "Hãy điền mật khẩu mới"
    if user and new_password:
        try:
            user.password = new_password
            db.session.commit()
            print("Change password success")
            return redirect(url_for("user.home"))
        except IndentationError:
            db.session.rollback()
            msg_change_password_error = "Đổi mật khẩu thất bại!" 
    return render_template("change_password.html", msg_change_password_error = msg_change_password_error)
def get_change_password():
    return render_template("change_password.html",user = current_user)

def list_acc_service():
    imgs = []
    page = request.args.get('page',1,type=int)
    accounts = Acc.query.paginate(page = page, per_page = 8)
    for i in accounts.items:    
        weaponAcc = Img.query.filter_by(acc_id = i.id).first()
        imgs.append(weaponAcc)
    print(current_user)
    return render_template("list_acc.html", user = current_user, accounts = accounts, imgs = imgs)

def get_info_acc_by_id_service(id):
    acc = Acc.query.get(id)
    imgs = Img.query.filter_by(acc_id = id).all()
    return render_template("info_acc_by_id.html",user = current_user,acc = acc, imgs = imgs)
