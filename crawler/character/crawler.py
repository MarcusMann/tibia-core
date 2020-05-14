from .parser import Parser
from db import DB


class Crawler:
    def __init__(self, downloader, default_url: str, **kwargs):
        self.http = downloader
        self.default_url = default_url
        self.parser = Parser()
        self.kwargs = kwargs

    async def download(self):
        response = await self.build_request(self.default_url)
        character = self.parser.parse(response.text)

        with DB() as database:
            database.characters.insert(character)
            print(f"{character['name']} has been saved!")
        return character

    async def build_request(self, default_url):
        response = await self.http.post(default_url, data={"name": self.kwargs["name"]})
        return response
