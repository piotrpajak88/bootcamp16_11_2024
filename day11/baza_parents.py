from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# engine = create_engine("sqlite:///:memory:", echo=True)
engine = create_engine("sqlite:///parents_databases.db", echo=False)
Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    children = relationship("Child", backref="parent") # backref - doda pole parent w klasie Child automatycznie
    # przy back_populates musielismy w klasie Child samodzielnie zdefiniowac to pole z relacja

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id')) # relacja jeden do jednego

    def __repr__(self):
        return f"id={self.id}, name={self.name}"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

parent1 = Parent(name="Adam")
child1 = Child(name = "Abel", parent = parent1)
child2 = Child(name = "Kain", parent = parent1)
child3 = Child(name = "Set", parent = parent1)

# session.add(parent1)
# session.add(child1)
# session.add(child2)
# session.add(child3)

# session.add_all(
#     [parent1,child1,child2,child3]
# )

session.commit()

our_parent = session.query(Parent).all()
print(our_parent)

our_parent_filtered = session.query(Parent).filter_by(name = "Adam").first()
print(our_parent_filtered.name)

print(5 * '-')

children = our_parent_filtered.children

for child in children:
    print(child.name)

    # Abel
    # Kain
    # Set

