from flask import Blueprint, request, render_template
from .service import handle_register_post, get_form_register, get_home, get_form_login, handle_login_post, get_user_by_id_service, user_logout, update_password_by_id, get_change_password, list_acc_service, get_info_acc_by_id_service
from os import path
from flask_login import login_required
user = Blueprint("user", __name__)

@user.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return get_form_login()
    else:
        return handle_login_post()

@user.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return get_form_register()
    elif request.method == 'POST':
        return handle_register_post()
@user.route("/", methods=['GET'])
def home():
    return get_home()

@user.route("/user/info/<int:id>", methods=["GET"])
def get_info_user_by_id(id):
    return get_user_by_id_service(id) 

@user.route("/logout")
def logout():
    return user_logout()

@user.route("/changepassword/<int:id>", methods=["GET", "POST"])
def change_password(id):
    if request.method == "GET":
        return get_change_password()
    else:
        return update_password_by_id(id)

@user.route("/list_acc", methods=["GET"])
def list_acc():
    return list_acc_service()

@user.route("/acc/<int:id>", methods=["GET"])
def get_info_acc_by_id(id):
    return get_info_acc_by_id_service(id)

