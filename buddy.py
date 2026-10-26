@'
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query).fetchall()

PASSWORD = "admin123"
'@ | Set-Content buggy.py
SECRET_KEY = 'abc123'

SECRET_KEY = 'abc123'
