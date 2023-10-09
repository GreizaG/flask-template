from inspect import getdoc

from flask import current_app


def endpoints_list():
    """
    Retrieve a list of endpoints along with their HTTP methods and docstring descriptions.

    Returns:
        list: A list of dictionaries containing endpoint information.

    Example:
        [
            {
                "endpoint": "/admin",
                "methods": ['GET'],
                "doc": 'Flask Admin'
            },
            {
                "endpoint": "/example_endpoint",
                "methods": ['GET', 'POST'],
                "doc": 'This is an example endpoint with a docstring.'
            },
            # More endpoint entries...
        ]

    This function iterates through the Flask application's URL rules and extracts information about each endpoint,
    excluding static and admin routes. It includes the HTTP methods allowed for each endpoint and, if available,
    the docstring of the associated view function. If no docstring is found, it uses a default message.
    """
    rules = current_app.url_map.iter_rules()
    endpoints = [{
        "endpoint": "/admin",
        "methods": ['GET'],
        "doc": 'Flask Admin'
    }]
    for rule in rules:
        if not str(rule).startswith('/static') and not str(rule).startswith('/admin'):
            view_function = current_app.view_functions[rule.endpoint]
            docstring = getdoc(view_function) or "No documentation available"
            endpoints.append({
                "endpoint": str(rule),
                "methods": list(rule.methods - {'OPTIONS', 'HEAD'}),
                "doc": docstring
            })
    return endpoints
