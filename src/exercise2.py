from flask import Blueprint,request
from werkzeug.security import check_password_hash
from .utils import create_jwt,verify_jwt, get_db_connection

exercise2 = Blueprint("exercise2",__name__)


@exercise2.route("/login",methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return {"error":"username and password are required."},400

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute(f"SELECT * from user where username = '{username}';")
    user = cur.fetchone()
    connection.close()
    if user and check_password_hash(user.get("password"), password):
            return {"message":"You've logged in successfully","token":create_jwt(user)},200

    return {"error":"Invalid credentials."},401


@exercise2.route("/authorize",methods=["GET"])
def authorize():
    authorization = request.headers.get("Authorization")
    if not authorization:
        return {"error":"Authrozatin credentials not provided."},401

    _, token = authorization.split(" ")
    is_authorized = verify_jwt(token)

    if is_authorized:
        is_authorized.pop("password")
        return {"message":"token is valid","user":is_authorized},200

    return {"error":"Invalid credentials."},401

