import pytest, os
from src.app import create_app
from src.config import DB_URI
import init_db

@pytest.fixture(scope="session")
def app():
    app = create_app("test")
    # create db
    init_db.setup()
    yield app
    os.remove(DB_URI)


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope="session")
def auth_token(client):
    login_response = client.post("/login",json={
        "username":"admin",
        "password": "Admin@123"
    })
    return login_response.json.get("token")