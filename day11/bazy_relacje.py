from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///address_book.db', echo=True)

Base = declarative_base()


# encje - klasy odwzorujace tabele w bazie danych

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __repr__(self):
        return self.email


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name='Anakin', age=38)
anakin2 = Person(name='Anakin Anakin', age=38)
anakin2.addresses = [Address(email='anakin@wp.pl'),
                     Address(email='vader@gmail.com')]

leia = Person(name='Leia', age=36)
leia.addresses = [Address(email='leia@gmail.com'),
                  Address(email='leia123@gmail.com'),
                  Address(email='anakinleftme@gmail.com')]


r2d2 = Person(name='R2-D2', age=123)
r2d2.addresses = [Address(email='r2d2@gmail.com'),
                  Address(email='thebestrobot@gmail.com'),
                  Address(email='r2d2@wp.pl')]
new_r2d2 = Person(name='New R2-D2', age=123)
r2d2.addresses = [Address(email='newartuditu@gmail.com')]
r2d2_3 = Person(name='R2-D2_3', age=123)
r2d2.addresses = [Address(email='artuditu@gmail.com')]

# session.add(anakin)
# session.add(anakin2)
#session.add(r2d2)
#session.add(new_r2d2)
#session.add(r2d2_3)

session.commit()

all_ = session.query(Person).all()
all2_ = session.query(Address).all()
print(all_)
print(all2_)

# 2025-01-11 10:42:44,067 INFO sqlalchemy.engine.Engine SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person
# 2025-01-11 10:42:44,067 INFO sqlalchemy.engine.Engine [generated in 0.00013s] ()
# [Anakin (id=1), Anakin Anakin (id=2), Leia (id=3)]

first = session.query(Person).first()
print(first)

# 2025-01-11 10:43:48,441 INFO sqlalchemy.engine.Engine SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person
#  LIMIT ? OFFSET ?
# 2025-01-11 10:43:48,441 INFO sqlalchemy.engine.Engine [generated in 0.00011s] (1, 0)
# Anakin (id=1)

print(type(first))  # <class '__main__.Person'>

print(first.name, first.age) # Anakin 38

anakin_list = session.query(Person).filter(
    Person.name.like('Anakin%')
).all()
print(anakin_list)


# 2025-01-11 10:48:34,865 INFO sqlalchemy.engine.Engine SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person
# WHERE person.name LIKE ?
# 2025-01-11 10:48:34,865 INFO sqlalchemy.engine.Engine [generated in 0.00012s] ('Anakin%',)
# [Anakin (id=1), Anakin Anakin (id=2)]

r2d2_name_list = session.query(Person).filter(
    Person.name.like('%R2-D2%')
).all()

r2d2_id_list = session.query(Person).filter(
    Person.id.in_([2,3])
).all()

r2d2_mail_list = (session.query(Person,Address).join(Address,Person.id==Address.person_id).all())

#print(r2d2_name_list)
#print(r2d2_id_list)
print(r2d2_mail_list)