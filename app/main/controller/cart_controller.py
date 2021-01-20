from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import CartDto, ItemDto
from ..service.cart_service import save_cart_item, get_item_by_cart, update_cart_status
from flask_cognito import cognito_auth_required, cognito_group_permissions, current_user, current_cognito_jwt

api = CartDto.api
_cart = CartDto.cart_new_item
_item_add = ItemDto.item_add

@api.route('/', methods = ['GET', 'POST', 'PUT'])
class Cart(Resource):

    @api.expect(_cart, validate=True)
    @api.response(201, 'Item successfully added.')
    @api.doc('add new item in the cart')
    def post(self):
        """Adds a new Item in the Cart """
        data = request.json
        return save_cart_item(data=data)

    @api.expect(_cart, validate=True)
    @api.response(201, 'Item successfully updated.')
    @api.doc('add new item in the cart')
    def put(self):
        """Adds a new Item in the Cart """
        data = request.json
        return save_cart_item(data=data)

@api.route('/<cart_id>')
@api.param('cart_id', 'Cart identifier')
@api.response(404, 'Cart not found.')
class CartList(Resource):
    @api.doc('get the list of items in the cart')
    @api.marshal_with(_item_add)
    def get(self, cart_id):
        """get a user given its identifier"""
        items = get_item_by_cart(cart_id)
        if not items:
            print("abort!!!")
            api.abort(404)
        else:
            return items

@api.route('/<cart_id>/checkout')
class CartCheckout(Resource):

    @api.response(201, 'Cart successfully checked out.')
    @api.doc('Checkout cart')
    #@cognito_auth_required
    def post(self, cart_id):
        """Adds a new Item in the Cart """
        data = request.json
        print(data)
        return update_cart_status(cart_id, "checkedout", data)


@api.route('/<cart_id>/cancel')
class CartCheckout(Resource):

    @api.response(201, 'Cart successfully cancelled.')
    @api.doc('Cancel cart')
    def post(self, cart_id):
        """Adds a new Item in the Cart """
        return update_cart_status(cart_id, "cancelled")
