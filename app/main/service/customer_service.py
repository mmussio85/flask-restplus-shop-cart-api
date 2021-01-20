import uuid
import datetime

from app.main import db
from app.main.model.customer import Customer

import boto3
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
import uuid


user_pool_id = u"XXXXXXXXXXXX"
client_id = u"XXXXXXXXXXXXX"
client_secret = u'XXXXXXXXXXXXX'

cognito = boto3.client('cognito-idp', region_name="us-east-1")

def get_secret_hash(username):
            msg = username + client_id
            dig = hmac.new(str(client_secret).encode('utf-8'), 
                msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
            d2 = base64.b64encode(dig).decode()
            return d2

def save_customer(data):
    try:
        username = data.get('username')
        password = data.get('password')
        resp = cognito.admin_create_user(
                    UserPoolId=user_pool_id,
                    Username=username,
                    TemporaryPassword='test1234',
                    )

        cognito.admin_add_user_to_group(
            UserPoolId=user_pool_id, Username=username, GroupName="client"
        )

        resp = cognito.admin_set_user_password(
            UserPoolId=user_pool_id,
            Username=username,
            Password=password,
            Permanent=True
        )
        new_item = Customer(
            user_name=data['username']
        )
        save_changes(new_item)
        resp = cognito.admin_initiate_auth(
                    UserPoolId=user_pool_id,
                    ClientId=client_id,
                    AuthFlow='ADMIN_NO_SRP_AUTH',
                    AuthParameters={
                        'USERNAME': username,
                        'SECRET_HASH': get_secret_hash(username),
                        'PASSWORD': password
                    },
                    ClientMetadata={
                        'username': username,
                        'password': password
                    })

        return resp["AuthenticationResult"]['AccessToken'], 200
        

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        raise e

def generate_token(data):
    try:
        

        username = data.get('username')
        password = data.get('password')
        resp = cognito.admin_initiate_auth(
                    UserPoolId=user_pool_id,
                    ClientId=client_id,
                    AuthFlow='ADMIN_NO_SRP_AUTH',
                    AuthParameters={
                        'USERNAME': username,
                        'SECRET_HASH': get_secret_hash(username),
                        'PASSWORD': password
                    },
                    ClientMetadata={
                        'username': username,
                        'password': password
                    })

        return resp["AuthenticationResult"]['AccessToken']
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        raise e


def save_changes(data):
    db.session.add(data)
    db.session.commit()

