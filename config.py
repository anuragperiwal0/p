import os
import logging
class Config:

    API_ID = int(os.environ.get("API_ID", "10683462"))
    API_HASH = os.environ.get("API_HASH", "8ab812d6e6849bd6352dcb731e44c31e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5984638204:AAG2oTXKedFkRfnR1MftvOIsKUrMhpXVits")
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT")
    OWNER_ID = os.environ.get("OWNER_ID", "5543917190")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://anurag:xC6QOmRI7j9i8yj6@anurag.co63n.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","anurag")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'anurag_data')
    SESSION = os.environ.get("SESSION", "BQA_gnpuaHgmzC8Hkp55qtx7e2J6ZVD6v9jQK7oZAuCwGS7BCzL2YHJXB8RqfGQngKMdIqauzrDGv3Ou1ccjcnbGIU9_u7CE3rbFDYlCFDMZYJMO9Jbo6VUQzuxMrenXJE8hKxKkyX-U-8pUsi_QiMhaF2DJNkAaDylqn0x3G0BhzRT31rkevI9M5q37kOLa7l3LO5gNEUnVdup91eRCVh26T5-qCW8ozLS8LW1BTK_HnYRwytgpMVg7z9fPSUixFvq4DD8NiW9gyjmZ3R8Ik5RPcFGMWBbZLPLcQCnoaETTrfAkpVPkbJJxg8hkkgUhHoIRLzYjFij2zh3oXOmHYjPRAAAAAVLdr70A")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001787652537"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "forwardro_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
