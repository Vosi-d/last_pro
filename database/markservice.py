from database.models import StudentMarks
from database import get_db

def get_all_marks_db():
    db = next(get_db())

    all_marks = db.query(StudentMarks).all()

    return all_marks

def get_exact_mark_db(mark_id):
    db = next(get_db())

    exact_mark = db.query(StudentMarks).filter_by(mark_id=mark_id).first()

    if exact_mark:
        return exact_mark

    return 'Mark is not found'

def add_new_mark_db(student_id, mark_mark, publish_date):
    db = next(get_db())

    new_mark = StudentMarks(student_id=student_id, mark_mark=mark_mark, publish_date=publish_date)

    db.add(new_mark)
    db.commit()

    return 'Posted'

def edit_mark_db(mark_id, new_mark):
    db = next(get_db())

    exact_mark = db.query(StudentMarks).filter_by(mark_id=mark_id).first()

    if exact_mark:
        exact_mark.mark_mark = new_mark
        db.commit()

        return 'Mark was edited'

    return 'Mark is not found'

def delete_mark_db(mark_id):
    db = next(get_db())

    exact_mark = db.query(StudentMarks).filter_by(mark_id=mark_id).first()

    if exact_mark:
        db.delete(exact_mark)
        db.commit()

        return 'Successfully deleted'

    return 'Mark is not found'

