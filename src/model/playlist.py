from model.media import Song

from mongoengine import *

class Playlist(Document):
    name = StringField(required=True, unique=True)
    description = StringField(default="")
    songs = ListField(ReferenceField(Song, reverse_delete_rule=CASCADE), default=[])