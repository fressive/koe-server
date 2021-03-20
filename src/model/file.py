from mongoengine import *
from enum import Enum
from datetime import datetime
from model.config import Config
from util.file_provider import FileProvider

import hashlib

class FileType(Enum):
    image = "image"
    audio = "audio"
    others = "others"

    @staticmethod
    def parse_from_content_type(content_type):
        if content_type.startswith("image"):
            return "image"
        elif content_type.startswith("audio"):
            return "audio"
        else:
            return "others"

class File(Document):
    """
        
    """
    md5 = StringField(required=True, unique=True)
    extension = StringField(required=True)
    file_type = StringField(required=True)
    update_time = DateTimeField(default=datetime.now(), required=True)
    provider = StringField(required=True)
    metadata = DictField()

    @staticmethod
    def create(data, extension, file_type, metadata = {}):
        md5 = hashlib.md5(data).hexdigest()

        result = File.objects(md5=md5).first()
        if not result:
            provider = Config.get("file_provider")

            result = File(
                md5=md5, 
                extension=extension, 
                file_type=file_type, 
                provider=provider,
                metadata=metadata
            )
            result.save()

            FileProvider.get_instance(provider).write(md5, data)
            
        return result
            
    def read(self):
        return FileProvider.get_instance(self.provider).read(self.md5)