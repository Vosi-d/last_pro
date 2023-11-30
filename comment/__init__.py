from fastapi import APIRouter

comment_router = APIRouter(prefix='/comments', tags=['Comments'])

from comment import comment_api
