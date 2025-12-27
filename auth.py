import hashlib
from db import get_connection

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute(
        "SELECT role FROM users WHERE username=%s AND password=%s",
        (username, hashed_password)
    )

    result = cursor.fetchone()
    conn.close()
    return result
