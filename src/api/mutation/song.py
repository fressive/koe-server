from api.query.song import Song
from model.file import File as FileM
from model.media import Album as AlbumM, Artist as ArtistM, Song as SongM
from util.channel import chan

import graphene

class CreateSong(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        artists_id = graphene.List(graphene.String, required=True)
        album_id = graphene.String(required=True)

        aliases = graphene.List(graphene.String, default_value=[])
        cover_files = graphene.List(graphene.String, default_value=[])
        audio_files = graphene.List(graphene.String, default_value=[])

    ok = graphene.Boolean()
    song = graphene.Field(lambda: Song)

    @staticmethod
    def mutate(root, info, title, artists_id, album_id, aliases, cover_files, audio_files):
        model = SongM(
            title=title, 
            artists=[ArtistM.objects.get(id=x) for x in artists_id],
            album=AlbumM.objects.get(id=album_id),
            aliases=aliases,
            cover_files=[FileM.objects.get(id=x) for x in cover_files],
            audio_files=[FileM.objects.get(id=x) for x in audio_files]
        )

        model.save()
        
        chan.publish("song_added", {
            "model": model
        })

        song = model
        ok = True
        return CreateSong(ok=ok, song=song)
