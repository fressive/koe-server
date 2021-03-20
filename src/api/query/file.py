from model.file import File as FileM

import graphene
from graphene_mongo import MongoengineObjectType

class File(MongoengineObjectType):
    class Meta:
        model = FileM