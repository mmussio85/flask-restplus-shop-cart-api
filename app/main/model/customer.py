
from .. import db, flask_bcrypt
import datetime



class Customer(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "Customer"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), unique=False, nullable=False)
    
    
    def __repr__(self):
        return "<Customer '{}'>".format(self.name)
