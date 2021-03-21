import graphene
from model.media import Lyric as LyricM
from graphene_mongo import MongoengineObjectType

class Lyric(MongoengineObjectType):
    class Meta:
        model = LyricM