from database.models import Student
from database import get_db

def get_all_students_db():
    db = next(get_db())

    all_students = db.query(Student).all()

    return all_students

def get_exact_student_db(student_id):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id).first()

    if exact_student:
        return exact_student

    return False

def add_new_student(name, surname, email, password, reg_date):
    db = next(get_db())

    checker = db.query(Student).filter_by(email=email).first()

    if checker:
        return 'This email is already registered'
    else:
        new_student = Student(name=name, surname=surname, email=email, password=password, reg_date=reg_date)

        db.add(new_student)
        db.commit()

        return 'Student is registered'

def login_student_db(email, password):
    db = next(get_db())

    student = db.query(Student).filter_by(email=email, password=password).first()

    if student:
        return student

    return 'Error'

def edit_student_info_db(student_id, edit_info, new_info):
    db = next(get_db())

    exact_student = get_exact_student_db(student_id)

    if exact_student:
        if edit_info == 'email':
            exact_student.email = new_info

        elif edit_info == 'password':
            exact_student.password = new_info

        elif edit_info == 'name':
            exact_student.name = new_info

        db.commit()

        return 'Info changed'

    return 'Student not found'

def delete_student_db(student_id):
    db = next(get_db())

    student = db.query(Student).filter_by(student_id=student_id).first()

    if student:
        db.delete(student)
        db.commit()

        return 'Student was deleted'

    return 'Student was not found'



