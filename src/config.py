import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
DB_URI = f"{BASE_DIR}/NVISH_exercise_dev.db"

load_dotenv(f"{BASE_DIR}/.env")

base_config = {
    "FLASK_ENV":os.getenv("FLASK_ENV","development"),
    "SECRET_KEY" : os.getenv("SECRET_KEY","development-key"),
    "DEBUG" : os.getenv("DEBUG",False)
}

development_config = {
    **base_config,
    # add other required configs below
    # "SQLALCHEMY_DATABASE_URI" : f"sqlite:///{BASE_DIR}/NVISH_exercise_dev.db",
    # "SQLALCHEMY_TRACK_MODIFICATIONS" : False,
}

production_config = {
    **base_config,
    # "SQLALCHEMY_DATABASE_URI" : f"sqlite:///{BASE_DIR}/NVISH_exercise_prod.db",
    # "SQLALCHEMY_TRACK_MODIFICATIONS" : False,
    # add other prod configs below
}

testing_config = {
    **base_config,
    "TESTING" : True,
    # add other test configs below
    # "SQLALCHEMY_DATABASE_URI" : f"sqlite:///{BASE_DIR}/NVISH_exercise_test.db",
    # "SQLALCHEMY_TRACK_MODIFICATIONS" : False,
}

configuration = {
    "dev": development_config,
    "prod": production_config,
    "test": testing_config
}