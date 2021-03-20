"""
    The job is used for automatically fetch lyrics from the web.
"""
import job
from model.media import Lyric

import requests
from NetEaseMusicApi import api
from loguru import logger

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"

class LyricProvider:
    @staticmethod
    def fetch(artist, album, title):
        pass

class NeteaseLP(LyricProvider):
    @staticmethod
    def fetch(artist, album, title):
        song = api.search.songs("{} {} {}".format(artist, album, title))
        if not song:
            return None

        song_id = song[0]["id"]
        data = requests.get("http://music.163.com/api/song/lyric?os=osx&id={}&lv=-1&kv=-1&tv=-1".format(song_id), headers={"User-Agent": user_agent}).json()

        if not "lrc" in data.keys():
            return None
        
        lyric = data["lrc"]["lyric"]
        translated_lyric = data["tlyric"]["lyric"]

        return {
            "source": lyric,
            "zh_CN": translated_lyric
        }

class QQMusicLP(LyricProvider):
    @staticmethod
    def fetch(artist, album, title):
        pass

providers = {
    "netease": NeteaseLP()
}
    
def fetch_lyric(model):
    for k in providers.keys():
        provider = providers[k]
        result = provider.fetch(" ".join(map(lambda x: x.name, model.artists)), model.album.name, model.title)

        if not result:
            continue
        
        for i in result:
            lyric = result[i]
            if lyric == "":
                continue
            
            lyric_model = Lyric(
                lyric=lyric,
                source=k,
                type="lrc",
                song=model,
                language=i
            )

            lyric_model.save()

        logger.info("Successfully fetch lyric for song `{0} - {1}` from {2}.", "/".join(map(lambda x: x.name, model.artists)), model.title, k)
        

@job.receiver("song_added")
def recevier(data): 
    model = data["model"]

    fetch_lyric(model)
