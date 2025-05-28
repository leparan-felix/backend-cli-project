from database.db import get_connection
from models.product import Product

def add_product(name, quantity, price):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
        conn.commit()

def list_products():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        return [Product(*row) for row in rows]

def update_product(id, quantity=None, price=None):
    with get_connection() as conn:
        cursor = conn.cursor()
        if quantity is not None:
            cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, id))
        if price is not None:
            cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))
        conn.commit()

def delete_product(id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        conn.commit()
