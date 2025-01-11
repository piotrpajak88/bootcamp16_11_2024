from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///moja_baza_danych.db")
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books=relationship("Book", back_populates='author')

    def __repr__(self):
        return self.name

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book" , back_populates='publisher')

    def __repr__(self):
        return self.name

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship("Publisher", back_populates='books')

    def __repr__(self):
        return self.title

# tworzenie tabel w bazie danych na podtsawie encji
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_author = Author(name = "Adam Mickiewicz")
new_publisher = Publisher(name="Wydawnictwo XYZ")
new_author2 = Author(name = "Tolkien")

pt = Book(title= "Pan Tadeusz", author = new_author, publisher = new_publisher)
lotr = Book(title = "Lord of the Rings", author = new_author2, publisher = new_publisher)

# session.add(pt)
# session.add(lotr)

# session.add_all(
#     [new_author, new_author2, new_publisher, pt, lotr]
# )

session.commit()

author_book_list = session.query(Author,Book).join(Book,Author.id==Book.author_id).all()
publisher_list = session.query(Publisher,Book).join(Book,Publisher.id==Book.publisher_id).all()
autor_ksiazka_wydawca = session.query(Author,Book,Publisher).join(Book,Author.id==Book.author_id).join(Publisher,Publisher.id==Book.publisher_id).all()

session.close()

print(author_book_list)
print(publisher_list)
print(autor_ksiazka_wydawca)
#
# [(Adam Mickiewicz, Pan Tadeusz), (Tolkien, Lord of the Rings), (Adam Mickiewicz, Pan Tadeusz), (Tolkien, Lord of the Rings)]
# [(Wydawnictwo XYZ, Pan Tadeusz), (Wydawnictwo XYZ, Lord of the Rings), (Wydawnictwo XYZ, Pan Tadeusz), (Wydawnictwo XYZ, Lord of the Rings)]
# [(Adam Mickiewicz, Pan Tadeusz, Wydawnictwo XYZ), (Tolkien, Lord of the Rings, Wydawnictwo XYZ), (Adam Mickiewicz, Pan Tadeusz, Wydawnictwo XYZ), (Tolkien, Lord of the Rings, Wydawnictwo XYZ)]