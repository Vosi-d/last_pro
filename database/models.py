from sqlalchemy import Integer, String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    reg_date = Column(DateTime)

class StudentMarks(Base):
    __tablename__ = 'student_marks'
    mark_id = Column(Integer, autoincrement=True, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    mark_mark = Column(Integer)

    publish_date = Column(DateTime)

    student_fk = relationship(Student, lazy='subquery')

class MarkComment(Base):
    __tablename__ = 'mark_comments'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)
    mark_id = Column(Integer, ForeignKey('student_marks.mark_id'))
    student_id = Column(Integer, ForeignKey('students.student_id'))

    comment_text = Column(String)

    publish_date = Column(DateTime)

    mark_fk = relationship(StudentMarks, lazy='subquery')



