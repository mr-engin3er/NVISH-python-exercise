import sqlite3
from werkzeug.security import generate_password_hash
from src.config import DB_URI
connection = sqlite3.connect(DB_URI)

cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS user;');

cur.execute('''CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);''')

cur.execute('DROP TABLE IF EXISTS posts;');

cur.execute('''CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);''')

data = ('admin', generate_password_hash('Admin@123'))

cur.execute("INSERT INTO user (username, password) VALUES (?, ?)",
            data
            )

connection.commit()
connection.close()