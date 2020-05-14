from pymongo import MongoClient
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")


class DB:
    def __init__(self):
        self.session = None

    def __enter__(self):
        _host = config.get("default", "host")
        _port = config.get("default", "port")

        if self.session is not None:
            raise RuntimeError("Already connected")
        self.session = MongoClient(f"mongodb://{_host}:{_port}")
        return self.session.tibia

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None
