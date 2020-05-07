from .parser import Parser


class Crawler:
    def __init__(self, downloader, default_url: str):
        self.downloader = downloader
        self.default_url = default_url
        self.parser = Parser()

    async def download(self):
        response = await self.downloader.get(self.default_url)
        return self.parser.parse(response.text)
