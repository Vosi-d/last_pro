from fastapi import FastAPI
from database import Base, engine

from student_mark import marks_router
from registration import student_router
from profile import profile_router
from comment import comment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(student_router)
app.include_router(profile_router)
app.include_router(marks_router)
app.include_router(comment_router)
