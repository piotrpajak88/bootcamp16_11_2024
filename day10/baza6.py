import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("../day10/sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Connected to SQLite")

    update = '''
    UPDATE software SET price = 1999 WHERE id = 7;
    '''
    # cursor.execute(update)
    # sql_connection.commit()

    delete = '''
        DELETE FROM software WHERE id = 1; 
        '''

    # cursor.execute(delete)
    # sql_connection.commit()


    select = '''
        SELECT * FROM software WHERE price > 500; 
        '''
    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("Bład bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("SQLite connection is closed")