from functools import wraps


def make_html(element):
    def html_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            text = f"<{element}>"
            text += function(*args, **kwargs)
            text += f"</{element}>"
            return text
        return wrapper
    return html_decorator
