import json
from src.redis_utils import connect_redis, is_redis_connected, set_dict, get_dict, delete_cache

def test_connect_redis(mocker):
    mock = mocker.patch("src.redis_utils.redis.Redis")
    connect_redis()
    assert mock.is_called(),f'''
    Expecting {True} and got {mock.is_called()}'''


def test_is_redis_connected(mocker):
    mocker.patch("src.redis_utils.redis_client.ping",return_value=True)
    result = is_redis_connected()
    assert result,f'''
    Expecting {True} and got {result}'''

def test_get_dict(mocker):
    data = json.dumps([{"some":"data"}])
    mocker.patch("src.redis_utils.redis_client.get",return_value=data)
    result = get_dict("key")
    assert result == json.loads(data), f'''
    Expecting {json.loads(data)} and got {result}'''


def test_set_dict(mocker):
    mocker.patch("src.redis_utils.redis_client.set",return_value=True)
    result = set_dict("key",{"data":"value"})
    assert result, f'''
    Expecting {True} and got {result}'''


def test_delete_cache(mocker):
    mocker.patch("src.redis_utils.redis_client.delete",return_value=True)
    result = delete_cache("key")
    assert result, f'''
    Expecting {True} and got {result}'''