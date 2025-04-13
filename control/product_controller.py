from model.product import Product
import sqlite3
from view.product import ProductView

class ProductControllerLegacy:
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
    
from model.product import Product
from view.product import ProductView
from repository.product_repository import ProductRepository

class ProductController:
    def __init__(self):
        self.view = ProductView()
        self.repo = ProductRepository()

    def register_product(self):
        name, taste, price = self.view.input_product_data()
        try:
            product = Product(name, taste, price)
            self.repo.save(product)
            self.view.show_message("Product registered successfully!")
        except ValueError as e:
            self.view.show_message(f"Error: {e}")

    def list_all_products(self):
        products = self.repo.get_all()
        self.view.show_products(products)

    def search_by_name(self):
        name = input("Enter customer name to search: ")
        products = self.repo.get_by_name(name.lower())
        self.view.show_products(products)


    def search_by_taste(self):
        taste = input("Enter product taste to search: ").lower()
        products = self.repo.get_by_taste(taste)
        self.view.show_products(products)
