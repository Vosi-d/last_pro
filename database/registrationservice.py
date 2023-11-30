from database.models import LoginModel, RegisterModel
from database import get_db
from datetime import datetime

from database.models import RegisterModel
from database import get_db


# Регистрация пользователя (name, surname, email, phone_number, pass)
def register_user_db(name, surname, email, phone_number,
                     password, city, reg_date):
    db = next(get_db())

    new_user = RegisterModel(name=name, surname=surname, email=email,
                    phone_number=phone_number, password=password, city=city,
                    reg_date=reg_date)
    db.add(new_user)
    db.commit()

    return 'Succsefully registretion'

# Получить инфо о пользователе
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(RegisterModel).filter_by(user_id=user_id).first()

    return exact_user

# Проферка данных через (email)
def check_user_email_db(email):
    db = next(get_db())

    checker = db.query(RegisterModel).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return 'Not found email!'

# Изменить данные у полльзователя
def edit_user_db(user_id, edit_type, new_data):
    db = next(get_db())

    exact_user = db.query(RegisterModel).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data
        elif edit_type == 'password':
            exact_user.password = new_data
        elif edit_type == 'city':
            exact_user.city = new_data

        db.commit()

        return 'Date edit succsefully'
    else:
        return 'User not found'


# Удаления пользователя (user_id)
def delete_user_db(user_id):
    db = next(get_db())

    delete_user = db.query(RegisterModel).filter_by(user_id=user_id).first()

    if delete_user:
        db.delete(delete_user)
        db.commit()

        return 'User succsefully deleted'
    else:
        return 'User not found'