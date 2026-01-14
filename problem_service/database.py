import sqlite3

DATABASE = 'problem_service.db'

def get_db():    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_conn():
    conn = get_db()
    cursor = conn.cursor()
    return conn, cursor

