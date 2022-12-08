
def test_login(client):
    login_response = client.post("/login",json={
        "username":"admin",
        "password": "Admin@123"
    })
    assert login_response.status_code == 200, f"Expecting status {200} and got {login_response.status_code}"


def test_authorize(client,auth_token):
    auth_response = client.get("/authorize",headers={
        "Authorization" : f'Bearer {auth_token}'
    })
    assert auth_response.status_code == 200, f"Expecting status {200} and got {auth_response.status_code}"