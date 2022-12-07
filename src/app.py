from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import configuration

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(configuration.get("dev"))
    db.init_app(app)

    return app

