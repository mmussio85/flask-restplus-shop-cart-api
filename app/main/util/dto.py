from flask_restx import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    user = api.model('customer', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=False, description='user password'),
        
    })

class ItemDto:
    # TODO unify both item dto
    api = Namespace('item', description='item related operations')
    item_add = api.model('item', {
        #'ID': fields.Integer(required=True, description='item id'),
        'name': fields.String(required=True, description='item name'),
        'supplier': fields.String(required=True, description='item supplier'),
        'category': fields.String(required=True, description='item category'),
        'price': fields.Integer(description='item price')
    })
    item_update = api.model('item', {
        'ID': fields.Integer(required=True, description='item id'),
        'name': fields.String(required=True, description='item name'),
        'supplier': fields.String(required=True, description='item supplier'),
        'category': fields.String(required=True, description='item category'),
        'price': fields.Integer(description='item price')
    })

class CartDto:
    api = Namespace('cart', description='cart related operations')
    cart_new_item = api.model('cart', {
        'cart_id': fields.Integer(required=False, description='cart id'),
        'item_id': fields.Integer(required=True, description='item id'),
    })
    
class PaymentDto:
    api = Namespace('payment', description='cart related operations')
    payment = api.model('payment', {
        'type': fields.Integer(required=True, description='payment ype'),
        'name': fields.Integer(required=False, description='person name'),
        'credit_card': fields.Integer(required=False, description='credit card'),
        'mail': fields.Integer(required=False, description='user mail'),
        'password': fields.Integer(required=False, description='user password'),
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The user account'),
        'password': fields.String(required=True, description='The user password '),
    })
