from model.client import Client
import sqlite3

class ClientControler:
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
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL
                    state TEXT NOT NULL)
                '''
                )
            conn.commit()
            
    # adicionar cliente        
    def add_client(self):
       pass
