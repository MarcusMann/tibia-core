from configparser import ConfigParser
from urllib.parse import urljoin
from crawler.downloader import Downloader

from . import crawler

config = ConfigParser()
config.read("config.ini")


class Crawler(crawler.Crawler):
    def __init__(self, param: str, downloader=Downloader(), **kwargs):
        super().__init__(
            downloader,
            urljoin(config.get("default", "default_url"), param),
            name=kwargs["name"],
        )

    async def init(self):
        return await self.download()
