from functools import wraps

from flask_login import current_user


def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if current_user.role == role:
                return view_func(*args, **kwargs)
            else:
                return "You are not authorized to view this page"

        return wrapper

    return decorator
