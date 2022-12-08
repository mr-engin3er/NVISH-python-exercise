import os, json, redis

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PORT = os.getenv("REDIS_PORT",6379)


def connect_redis():
    try:
        global redis_client
        redis_client = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
        return redis_client
    except redis.ConnectionError as err:
        print(err)

def set_dict(key,value):
    return redis_client.set(key,json.dumps(value))

def get_dict(key):
    data = redis_client.get(key)
    return json.loads(data) if data else False

def delete_cache(key):
    return redis_client.delete(key)


def is_redis_connected():
    try:
        return redis_client.ping()
    except redis.ConnectionError as err:
        print(err)
        return False
