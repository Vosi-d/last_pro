from fastapi import Body
from datetime import datetime
from student_mark import marks_router
from database.markservice import add_new_mark_db, delete_mark_db, edit_mark_db, get_exact_mark_db, get_all_marks_db

@marks_router.get('/all-marks')
async def get_all_marks():
    result = get_all_marks_db()

    return {'status': 1, 'message': result}

@marks_router.get('/exact-mark')
async def get_exact_mark(mark_id: int):
    result = get_exact_mark_db(mark_id)

    return {'status': 1, 'message': result}

@marks_router.delete('/delete-mark')
async def delete_mark(mark_id: int):
    result = delete_mark_db(mark_id)

    return {'status': 1, 'message': result}

@marks_router.put('/edit-mark')
async def change_mark(mark_id: int = Body(...),
                      new_mark: int = Body(...)):
    result = edit_mark_db(mark_id, new_mark)

    return {'status': 1, 'message': result}

@marks_router.post('/new-mark')
async def new_student_mark(student_id: int = Body(...), mark_mark: int = Body(...)):
    result = add_new_mark_db(student_id=student_id, mark_mark=mark_mark,
                             publish_date=datetime.now())
    return {'status': 1, 'message': result}
