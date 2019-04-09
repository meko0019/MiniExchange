from flask import Blueprint

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route('/', methods=["GET"])
def index():
    return "Hello World"