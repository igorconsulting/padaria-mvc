import sqlite3
from model.product import Product

class ProductRepository:
    def __init__(self, db_path='data/bakery.db'):
        self.db_path = db_path
        self.__create_table()

    def __create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    taste TEXT NOT NULL,
                    price REAL NOT NULL)
            ''')
            conn.commit()

    def save(self, product: Product):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO products (name, taste, price) VALUES (?,?,?)',
                (product.name, product.taste, product.price)
            )
            conn.commit()

    def get_all(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            rows = cursor.fetchall()
        return [Product(row[1], row[2], row[3]) for row in rows]
    
    def get_by_name(self, name: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products WHERE name = ?', (name,))
            rows = cursor.fetchall()
        return [Product(row[1], row[2], row[3]) for row in rows]

    def get_by_taste(self, taste: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products WHERE taste = ?', (taste,))
            rows = cursor.fetchall()
        return [Product(row[1], row[2], row[3]) for row in rows]
