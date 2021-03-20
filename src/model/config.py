from mongoengine import *

class Config(Document):
    meta = {'collection': 'config'}

    key = StringField(required=True)
    value = StringField(required=True)
    default = StringField(required=True)

    @staticmethod
    def create(key, value, default):
        try:
            Config.objects.get(key=key)
        except:
            Config(key=key, value=value, default=default).save()

    @staticmethod
    def get(key):
        try:
            return Config.objects.get(key=key).value
        except:
            raise

    @staticmethod
    def set(key, value):
        Config.objects(key=key).update(value=value)

    @staticmethod
    def set_to_default(key):
        Config.set(key, Config.get(key).default)

    @staticmethod
    def initialize():
        Config.create("data_save_path", "./data", "./data")
        Config.create("file_provider", "local_storage", "local_storage")
        Config.create("audio_transcoding_size_limit", "true", str(1024 * 1024 * 10))
        