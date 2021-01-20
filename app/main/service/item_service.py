import uuid
import datetime

from app.main import db
from app.main.model.item import Item
from app.main.util.mail import Mail
 
def get_item_by_id(item_id):
    return Item.query.filter_by(ID=item_id).first()

def delete_item_by_id(cart_id):
    try:
        delete_elem(Item.query.filter_by(ID=cart_id).first())
    except Exception as e:
        raise Exception("Item {0} is part of an excisting cart.".format(item_id))    

def get_all_items():
    return Item.query.all()

def save_new_item(data):
    new_item = Item(
        name=data['name'],
        supplier=data['supplier'],
        price=data['price'],
        category=data['category']
            
    )
    save_changes(new_item)
    mail = Mail()
    mail.send_email( "Added Name {0} Supplier {1} Price {2}".format(new_item.name, new_item.supplier, new_item.price))
    return "Added Item", 200
    
def update_new_item(data):
    item = Item.query.filter_by(ID=data['ID']).first()
    if item:
        item.name = data['name']
        item.supplier = data['supplier']
        if data['price'] != item.price:
            mail = Mail()
            mail.send_email( "Price changed Price {0}".format(data['price']))
        item.price = data['price']
        db.session.commit()
        
        return "Updated Item", 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Item is not present.',
        }
        return response_object, 409
    
def delete_elem(data):
    db.session.delete(data)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

