
from market import db



class User(db.Model):
    id = db.Column(db.Integer(),primary_key= True)
    username = db.Column(db.String(30),unique = True, nullable = False)
    email_address = db.Column(db.String(50),nullable = False,unique=True)
    password_hash = db.Column(db.String(60),nullable = False)
    budget = db.Column(db.Integer(),nullable = False,default = 1000)
    items = db.relationship('Item',backref='owned_user', lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer(),primary_key= True)
    name = db.Column(db.String(50),nullable = False,unique=True)
    price = db.Column(db.Integer(),nullable = False)
    barcode = db.Column(db.Integer(),nullable = False,unique=True)
    description = db.Column(db.String(500),nullable = False,unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey(User.id))

    
    def __repr__(self):
        return f'Item {self.name}'