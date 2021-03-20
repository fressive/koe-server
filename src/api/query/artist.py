from model.media import Artist as ArtistM

import graphene
from graphene_mongo import MongoengineObjectType

class Artist(MongoengineObjectType):
    class Meta:
        model = ArtistM