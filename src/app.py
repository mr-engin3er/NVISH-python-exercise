from flask import Flask
from .config import configuration


def create_app():
    from .exercise1 import exercise1 
    from .exercise2 import exercise2

    app = Flask(__name__)
    app.config.from_mapping(configuration.get("dev"))

    app.register_blueprint(exercise1,url_prefix="/")
    app.register_blueprint(exercise2,url_prefix="/")

    return app

