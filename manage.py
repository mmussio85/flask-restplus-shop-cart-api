import os
#import unittest
import pytest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#from app import blueprint
from app.main import create_app, db
from app.main.model.customer import Customer

from flask_cognito import CognitoAuth

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
#app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

# configuration
app.config.update({
    	'COGNITO_REGION': 'us-east-1',
    	'COGNITO_USERPOOL_ID': 'XXXXXXXX',
    	'COGNITO_APP_CLIENT_ID': 'XXXXXXXXX',
    	'COGNITO_JWT_HEADER_NAME': 'X-MyAxpp-Authorization',
    	'COGNITO_JWT_HEADER_PREFIX': 'Bearer',
	})
    


# initialize extension

cogauth = CognitoAuth(app)

@cogauth.identity_handler
def lookup_cognito_user(payload):
    """Look up user in our database from Cognito JWT payload."""
    return Customer.query.filter(Customer.user_name == payload['username']).one_or_none()

@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    #tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    #result = unittest.TextTestRunner(verbosity=2).run(tests)
    #if result.wasSuccessful():
    #    return 0
    #return 1
    pytest.main(["-s", "app/test"])

if __name__ == '__main__':
    manager.run()
