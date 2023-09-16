from backend.extension import db
from backend.backend_ma import UserSchema
from backend.model import User, Img, Acc
from datetime import datetime
from flask import request, jsonify, render_template, session, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import json
import base64
from io import BytesIO
import os
import imgbbpy
import shutil

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii') 
    return render_pic

def get_home_admin():
    return render_template("admin.html")
def get_dashboard():
    users = User.query.all()
    currentMonth = datetime.now().month
    countUserCurrent = 0
    for user in users:
        print("User:", user.datejoin.month)
        if user.datejoin.month == currentMonth:
             countUserCurrent += 1
    print("User moi dang ky: ", countUserCurrent)
    return render_template("admin_dashboard.html", total_acc = countUserCurrent)

def get_data_json():
    users = User.query.all()
    if users:
        return users_schema.jsonify(users)

def get_all_user():
    users = User.query.all()
    # jsonData = json.dumps(users)
    print(get_data_json())
    if users:
        return render_template("admin_get_all_users.html", jsondata = users)
        # return render_template("admin",)
    else:
        return jsonify({"message": "Not found books!"}), 404
    
def get_add_acc():
    str_id_acc = ""
    lastAcc = db.session.query(Acc).order_by(Acc.id.desc()).first()
    if lastAcc:
        id_acc = lastAcc.id + 1
    else:
        id_acc = 1
    str_id_acc = str(id_acc)
    return render_template("admin_add_acc.html", id_acc=str_id_acc)

def handle_post_add_acc():
    priceAcc = request.form.get("price-acc")
    classAcc = request.form.get("class-acc")
    rankAcc = request.form.get("rank-acc")
    serverAcc = request.form.get("server-acc")
    cardAcc = request.form.get("card-acc")
    weaponAcc = request.form.get("weapon-acc")
    levelAcc = request.form.get("level-acc")
    hotDessAcc = request.form.get("hot-des-acc")
    
    newAcc = Acc(classAcc, rankAcc, priceAcc, serverAcc, cardAcc, weaponAcc, levelAcc, hotDessAcc)
    db.session.add(newAcc)
    db.session.commit()
    
    lastAcc = db.session.query(Acc).order_by(Acc.id.desc()).first()
    
    directory_img = str(lastAcc.id)
    path = os.path.join('backend','static', 'Image', directory_img)
    os.makedirs(path)
    
    file1 = request.files["uploaded-file1"]
    file2 = request.files["uploaded-file2"]
    file3 = request.files["uploaded-file3"]
    file4 = request.files["uploaded-file4"]
    
    
    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)
    filename3 = secure_filename(file3.filename)
    filename4 = secure_filename(file4.filename)
   
    
    #save local
    file1.save(os.path.join(path, filename1))
    file2.save(os.path.join(path, filename2))
    file3.save(os.path.join(path, filename3))
    file4.save(os.path.join(path, filename4))
   
    #upload imgbb
    client = imgbbpy.SyncClient('ffbdad501d7316f58281c592a65a955f')
    image1 = client.upload(file=os.path.join(path, filename1))
    image2 = client.upload(file=os.path.join(path, filename2))
    image3 = client.upload(file=os.path.join(path, filename3))
    image4 = client.upload(file=os.path.join(path, filename4))
   
    #delete local
    shutil.rmtree(path, ignore_errors=True)
    
    #save db
    newImg1 = Img(filename1, str(image1.url), int(lastAcc.id))
    newImg2 = Img(filename2, str(image2.url), int(lastAcc.id))
    newImg3 = Img(filename3, str(image3.url), int(lastAcc.id))
    newImg4 = Img(filename3, str(image4.url), int(lastAcc.id))
    db.session.add(newImg1)
    db.session.add(newImg2)
    db.session.add(newImg3)
    db.session.add(newImg4)

    db.session.commit()
    
    print("Lưu thành công")
    return redirect(url_for("admin.admin_home"))
    
def update_balance_for_user(id):
    user = User.query.get(id)
    data = request.json
    if user:
        if data and "balance" in data:
            try:
                user.balance = data["balance"]
                db.session.commit()
                return jsonify({"message": "User is updated!"}), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update user!"}), 400 
    else:
        return jsonify({"message": "Not found user"}), 404
    
def get_img(id):
    pass