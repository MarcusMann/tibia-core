
class Crawler:
    def __init__(self, downloader, default_url: str):
        self.downloader = downloader
        self.default_url = default_url

    async def download(self):
        response = await self.downloader.get(self.default_url)
        return response