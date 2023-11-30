from registration import student_router, RegisterModel, LoginModel
from database.studentservice import add_new_student, login_student_db, delete_student_db

@student_router.post('/register-student')
def register_student(data: RegisterModel):
    register_data = data.model_dump()
    result = add_new_student(**register_data)

    return {'status': 1, 'message': result}


@student_router.post('/login')
def login_student(data: LoginModel):
    login_data = data.model_dump()
    result = login_student_db(**login_data)

    return {'status': 1, 'message': result}


@student_router.delete('/delete')
def delete_student(student_id: int):
    result = delete_student_db(student_id)

    return {'status': 1, 'message': result}



