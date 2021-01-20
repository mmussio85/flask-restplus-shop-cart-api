from flask_restx import Api
from flask import Blueprint

from .main.controller.item_controller import api as item_ns
from .main.controller.cart_controller import api as cart_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.customer_controller import api as customer_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) SHOP CART API WITH COGNITO',
          version='1.0',
          description='flask restplus (restx) web service'
          )

api.add_namespace(auth_ns)
api.add_namespace(item_ns)
api.add_namespace(cart_ns)
api.add_namespace(customer_ns)