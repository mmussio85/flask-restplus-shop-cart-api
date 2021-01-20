
from .. import db, flask_bcrypt
import datetime



class Item(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "Item"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    supplier = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String(20), unique=False, nullable=False)
    
    def __init__(self, name, supplier, price, category):
        self.name = name
        self.supplier = supplier
        self.price = price
        self.category = category

    #def __repr__(self):
    #    name = self.name
    #    price = self.price

    #    return "<Item '{}'>".format(self.name)
