import os
from src.app import create_app
from src.redis_utils import connect_redis


HOST = os.getenv("HOST", "localhost")
ENV = os.getenv("ENV", "dev")
PORT = os.getenv("PORT", 8000)

connect_redis()
app = create_app(ENV)


if __name__ == "__main__":
    app.run(HOST, PORT)
