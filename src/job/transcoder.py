import job
from loguru import logger

def audio_transcode(data):
    pass

@job.receiver("file_uploaded")
def receiver(data):
    logger.info("New file `{0}` uploaded", data["result"]["filename"])
    if data["result"]["filetype"] == "audio":
        pass