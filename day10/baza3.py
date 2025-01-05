import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("../day10/sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Connected to SQLite")

    insert = '''
    INSERT INTO software (id,name,price)
    VALUES (5,"SQL",199);
    '''
    insert2 = '''
    INSERT INTO software (id,name,price)
    VALUES (7,"T-SQL",999);
    '''
    # cursor.execute(insert)
    # cursor.execute(insert2)
    # sql_connection.commit()

    select = """
    SELECT * FROM software
    """

    for row in cursor.execute(select):
        print(row)

    # Connected to SQLite
    # (1, 'Python', 100.0)
    # (2, 'Java', 50.0)
    # (3, 'SQL', 199.0)
    # (5, 'SQL', 199.0)
    # (7, 'T-SQL', 999.0)
    # SQLite connection is closed


except sqlite3.Error as e:
    print("Bład bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("SQLite connection is closed")