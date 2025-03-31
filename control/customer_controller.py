from model.customer import Customer
import sqlite3

class CustomerController:
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
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    state TEXT NOT NULL)
                '''
                )
            conn.commit()
            
    # adicionar cliente        
    def add_client(self,customer) -> None:
        """
        Adds a new client to the database
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(('''
                INSERT INTO customers (name, phone, state)
                VALUES (?,?,?)
            '''
            ), (customer.name, customer.phone, customer.state))
            conn.commit()
    
    def get_all_customers(self):
        """
        Retrieves all customers from the database
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM customers')
            rows = cursor.fetchall()

        customers = [Customer(row[1],row[2],row[3]) for row in rows]

        return customers
    
    def get_clients_by_state(self, state:str):
        """
        Retrieves clients by state.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM customers WHERE state = ?',(state,)
            )
            rows = cursor.fetchall()

        customers = [Customer(row[1],row[2],row[3]) for row in rows]
        return customers 