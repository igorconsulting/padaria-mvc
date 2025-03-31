from model.customer import Customer
import sqlite3

class ProductController:
    def __init__(self, db_path='data/bakery.db'):
        self.db_path = db_path
        self.__create_table()

    def __create_table(self):
        """
        Creates the clients table if it doesn't already exists.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    taste TEXT NOT NULL,
                    price DOUBLE NOT NULL)
                '''
                )
            conn.commit()
            
    # adicionar cliente        
    def add_product(self,product) -> None:
        """
        Adds a new client to the database
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(('''
                INSERT INTO product (name, taste, price)
                VALUES (?,?,?)
            '''
            ), (product.name, product.phone, product.state))
            conn.commit()
    
    def get_all_products(self):
        """
        Retrieves all customers from the database
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            rows = cursor.fetchall()

        customers = [Customer(row[1],row[2],row[3]) for row in rows]

        return customers
    
    def get_products_by_taste(self, taste:str):
        """
        Retrieves clients by state.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM customers WHERE taste = ?',(taste,)
            )
            rows = cursor.fetchall()

        customers = [Customer(row[1],row[2],row[3]) for row in rows]
        return customers 