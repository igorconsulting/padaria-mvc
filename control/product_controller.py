from model.product import Product
import sqlite3

class ProductController:
    def __init__(self, db_path='data/bakery.db'):
        self.db_path = db_path
        self.__create_table()

    def __create_table(self):
        """
        Creates the products table if it doesn't already exists.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    taste TEXT NOT NULL,
                    price REAL NOT NULL)
                '''
                )
            conn.commit()
                    
    def add_product(self,product: Product) -> None:
        """
        Adds a new product to the database
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(('''
                INSERT INTO products (name, taste, price)
                VALUES (?,?,?)
            '''
            ), (product.name, product.taste, product.price))
            conn.commit()
    
    def get_all_products(self):
        """
        Retrieves all products from the database
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            rows = cursor.fetchall()

        products = [Product(row[1],row[2],row[3]) for row in rows]

        return products
    
    def get_products_by_taste(self, taste:str):
        """
        Retrieves products by state.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM products WHERE taste = ?',(taste,)
            )
            rows = cursor.fetchall()

        products = [Product(row[1],row[2],row[3]) for row in rows]
        return products 