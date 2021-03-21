from api.query import artist, album, song, file, lyric, playlist
from model.file import File as FileM
from model.media import Album as AlbumM, Artist as ArtistM, Song as SongM, Lyric as LyricM
from model.playlist import Playlist as PlaylistM
from mongoengine import Q

import re
import graphene
import _global


class Query(graphene.ObjectType):
    artists = graphene.List(
        artist.Artist, 
        keywords=graphene.Argument(graphene.List(graphene.String), default_value=""),
        regexp=graphene.Argument(graphene.String, default_value=".*{}.*"),
        page=graphene.Argument(graphene.Int, default_value=0), 
        limit=graphene.Argument(graphene.Int, default_value=100)
    )
    albums = graphene.List(
        album.Album, 
        keywords=graphene.Argument(graphene.List(graphene.String), default_value=""),
        regexp=graphene.Argument(graphene.String, default_value=".*{}.*"),
        page=graphene.Argument(graphene.Int, default_value=0), 
        limit=graphene.Argument(graphene.Int, default_value=100)
    )
    songs = graphene.List(song.Song, page=graphene.Argument(graphene.Int, default_value=0), limit=graphene.Argument(graphene.Int, default_value=100))
    files = graphene.List(file.File, page=graphene.Argument(graphene.Int, default_value=0), limit=graphene.Argument(graphene.Int, default_value=100))
    lyrics = graphene.List(lyric.Lyric, songId=graphene.Argument(graphene.String, required=True), page=graphene.Argument(graphene.Int, default_value=0), limit=graphene.Argument(graphene.Int, default_value=100))
    playlists = graphene.List(playlist.Playlist, playlistId=graphene.Argument(graphene.String, default_value=""), page=graphene.Argument(graphene.Int, default_value=0), limit=graphene.Argument(graphene.Int, default_value=100))
    
    version = graphene.String(default_value=_global.version)

    @staticmethod
    def resolve_artists(root, info, keywords, regexp, page, limit):
        _filter = Q()
        if keywords:
            for i in keywords:
                regex = re.compile(regexp.format(i))
                _filter = _filter | (Q(name=regex) | Q(aliases__in=[regex]))

        return list(ArtistM.objects.filter(_filter).skip(page * limit).limit(limit))

    @staticmethod
    def resolve_albums(root, info, keywords, regexp, page, limit):
        _filter = Q()
        if keywords:
            for i in keywords:
                regex = re.compile(regexp.format(i))
                _filter = _filter | Q(name=regex)

        return list(AlbumM.objects.filter(_filter).skip(page * limit).limit(limit))

    @staticmethod
    def resolve_songs(root, info, page, limit):
        return list(SongM.objects.skip(page * limit).limit(limit))
        
    @staticmethod
    def resolve_files(root, info, page, limit):
        return list(FileM.objects.skip(page * limit).limit(limit))

    @staticmethod
    def resolve_lyrics(root, info, songId, page, limit):
        return list(LyricM.objects.filter(song=songId).skip(page * limit).limit(limit))

    @staticmethod
    def resolve_playlists(root, info, playlistId, page, limit):
        _filter = Q()
        if not playlistId == "":
            _filter = _filter | Q(id=playlistId)
        return list(PlaylistM.objects.filter(_filter).skip(page * limit).limit(limit))