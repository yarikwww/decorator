from functools import wraps

def requires_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_type = kwargs.get('user_type')
            if user_type != required_role:
                raise ValueError("Permission denied")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires_role('admin')
def show_customer_receipt(*args, **kwargs):

    return "Receipt shown"


try:
    print(show_customer_receipt(user_type='user'))
except ValueError as e:
    print(e)

try:
    print(show_customer_receipt(user_type='admin'))
except ValueError as e:
    print(e)
