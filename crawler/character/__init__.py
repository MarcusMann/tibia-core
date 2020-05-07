from .crawler import Crawler
from crawler.downloader import Downloader


class Tibia:
    def __init__(self, default_url: str):
        self.default_url = default_url
        self.downloader = Downloader()

    async def init(self):
        crawler = Crawler(self.downloader, self.default_url)
        return await crawler.download()
