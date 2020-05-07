from .parser import Parser


class Crawler:
    def __init__(self, downloader, default_url: str, **kwargs):
        self.http = downloader
        self.default_url = default_url
        self.parser = Parser()
        self.kwargs = kwargs

    async def download(self):
        response = await self.build_request(self.default_url)
        return self.parser.parse(response.text)

    async def build_request(self, default_url):
        response = await self.http.post(default_url, data={"name": self.kwargs["name"]})
        return response
