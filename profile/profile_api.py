from fastapi import Body

from profile import profile_router
from database.studentservice import get_exact_student_db, get_all_students_db, edit_student_info_db
@profile_router.get('/exact-student')
async def exact_student_info(student_id: int):
    result = get_exact_student_db(student_id)

    if result:
        return {'status': 1, 'message': result}

    else:
        return {'status': 0, 'message': 'Not found'}

@profile_router.get('/all-students')
async def all_students_info():
    result = get_all_students_db()

    return {'status': 1, 'message': result}


@profile_router.put('/edit-student')
async def edit_student(student_id: int = Body(...),
                       new_info: str = Body(...),
                       edit_info: str = Body(...)):
    result = edit_student_info_db(student_id=student_id, edit_info=edit_info, new_info=new_info)

    return {'status': 1, 'message': result}



