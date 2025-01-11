from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


Base = declarative_base()

#tabela asocjacyjna
student_course_table = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    courses = relationship("Course", secondary=student_course_table, back_populates = "students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    students = relationship("Student", secondary=student_course_table, back_populates="courses")


engine = create_engine('sqlite:///kursy.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#dodawanie studenta
student1 = Student(name="Anna Kowalska")
student2 = Student(name="Jan Nowak")

course1 = Course(name = "Programowanie w Pythonie dla zaawansowanych")
course2 = Course(name = "Programowanie w T-SQL dla profesjonalistow")

# student1.courses.append(course1)
# student1.courses.append(course2)
#
# student2.courses.append(course1)
#
# session.add(student1)
# session.add(student2)
#
# session.commit()


our_student = session.query(Student).filter_by(name="Anna Kowalska").first()
print(f"Student: {our_student.name}")
for course in our_student.courses:
    print(f"Kurs: {course.name}")

# Student: Anna Kowalska
# Kurs: Programowanie w Pythonie dla zaawansowanych
# Kurs: Programowanie w T-SQL dla profesjonalistow


our_course = session.query(Course).first()
print(our_course.name)
for student in our_course.students:
    print(f"Student: {student.name}")

# Programowanie w Pythonie dla zaawansowanych
# Student: Anna Kowalska
# Student: Jan Nowak


