import os
from src.app import create_app

HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", 8000)

app = create_app()


if __name__ == "__main__":
    app.run(HOST, PORT)
