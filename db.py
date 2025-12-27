import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Farooqma12@",
        database="client_query_db"
    )
