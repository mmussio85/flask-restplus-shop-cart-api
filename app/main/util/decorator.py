from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from itertools import groupby


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated

def print_decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        result = {}

        output = f(*args, **kwargs)
        result["total"] = len(output["data"])
        result["categories"] = { k: len(list(v))   for k,v in groupby(sorted(output["data"], key=lambda x: x["category"]), lambda x: x["category"])}
        result["data"] = output["data"]


        

        return result

    return decorated