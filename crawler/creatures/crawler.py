import re
from contextlib import suppress

import pymongo
from bs4 import BeautifulSoup

from .parser import Parser

GET_LINKS_REGEX = r"race"


class Crawler:
    def __init__(self, downloader, default_url: str, **kwargs):
        self.http = downloader
        self.default_url = default_url
        self.parser = Parser()
        self.kwargs = kwargs
        self.creatures = []

    async def download(self):
        response = await self.http.get(self.default_url)
        links = self.get_creatures_links(response)
        creatures = []

        with suppress(StopAsyncIteration):
            for link in links:
                creature = await self.http.get(link)
                data = self.parser.parse(creature)
                self.creatures.append(data)

    def save(self):
        client = pymongo.MongoClient("mongodb://db")
        collection = client.tibia.creatures
        collection.insert_many(self.creatures)

    def get_creatures_links(self, raw):
        data = []
        html = BeautifulSoup(raw.text, "html.parser")
        links = html.find_all("a", {"href": re.compile(GET_LINKS_REGEX)})
        for link in links:
            data.append(link["href"])
        return data
