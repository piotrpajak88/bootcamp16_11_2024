import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Connected to SQLite")

    query = '''
    CREATE TABLE IF NOT EXISTS SqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL
    );
    '''

    # cursor.execute(query)
    # sql_connection.commit()


    #wczytanie skryptu sql jako tekst do wykonania na bazie danych

    with open('tables.sql','r') as file:
        sql_script = file.read()


    #wykonanie skryptu na bazie danych
    cursor.executescript(sql_script)


except sqlite3.Error as e:
    print("Bład bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("SQLite connection is closed")

