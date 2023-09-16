from flask import Blueprint, request
from .service import get_all_user, get_home_admin, update_balance_for_user, get_add_acc, handle_post_add_acc, get_dashboard

admin = Blueprint("admin", __name__)

@admin.route("/admin", methods=["GET"])
def admin_home():
    return get_home_admin()

@admin.route("/admin/get-all-users", methods=["GET"])
def admin_get_all_users():
    return get_all_user()

@admin.route("/admin/dashboard", methods=["GET"])
def admin_get_dashboard():
    return get_dashboard()

@admin.route("/admin/update-balance/<int:id>", methods=["PUT"])
def admin_update_balance(id):
    return update_balance_for_user(id)
@admin.route("/admin/add-acc", methods=["GET", "POST"])
def admin_add_account():
    if request.method == "GET":
        return get_add_acc()
    elif request.method == "POST":
        return handle_post_add_acc()
