from functools import wraps

from flask_jwt_extended import get_jwt, verify_jwt_in_request

from exceptions import PermissionDenied


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            roles = claims["roles"]
            if role in roles:
                return fn(*args, **kwargs)
            else:
                raise PermissionDenied(message="Permission Denied")

        return decorator
    return wrapper


def permission_required(permission):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            permissions = claims["permissions"]
            if permission in permissions:
                return fn(*args, **kwargs)
            else:
                raise PermissionDenied(message="Permission Denied")

        return decorator
    return wrapper
