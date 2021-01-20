import uuid
import datetime

from app.main import db
from app.main.model.cart import Cart
from app.main.model.item import Item
from app.main.util.mail import Mail

def get_item_by_cart(cart_id):
    cart = Cart.query.filter_by(ID=cart_id).first()
    return cart.items


def get_cart_amount(cart_id):
    tuple_items = map(lambda x: (int(x.price)), get_item_by_cart(cart_id))
    return sum(tuple_items)

def get_min_item_price(cart_id):
    return min(map(lambda x: (int(x.price)), get_item_by_cart(cart_id)))

def get_max_item_price(cart_id):
    return max(map(lambda x: (int(x.price)), get_item_by_cart(cart_id)))

def save_cart_item(data):
    item = Item.query.filter_by(ID=data['item_id']).first()
    if data.get('cart_id'):
        cart = Cart.query.filter_by(ID=data['cart_id']).first()
        if cart:
            #add the item in the cart
            cart.items.append(item)
            save_changes(cart)
        else:
            response_object = {
                'status': 'fail',
                'message': 'Invalid cart.',
            }
            return response_object, 409
    elif data.get("item_id"):
        new_cart = Cart(

            customerID = 1,
            status = "opened"
        )
        db.session.add(new_cart)
        db.session.flush()
        new_cart.items.append(item)
        save_changes(new_cart)
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'Item is not present.',
        }
        return response_object, 409

def update_cart_status(cart_id, status, data):
    cart = Cart.query.filter_by(ID=cart_id).first()
    if cart and cart.status == "opened":
        cart.status = status
        db.session.commit()
        amount = get_cart_amount(cart_id)
        if data["type"] == "credit_card":
            amount = amount * 0.90
        elif data["type"] == "paypal":
            amount = amount - get_min_item_price(cart_id)
        elif data["type"] == "cash":
            amount = amount - (get_max_item_price(cart_id) * 0.90)
        mail = Mail()
        mail.send_email( "Checkedout cart {0} amount {1}".format(cart_id, amount))
        return "{0} cart {1} ! amount {2}".format(status, cart_id, amount), 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'cart id does not exist or It is not open.',
        }
        return response_object, 409    



def save_changes(data):
    db.session.add(data)
    db.session.commit()

#def update_changes(data):
#    db.session.update(data)
#    db.session.commit()    

