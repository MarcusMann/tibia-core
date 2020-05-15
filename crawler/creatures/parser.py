import base64

from bs4 import BeautifulSoup


class Parser:
    async def parse(self, creature, **kwargs):
        html = BeautifulSoup(creature.text, "html.parser")
        return {
            "name": self.extract_creature_name(html),
            "description": self.extract_creature_description(html),
            "image": await self.extract_creature_image(
                html, downloader=kwargs["downloader"]
            ),
        }

    def extract_creature_name(self, raw):
        print("Extracting name...")
        name = raw.select_one(".BoxContent h2")
        if name:
            return name.text

    def extract_creature_description(self, raw):
        print("Extracting description...")
        descriptions = raw.select(".BoxContent p")
        data = []

        for description in descriptions:
            data.append(description.text)
        return data

    async def extract_creature_image(self, raw, downloader):
        print("Extracting image...")
        image = raw.select_one(".BoxContent div:nth-of-type(2) div img")
        if image:
            response = await downloader.get(image["src"])
            return base64.b64encode(response.content)
