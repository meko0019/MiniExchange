import os

import flask

from app.database import db



def create_app(settings=None):
    """Application factory with optional overridable settings.
    """
    if settings is None:  # pragma: no coverage
        settings = {}

    app = flask.Flask(__name__)

    # If we're in debug mode we're using the development test_config
    # otherwise we'll default to the production test_config.
    if settings.get("DEBUG", False) or os.environ.get("DEBUG", False):
        app.config.from_object("config.DevelopmentConfig")
    else:  # pragma: no coverage
        app.config.from_object("config.ProductionConfig")

    # We'll override the defaults in test_config.py if given here.
    app.config.from_mapping(settings)

    # Initialize the database with the application.
    db.init_app(app)


    from app.api.views import api_blueprint
   
    app.register_blueprint(api_blueprint)




    return app
