import json

from flask import abort, jsonify, request, url_for

from app import cache
from app.api.views import api_blueprint
from app.database import db
from app.users.models import User



@api_blueprint.route("/users", methods=["GET"])
@cache.cached(timeout=120, query_string=True)
def list_users():
    """
    List users.
    This endpoint supports pagination.
    """
    #TODO: paginated response
    return [jsonify(**user.__json__()) for user in User.query.all()]


@api_blueprint.route("/users/<string:username>", methods=["GET"])
def get_user(username):
    """
    Get a single user.
    """
    user = User.query.filter(User.username == username).first()
    if user is None:
        return abort(404)
    return jsonify(**user.__json__())


@api_blueprint.route("/users/", methods=["POST"])
def create_user():
    """
    Create a user.
    """
    pass


@api_blueprint.route("/users/<string:username>", methods=["PUT"])
def modify_user(username):
    """
    Update a user.
    """
    pass

