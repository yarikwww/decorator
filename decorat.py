from functools import wraps

def catch_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка: {e}")
    return wrapper

@catch_exceptions
def risky_function(x, y):
    return x / y

risky_function(10, 0)