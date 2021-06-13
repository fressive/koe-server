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
        data = FileProvider.get_instance(provider).read(md5)
        data_stream = FileProvider.get_instance(provider).open(md5)

        return response.response_file(data_stream, extension=model.extension, content_length=len(data))
    except:
        return response.response_not_found(message="File not found")

@router.get("/file/id/{id}", summary="Get file by id")
async def get_file(id: str):
    try:
        model = FileM.objects.get(id=id)

        provider = Config.get("file_provider")
        data = FileProvider.get_instance(provider).read(model.md5)
        data_stream = FileProvider.get_instance(provider).open(model.md5)

        return response.response_file(data_stream, extension=model.extension, content_length=len(data))
    except:
        raise
        return response.response_not_found(message="File not found")

@router.head("/file/id/{id}")
async def head_file(id: str):
    try:
        model = FileM.objects.get(id=id)

        provider = Config.get("file_provider")
        data = FileProvider.get_instance(provider).read(model.md5)

        return response.response_file_headers(extension=model.extension, content_length=len(data))
    except:
        raise
        return response.response_not_found(message="File not found")
