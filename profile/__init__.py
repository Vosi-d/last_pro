from fastapi import APIRouter

profile_router = APIRouter(prefix='/profile', tags=['Profile'])

from profile import profile_api

