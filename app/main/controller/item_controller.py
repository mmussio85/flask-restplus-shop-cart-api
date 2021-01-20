from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, print_decorator
from ..util.dto import ItemDto
from ..service.item_service import get_all_items, save_new_item, update_new_item, get_item_by_id, delete_item_by_id
from flask_cognito import cognito_auth_required, cognito_group_permissions, current_user, current_cognito_jwt

api = ItemDto.api
_item_add = ItemDto.item_add
_item_update = ItemDto.item_update

@api.route('/', methods = ['GET', 'POST', 'PUT'])
class ItemList(Resource):
    @api.doc('list_of_items')
    @print_decorator
    @api.marshal_list_with(_item_add, envelope='data')
    def get(self):
        return get_all_items()

    @api.expect(_item_add, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new item')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_item(data=data)

    @api.expect(_item_update, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new item')
    @cognito_auth_required
    @cognito_group_permissions(['admin'])
    def put(self):
        data = request.json
        return update_new_item(data=data)

@api.route('/<item_id>')
@api.param('item_id', 'Item identifier')
@api.response(404, 'Item not found.')
class Item(Resource):
    @api.doc('get an item')
    @api.marshal_with(_item_add)
    def get(self, item_id):
        """get a user given its identifier"""
        item = get_item_by_id(item_id)
        if not item:
            api.abort(404)
        else:
            return item

    @api.doc('delete an item')
    @cognito_auth_required
    @cognito_group_permissions(['admin'])
    def delete(self, item_id):
        """delete an item given its identifier"""
        try:
            return delete_item_by_id(item_id)    
        except Exception as e:
            return "Item {0} is part of an existing cart.".format(item_id), 500
        
        