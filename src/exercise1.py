from flask import Blueprint

exercise1 = Blueprint("exercise1", __name__)


@exercise1.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong"}, 200
