import sqlite3

lista = []
sql_connection = None
try:
    sql_connection = sqlite3.connect("../day10/sqlite_python.db")
    sql_connection.row_factory = sqlite3.Row # ustawienie aby baza zawracala jako slownik
    cursor = sql_connection.cursor()
    print("Connected to SQLite")

    select = """
        SELECT * FROM software
        """
    for row in cursor.execute(select):
        print(row)
        lista.append(dict(row))
    print(lista)

    # [{'id': 1, 'name': 'Python', 'price': 100.0}, {'id': 2, 'name': 'Java', 'price': 50.0},
    #  {'id': 3, 'name': 'SQL', 'price': 199.0}, {'id': 5, 'name': 'SQL', 'price': 199.0},
    #  {'id': 7, 'name': 'T-SQL', 'price': 999.0}]

    #inne podejscie do select
    cursor.execute(select)

    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))

    # {'id': 1, 'name': 'Python', 'price': 100.0}
    # {'id': 2, 'name': 'Java', 'price': 50.0}
    # {'id': 3, 'name': 'SQL', 'price': 199.0}
    # {'id': 5, 'name': 'SQL', 'price': 199.0}
    # {'id': 7, 'name': 'T-SQL', 'price': 999.0}

except sqlite3.Error as e:
    print("Bład bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("SQLite connection is closed")
