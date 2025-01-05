# context manager - narzedzie usprawniajace prace np.: z plikami
# with
# __enter__
# __exit__

import sqlite3
from pprint import pprint


class SQLiteDBContextManager:
    def __init__(self, db_name):
        """
        Metoda inicjalizujaca, kontruktor
        """
        self.db_name = db_name
        self.conn = None

    def __enter__(self): # wykonuje sie przed zadaniem
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb): # wykonuje sie zawsze
        if self.conn:
            self.conn.commit()
            self.conn.close()

db_name = "my_data.db"
lista = []
with SQLiteDBContextManager(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO users(name) VALUES(?);", ("John",))
    cursor.execute("INSERT INTO users(name) VALUES(?);", ("Alice",))
    cursor.execute("INSERT INTO users(name) VALUES(?);", ("Tom",))
    cursor.execute("INSERT INTO users(name) VALUES(?);", ("Radek",))
    select = cursor.execute("SELECT * FROM users;")
    for _ in select:
        print(_)
        lista.append(_)
pprint(lista)