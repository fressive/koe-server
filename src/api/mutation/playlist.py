from api.query.playlist import Playlist
from model.playlist import Playlist as PlaylistM

import graphene

class CreatePlaylist(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(default_value="")
        songs = graphene.List(graphene.String, default_value=[])

    ok = graphene.Boolean()
    playlist = graphene.Field(lambda: Playlist)

    @staticmethod
    def mutate(root, info, name, description, songs):
        model = PlaylistM(name=name, description=description, songs=songs)
        model.save()

        playlist = model
        ok = True
        return CreatePlaylist(playlist=playlist, ok=ok)
