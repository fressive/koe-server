
"""
    The job is used for handling metadata, cover processing and audio transcoding.
"""

import job

from model.media import Song
from loguru import logger
from util import audio

from model.file import File

def fetch_cover(model):
    """
        The function will automatically fetch the cover for the song and the album if the `cover_files` 
        is missing.
    """
    if len(model.audio_files) == 0:
        return

    cover = audio.get_audio_cover(model.audio_files[0].read())
    if cover:    
        cover_model = File.create(
            cover["data"], 
            cover["mime_type"].split("/")[-1], 
            "image", 
            {
                "height": cover["height"], 
                "width": cover["width"], 
                "mime_type": cover["mime_type"], 
                "description": cover["description"]
            }
        )
        if len(model.cover_files) == 0:
            model.cover_files.append(cover_model)
            model.save()

        album_model = model.album
        if len(album_model.cover_files) == 0:
            album_model.cover_files.append(cover_model)
            album_model.save()
        
def update_metadata(model):
    """
        This function will automatically update the related metadata of the song. 
    """
    # TODO: complete this
    pass

@job.receiver("song_added")
def recevier(data): 
    model = data["model"]

    logger.info("New song `{0} - {1}` uploaded", "/".join(map(lambda x: x.name, model.artists)), model.title)
    fetch_cover(model)
