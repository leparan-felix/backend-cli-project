import sqlite3

def get_connection():
    return sqlite3.connect("inventory.db")

def initialize_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                       
                quantity INTEGER NOT NULL CHECK(quantity >= 0),
                       
                price REAL NOT NULL CHECK(price >= 0)
                      
            )
        ''')
        conn.commit()
