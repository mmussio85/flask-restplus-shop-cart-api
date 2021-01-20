#from app.main.model.user import User
from app.main.model.customer import Customer

from ..service.customer_service import generate_token

class Auth:

    @staticmethod
    def login_user(data):
        message = ""
        try:
            customer = Customer.query.filter_by(user_name=data.get('username')).first()
            if customer:
                auth_token = generate_token(data)
                print(auth_token)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Token': auth_token
                    }
                    return response_object, 200
            else:
                raise Exception("invalid username.")    
        except botocore.errorfactory.NotAuthorizedException as e:
            raise e    

        except Exception as e:
            raise e

    