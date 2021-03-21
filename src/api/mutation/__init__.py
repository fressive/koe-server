import graphene
from api.mutation import artist, song, album, playlist

class Mutation(graphene.ObjectType):
    create_album = album.CreateAlbum.Field()
    create_artist = artist.CreateArtist.Field()
    create_song = song.CreateSong.Field()
    create_playlist = playlist.CreatePlaylist.Field()