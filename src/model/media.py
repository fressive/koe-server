from enum import Enum

from model.file import File

from datetime import datetime
from mongoengine import *

class Artist(Document):
    meta = {'collection': 'artist'}

    name = StringField(required=True)
    country = StringField()
    aliases = ListField(StringField())
    cover_files = ListField(ReferenceField(File))

class Album(Document):

    meta = {'collection': 'album'}

    name = StringField(required=True)
    artists = ListField(ReferenceField(Artist), required=True)
    cover_files = ListField(ReferenceField(File))
    released_date = DateField()

class Song(Document):

    title = StringField(required=True)
    artists = ListField(ReferenceField(Artist), required=True)
    album = ReferenceField(Album, required=True)
    update_time = DateTimeField(default=datetime.now(), required=True)

    aliases = ListField(StringField())
    lyrics = ListField(ReferenceField(File))
    audio_files = ListField(ReferenceField(File))
    cover_files = ListField(ReferenceField(File))

class Lyric(Document):
    md5 = StringField(required=True, unique=True)
    lyric = StringField(required=True)
    source = StringField(required=True)
    type = StringField(required=True)
    song = ReferenceField(Song, required=True)
    language = StringField(required=True)
