from flask import Blueprint, request, render_template
from .service import handle_register_post, get_form_register, get_home, get_form_login, handle_login_post, get_user_by_id_service
from os import path
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
