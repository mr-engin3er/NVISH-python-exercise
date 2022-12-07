import os
from src.app import create_app


HOST = os.getenv("HOST","localhost")
PORT = os.getenv("PORT",8000)

if __name__ == "__main__":
    create_app().run(HOST,PORT)
