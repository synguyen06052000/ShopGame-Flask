from .extension import db

class User(db.Model):
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
    