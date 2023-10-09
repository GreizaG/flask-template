from flask import jsonify, Blueprint, render_template

from app_project.utils.endpoint_utils import endpoints_list

root_bp_api_v1 = Blueprint('root_bp_api_v1', __name__, url_prefix='/api/v1/')
root_bp = Blueprint('root_bp', __name__)


@root_bp_api_v1.route('/')
def root():
    """
    Serve a JSON response with a greeting message under the 'root_bp_api_v1' blueprint.

    The 'root_bp_api_v1' blueprint is registered with the url_prefix '/api/v1/', so this function handles
    requests to the root of this blueprint, i.e., requests to '/api/v1/'.

    This endpoint returns a JSON object containing a greeting message, "Hello World!".
    It is a simple endpoint returning a static JSON response with a 200 HTTP status code.

    :return: A JSON object with a greeting message and a 200 HTTP status code.
    """
    return jsonify({
        "message": "Hello World!"
    }), 200


# Any other endpoint will be served as a general message for an invalid endpoint
@root_bp_api_v1.route('/<path:path>', methods=['GET'])
def invalid_endpoint(path):
    """
    Handle requests to invalid or nonexistent endpoints under the 'root_bp_api_v1' blueprint.

    The 'root_bp_api_v1' blueprint is registered with the url_prefix '/api/v1/', so this function handles
    requests to invalid or nonexistent endpoints that are prefixed with '/api/v1/'.

    This endpoint returns a JSON object containing a message indicating that the endpoint or method is invalid.
    It also optionally includes the path that was attempted to be accessed.
    This method only accepts GET requests and returns an HTTP status code 404, indicating that the resource was
    not found.

    :param path: The path that was attempted to be accessed.
    :type path: str
    :return: A JSON object with an error message and the path, along with an HTTP status code 404.
    """
    response = {
        "message": "Invalid endpoint or method",
        "path": path  # Optionally include the path that was attempted to be accessed
    }

    # 404 is the HTTP status code for "Not Found"
    return jsonify(response), 404


@root_bp.route('/')
def root():
    """
    Serve a JSON response with a greeting message.

    This endpoint returns a JSON object containing a greeting message, "Hello World!".
    It is a simple endpoint returning a static JSON response with a 200 HTTP status code.

    :return: A JSON object with a greeting message and a 200 HTTP status code.
    """
    return jsonify({
        "message": "Hello World!"
    }), 200


@root_bp.route('/routes', methods=['GET'])
def routes_info():
    """
    This route handler function is part of the 'root_bp' blueprint and is mapped to the '/routes' endpoint.
    It is accessible via HTTP GET requests and is responsible for retrieving and displaying information about
    all the available endpoints in the application, excluding static routes. It also filters out the 'OPTIONS'
    and 'HEAD' HTTP methods for each endpoint.

    The 'root_bp' blueprint should be registered with an appropriate url_prefix if needed.

    Returns:
        render_template: Renders an HTML template, 'routes.html', and passes the 'routes' variable to it,
                         containing a list of dictionaries. Each dictionary holds information about an endpoint,
                         including its URL pattern, the HTTP methods it supports, and the associated view function's
                         docstring.

    Usage:
        Accessible via a web browser or an HTTP client at the following URL:
        [protocol]://[host]:[port][url_prefix]/routes

    Example:
        If the 'root_bp' blueprint is registered with the url_prefix '/api' and the application is running locally
        on port 3001, you can access this route by navigating to:
        http://127.0.0.1:3001/api/routes

    """
    endpoints = endpoints_list()
    return render_template('routes.html', routes=endpoints)
