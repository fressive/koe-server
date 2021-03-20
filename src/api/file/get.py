from model.config import Config
from model.file import File as FileM, FileType
from util import audio, response
from util.file_provider import FileProvider

import hashlib
import io
from fastapi import APIRouter

router = APIRouter()

@router.get("/file/hash/{md5}", summary="Get file by hash")
async def get_file(md5: str):
    try:
        model = FileM.objects.get(md5=md5)

        provider = Config.get("file_provider")

        return response.response_file(FileProvider.get_instance(provider).read(md5))
    except:
        return response.response_not_found(message="File not found")

@router.get("/file/id/{id}", summary="Get file by id")
async def get_file(id: str):
    try:
        model = FileM.objects.get(id=id)

        provider = Config.get("file_provider")

        return response.response_file(FileProvider.get_instance(provider).read(model.md5))
    except:
        return response.response_not_found(message="File not found")

