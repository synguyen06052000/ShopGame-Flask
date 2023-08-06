from .extension import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(30))
    phonenumber = db.Column(db.String(30))
    balance = db.Column(db.Integer)
    role = db.Column(db.Integer)
    datejoin = db.Column(db.Date)
    
    def __init__(self, username, password, phonenumber, balance, role, datejoin):
        self.username = username
        self.password = password
        self.phonenumber = phonenumber
        self.balance = balance
        self.role = role
        self.datejoin = datejoin
        
class Acc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classAcc = db.Column(db.String(30))
    rank = db.Column(db.Integer)
    price = db.Column(db.Integer)
    server = db.Column(db.String(60))
    card = db.Column(db.String(30))
    weapon = db.Column(db.Integer)
    level = db.Column(db.Integer)
    hotDescription = db.Column(db.String(150))
    img_acc = db.relationship("Img")
    
    def __init__(self, classAcc, rank, price, server, card, weapon, level, hotDescription):
        self.classAcc = classAcc
        self.rank = rank
        self.price = price
        self.server = server
        self.card = card
        self.weapon = weapon
        self.level = level
        self.hotDescription = hotDescription    
    
class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    url_img = db.Column(db.String(256))
    acc_id = db.Column(db.Integer, db.ForeignKey("acc.id"))
    
    def __init__(self, name, url_img, acc_id):
        self.name = name
        self.url_img = url_img
        self.acc_id = acc_id
    
    