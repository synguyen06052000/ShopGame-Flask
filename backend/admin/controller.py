from flask import Blueprint, request
from .service import get_all_user, get_home_admin

admin = Blueprint("admin", __name__)

@admin.route("/admin", methods=["GET"])
def admin_home():
    return get_home_admin()

@admin.route("/admin/get-all-users", methods=["GET"])
def admin_get_all_users():
    return get_all_user()