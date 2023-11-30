from fastapi import APIRouter


marks_router = APIRouter(prefix='/mark', tags=['Marks'])

from student_mark import students_mark_api
