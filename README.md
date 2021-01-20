#### FLASK RESTX WITH COGNITO INTEGRATION

### Contributing
The structure of this project is based on this example, and adapted for managing a shop cart with Cognito user authentication:

```
https://github.com/cosmic-byte/flask-restplus-boilerplate.git
```


### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database. A local database "shop-cart-api" must be created, since DEV uses postgres locally.
    
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade

In addition, for the file /util/mail.py, please set a valid email and password.

### Cognito integration ###

    Since the app integrates with AWS Cognito, the user pool, the app id and the secret must be set in the following files: customer_service.py and manage.py                                                
    Once a user is created in the system, the token coming from cognito is retrived to be used for the next requests.
    A user group called *admin* must be created in cognito.                                                                                                                                         

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/



### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login_by_cognito"




