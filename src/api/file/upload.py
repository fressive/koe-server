from model.config import Config
from model.file import File as FileM, FileType
from util import audio, response
from util.channel import chan
from util.file_provider import FileProvider

import hashlib
from fastapi import Depends, APIRouter, Query, File, UploadFile
from typing import List
from mongoengine.errors import NotUniqueError

router = APIRouter()

# TODO: Refactor to GraphQL Upload

@router.post("/file/upload", summary="Upload files")
async def file_upload(files: List[UploadFile] = File(...)):

    result = []
    for file in files:
        try:
            data = file.file.read()
            md5 = hashlib.md5(data).hexdigest()
            
            file_type = FileType.parse_from_content_type(file.content_type)
            file_data = audio.get_audio_metadata(data) if file_type == "audio" else {}
            
            extension = file.filename.split(".")[-1]

            provider = Config.get("file_provider")
            
            model = FileM(
                md5=md5, 
                extension=extension, 
                file_type=file_type, 
                provider=provider,
                metadata=file_data
            )

            model.save()
            FileProvider.get_instance(provider).write(md5, data)
            
            res = {
                "file_id": str(model.id),
                "filename": file.filename,
                "md5": md5,
                "filetype": file_type,
                "data": file_data,
                "code": 200
            }

            result.append(res)

            chan.publish("file_uploaded", {
                "model": model,
                "result": res,
                "raw": data
            })
            
        except NotUniqueError as e:
            res = {
                "filename": file.filename,
                "code": 400
            }

            result.append(res)
    

    return response.response_ok(result)