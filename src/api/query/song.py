import graphene
from model.media import Song as SongM
from graphene_mongo import MongoengineObjectType

class Song(MongoengineObjectType):
    class Meta:
        model = SongM