from fastapi import APIRouter
from api.file import upload, get

file_api = APIRouter()
file_api.include_router(upload.router, tags=["File"])
file_api.include_router(get.router, tags=["File"])