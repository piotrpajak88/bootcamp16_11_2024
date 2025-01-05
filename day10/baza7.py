import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("../day10/sqlite_python.db")
    sql_connection.row_factory = sqlite3.Row  # zwraca dane ktore mozemy przeksztalcic w slownik
    cursor = sql_connection.cursor()
    print("Connected to SQLite")

    # table_data = 'software'
    table_data = 'hardware'

    select = f"SELECT * FROM {table_data};"

    cursor.execute(select)
    rows = cursor.fetchall()

    for row in rows:
        print(dict(row))


except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("SQLite connection is closed")
