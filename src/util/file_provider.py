from model.config import Config

import os

class FileProvider:
    @staticmethod
    def save(md5, data):
        pass

    @staticmethod
    def get(md5):
        pass

    @staticmethod
    def open(md5):
        pass

    @staticmethod
    def get_instance(provider):
        if provider == "local_storage":
            return LocalStorage()
        elif provider == "gridfs_storage":
            return GridFSStorage()
        else:
            return LocalStorage()

class LocalStorage(FileProvider):
    @staticmethod
    def write(md5, data):
        save_path = Config.get("data_save_path")
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        with open(os.path.join(save_path, md5), 'wb') as file:
            file.write(data)

    @staticmethod
    def read(md5):
        save_path = Config.get("data_save_path")
        with open(os.path.join(save_path, md5), 'rb') as file:
            return file.read()

    @staticmethod
    def open(md5):
        save_path = Config.get("data_save_path")
        return open(os.path.join(save_path, md5), 'rb')

class GridFSStorage(FileProvider):
    @staticmethod
    def save(md5, data):
        pass

    @staticmethod
    def get(md5):
        pass

    @staticmethod
    def open(md5):
        pass