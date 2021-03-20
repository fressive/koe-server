import audio_metadata

def get_audio_metadata(data):
    md = audio_metadata.loads(data)
    si = md["streaminfo"]
    tags = md["tags"]
    return {
        "tags": {
            "album": tags.get("album", None),
            "artist": tags.get("artist", None),
            "title": tags.get("title", None)
        },
        "streaminfo": {
            "bitrate": si.bitrate,
            "duration": si.duration,
            "sample_rate": si.sample_rate
        }
    }
    
def get_audio_cover(data):
    md = audio_metadata.loads(data)
    if len(md["pictures"]) == 0:
        return None
    else:
        return md["pictures"][0]
    