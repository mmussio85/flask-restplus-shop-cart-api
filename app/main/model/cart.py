
from .. import db, flask_bcrypt
import datetime
from app.main.model.customer import Customer

cart_item = db.Table('Cart_Item', db.Model.metadata,
    db.Column('cart_ID', db.Integer, db.ForeignKey('Cart.ID')),
    db.Column('item_ID', db.Integer, db.ForeignKey('Item.ID'))
)

class Cart(db.Model):
    __tablename__ = "Cart"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(20), unique=False, nullable=False)
    customer = db.relationship("Customer")
    customerID = db.Column(db.Integer, db.ForeignKey('Customer.ID'))
    payment = db.Column(db.String(20), unique=False, nullable=False)
    items = db.relationship("Item",
                               secondary=cart_item)
    def __repr__(self):
        return "<Cart '{}'>".format(self.status)

