from api.query import artist, album, song, file
from model.file import File as FileM
from model.media import Album as AlbumM, Artist as ArtistM, Song as SongM
from mongoengine import Q

import re
import graphene
import _global


class Query(graphene.ObjectType):
    artists = graphene.List(
        artist.Artist, 
        keywords=graphene.Argument(graphene.List(graphene.String), default_value=None),
        regex=graphene.Argument(graphene.String, default_value=".*{}.*"),
        page=graphene.Argument(graphene.Int, default_value=0), 
        limit=graphene.Argument(graphene.Int, default_value=100)
    )
    albums = graphene.List(
        album.Album, 
        keywords=graphene.Argument(graphene.List(graphene.String), default_value=None),
        regex=graphene.Argument(graphene.String, default_value=".*{}.*"),
        page=graphene.Argument(graphene.Int, default_value=0), 
        limit=graphene.Argument(graphene.Int, default_value=100)
    )
    songs = graphene.List(song.Song, page=graphene.Argument(graphene.Int, default_value=0), limit=graphene.Argument(graphene.Int, default_value=100))
    files = graphene.List(file.File, page=graphene.Argument(graphene.Int, default_value=0), limit=graphene.Argument(graphene.Int, default_value=100))
    
    version = graphene.String(default_value=_global.version)

    @staticmethod
    def resolve_artists(root, info, keywords, regex, page, limit):
        _filter = Q()
        if keywords:
            for i in keywords:
                regex = re.compile(regex.format(i))
                _filter = _filter | (Q(name=regex) | Q(aliases__in=[regex]))

        return list(ArtistM.objects.filter(_filter).skip(page * limit).limit(limit))

    @staticmethod
    def resolve_albums(root, info, keywords, regex, page, limit):
        _filter = Q()
        if keywords:
            for i in keywords:
                regex = re.compile(regex.format(i))
                _filter = _filter | Q(name=regex)

        return list(AlbumM.objects.filter(_filter).skip(page * limit).limit(limit))

    @staticmethod
    def resolve_songs(root, info, page, limit):
        return list(SongM.objects.skip(page * limit).limit(limit))
        
    @staticmethod
    def resolve_files(root, info, page, limit):
        return list(FileM.objects.skip(page * limit).limit(limit))