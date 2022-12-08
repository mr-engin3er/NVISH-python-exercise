import jwt,sqlite3
from .config import configuration, DB_URI

SECRET_KEY = configuration.get("dev").get("SECRET_KEY")

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def get_db_connection():
    connection = sqlite3.connect(DB_URI)
    connection.row_factory = dict_factory
    return connection

def create_jwt(payload):
    return jwt.encode(payload,SECRET_KEY,"HS256")

def verify_jwt(token):
    return jwt.decode(token,SECRET_KEY,["HS256"])