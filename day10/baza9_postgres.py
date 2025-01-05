import psycopg2

# conn = psycopg2.connect(
#     host='localhost',
#     port = 5432,
#     database = "mydatabase",
#     user = "myuser",
#     password = ''
# )

conn = psycopg2.connect(
    host='localhost',
    port = 5432,
    database='mydatabase',
    user='postgres',
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, email TEXT);")
conn.commit()

cursor.execute("INSERT INTO users (name, email) VALUES(%s, %s)", ("Jan","jan@rajkonkret.pl"))
cursor.execute("INSERT INTO users (name, email) VALUES(%s, %s)", ("Anna","anna@rajkonkret.pl"))

conn.commit()
# Replace these values with your own database credentials