from api.query.album import Album
from model.file import File as FileM
from model.media import Album as AlbumM, Artist as ArtistM

import graphene
from datetime import datetime

class CreateAlbum(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        artists_id = graphene.List(graphene.String, required=True)
        cover_files = graphene.List(graphene.String, default_value=[])
        released_date = graphene.DateTime(default_value=datetime.now())

    ok = graphene.Boolean()
    album = graphene.Field(lambda: Album)

    @staticmethod
    def mutate(root, info, name, artists_id, cover_files, released_date):
        model = AlbumM(
            name=name, 
            artists=[ArtistM.objects.get(id=x) for x in artists_id],
            cover_files=[FileM.objects.get(id=x) for x in cover_files],
            released_date=released_date
        )
        model.save()

        album = model
        ok = True
        return CreateAlbum(album=album, ok=ok)
