def test_save_post(client,mocker):
    mocker.patch("src.exercise3.is_redis_connected", return_value=False)
    response = client.post("/save",json={
        "title" : "My first post",
        "content" : "some big content"
    })
    assert response.status_code == 201 , f'''
    Expecting testing in config to be {201} but got {response.status_code}'''

def test_get_one_post(client,mocker):
    mocker.patch("src.exercise3.is_redis_connected", return_value=False)
    response = client.get("/get/1")
    assert response.status_code == 200 , f'''
    Expecting testing in config to be {200} but got {response.status_code}'''
    assert isinstance(response.json.get("data"), dict) , f'''
    Expecting testing in config to be {True} but got {isinstance(response.json.get("data"), list)}'''
 
    
    
def test_get_all_post(client,mocker):
    mocker.patch("src.exercise3.is_redis_connected", return_value=False)
    response = client.get("/get")
    assert response.status_code == 200 , f'''
    Expecting testing in config to be {200} but got {response.status_code}'''
    assert isinstance(response.json.get("data"), list) , f'''
    Expecting testing in config to be {True} but got {isinstance(response.json.get("data"), list)}'''

def test_delete_one_post(client,mocker):
    mocker.patch("src.exercise3.is_redis_connected", return_value=False)
    response = client.delete("/delete/1")
    assert response.status_code == 200 , f'''
    Expecting testing in config to be {200} but got {response.status_code}'''

def test_delete_all_post(client,mocker):
    mocker.patch("src.exercise3.is_redis_connected", return_value=False)
    response = client.delete("/delete")
    assert response.status_code == 200 , f'''
    Expecting testing in config to be {200} but got {response.status_code}'''