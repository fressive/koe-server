import importlib
import os

from loguru import logger
from functools import wraps
from util.channel import chan
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def receiver(channel):
    def decorator(func):
        chan.subscribe(channel, func)
    return decorator

for i in os.listdir("job"):
    splits = i.split(".")

    if splits[0] != "__init__" and splits[-1] == "py":
        logger.info("Job `{0}` loaded", splits[0])
        importlib.import_module("job." + splits[0])

scheduler.start()
