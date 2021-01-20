from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class CustomerLogin(Resource):
    """
        Customer Login Resource
    """
    @api.doc('customer login')
    #@api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        try:
            return Auth.login_user(data=post_data)
        except Exception as e:
            response_object = {
                        'status': 'fail',
                        'message': 'Invalid user or password.'
                        
                    }
            return response_object, 401    

@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
