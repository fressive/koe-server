import graphene
from model.playlist import Playlist as PlaylistM
from graphene_mongo import MongoengineObjectType

class Playlist(MongoengineObjectType):
    class Meta:
        model = PlaylistM