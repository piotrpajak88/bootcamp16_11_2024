import sqlite3

data = [
    (4,"Rust",89),
    (6,"Angular",18),
    (8,"JS",12),
]
sql_connection = None
try:
    sql_connection = sqlite3.connect("../day10/sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Connected to SQLite")

    insert = """
    INSERT INTO software(id,name,price) VALUES (?,?,?);
    """

    # cursor.execute(insert,(9,"Scala",560))
    # sql_connection.commit()

    # Wstawienie wielokrotnych rekordów
    cursor.executemany(insert, data)
    sql_connection.commit()

    
except sqlite3.Error as e:
    print("Bład bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("SQLite connection is closed")