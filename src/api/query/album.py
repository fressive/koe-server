from model.media import Album as AlbumM

import graphene
from graphene_mongo import MongoengineObjectType

class Album(MongoengineObjectType):
    class Meta:
        model = AlbumM