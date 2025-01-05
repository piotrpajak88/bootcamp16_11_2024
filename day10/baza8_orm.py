from sqlalchemy import create_engine, Column, Integer, String, text, select
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# klasy odwzorowujace tabele - encje
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

def __repr__(self):
    return f"<User(name={self.name}, age={self.age}>"

    #Tworzenie polaczenia z baza danych
engine = create_engine('sqlite:///mydatabase.db', echo=True) #zwraca silnik
Base.metadata.create_all(engine) #Tworzy tabele w bazie danych

# 2025-01-05 12:34:07,324 INFO sqlalchemy.engine.Engine
# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age INTEGER,
# 	PRIMARY KEY (id)
# )


Session = sessionmaker(bind=engine) #tworzy sesję
session = Session() #utworzenie sesji

new_user = User(name='Jan Kowalski', age=30)
session.add(new_user) #dodanie do sesji
session.commit() #zapisanie zmian w bazie danych
session.close()

# 2025-01-05 12:34:07,335 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-01-05 12:34:07,336 INFO sqlalchemy.engine.Engine INSERT INTO users (name, age) VALUES (?, ?)
# 2025-01-05 12:34:07,336 INFO sqlalchemy.engine.Engine [generated in 0.00011s] ('Jan Kowalski', 30)
# 2025-01-05 12:34:07,336 INFO sqlalchemy.engine.Engine COMMIT

users = session.query(User).all()
for user in users:
    print(user)
    print(f"imie: {user.name} wiek: {user.age}")


# 2025-01-05 12:40:44,419 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-01-05 12:40:44,420 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
# 2025-01-05 12:40:44,420 INFO sqlalchemy.engine.Engine [generated in 0.00010s] ()
# <__main__.User object at 0x000001D3039C9E20>
# imie: Jan Kowalski wiek: 30

result = session.execute(text("SELECT * FROM users"))

for row in result:
    print(row)

# (1, 'Jan Kowalski', 30)
# (2, 'Jan Kowalski', 30)
# (3, 'Jan Kowalski', 30)
# (4, 'Jan Kowalski', 30)
# (5, 'Jan Kowalski', 30)

users1 = select(User.objects.all)
result1 = session.scalars(users1)

for row in result1:
    print(row)
