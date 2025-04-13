import sqlite3
from model.customer import Customer

class CustomerRepository:
    def __init__(self, db_path='data/bakery.db'):
        self.db_path = db_path
        self.__create_table()

    def __create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    state TEXT NOT NULL
                )
            ''')
            conn.commit()

    def save(self, customer: Customer):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO customers (name, phone, state) VALUES (?, ?, ?)',
                (customer.name, customer.phone, customer.state)
            )
            conn.commit()

    def get_all(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM customers')
            rows = cursor.fetchall()
        return [Customer(row[1], row[2], row[3]) for row in rows]

    def get_by_name(self, name: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM customers WHERE name = ?', (name,))
            rows = cursor.fetchall()
        return [Customer(row[1], row[2], row[3]) for row in rows]

    def get_by_state(self, state: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM customers WHERE state = ?', (state,))
            rows = cursor.fetchall()
        return [Customer(row[1], row[2], row[3]) for row in rows]
