from sqlite3 import Connection
from src.utils import get_db_connection, dict_factory, create_jwt , verify_jwt



def test_get_db_connection():
    conn = get_db_connection()
    assert isinstance(conn,Connection),f'''
    Expecting {True} and got {isinstance(conn,Connection)}'''

def test_dict_factory(mocker):
    cursor = mocker.MagicMock()
    cursor.description = (["id"],["username"],["password"])
    row = ("1","admin","some-password")
    result = dict_factory(cursor,row)
    assert isinstance(result,dict),f'''
    Expecting {True} and got {isinstance(result,dict)}'''


def test_create_jwt(mocker):
    mock = mocker.patch("src.utils.jwt.encode")
    payload = {
        "id":"1",
        "username": "name"
    }
    create_jwt(payload)
    assert mock.is_called(),f'''
    Expecting {True} and got {mock.is_called()}'''

def test_verify_jwt(mocker):
    mock = mocker.patch("src.utils.jwt.decode")
    token = "ejnfnkllkf.dljlkkljds.djllkdjkld"
    verify_jwt(token)
    assert mock.is_called(),f'''
    Expecting {True} and got {mock.is_called()}'''
