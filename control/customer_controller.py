from model.customer import Customer
import sqlite3

class CustomerControllerLegacy:
    def __init__(self, db_path='data/bakery.db'):
        self.db_path = db_path
        self.__create_table()

    def __create_table(self):
        """
        Creates the customer table if it doesn't already exists.
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
                    
    def add_customer(self,customer) -> None:
        """
        Adds a new customer to the database
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
    
    def get_customers_by_state(self, state:str):
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

    def get_customers_by_name(self, name:str):
        """
        Retrieves clients by name.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM customers WHERE name = ?',(name,)
            )
            rows = cursor.fetchall()

        customers = [Customer(row[1],row[2],row[3]) for row in rows]
        return customers
    

from model.customer import Customer
from repository.customer_repository import CustomerRepository
from view.customer import CustomerView

class CustomerController:
    def __init__(self):
        self.view = CustomerView()
        self.repo = CustomerRepository()

    def register_customer(self):
        name, phone, state = self.view.input_customer_data()
        try:
            customer = Customer(name, phone, state)
            self.repo.save(customer)
            self.view.show_message("Customer registered successfully!")
        except ValueError as e:
            self.view.show_message(f"Error: {e}")

    def list_all_customers(self):
        customers = self.repo.get_all()
        self.view.show_customers(customers)

    def search_by_name(self):
        name = input("Enter customer name to search: ")
        customers = self.repo.get_by_name(name.lower())
        self.view.show_customers(customers)

    def search_by_state(self):
        state = input("Enter customer state to search: ")
        customers = self.repo.get_by_state(state.lower())
        self.view.show_customers(customers)
