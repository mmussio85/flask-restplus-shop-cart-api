from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, print_decorator
from ..util.dto import CustomerDto
from ..service.customer_service import save_customer
from flask_cognito import cognito_auth_required, cognito_group_permissions, current_user, current_cognito_jwt

api = CustomerDto.api
_customer_add = CustomerDto.user


@api.route('/', methods = ['POST'])
class Customer(Resource):
    @api.doc('add_customer')
    @api.expect(_customer_add, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new item')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_customer(data=data)

    