from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

student_router = APIRouter(prefix='/student', tags=['Student'])

class RegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    reg_date: datetime = datetime.now()

class LoginModel(BaseModel):
    email: str
    password: str

from registration import registration_api

