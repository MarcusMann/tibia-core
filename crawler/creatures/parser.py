from bs4 import BeautifulSoup


class Parser:
    def parse(self, creature, **kwargs):
        html = BeautifulSoup(creature.text, "html.parser")
        return {
            "name": self.extract_creature_name(html),
            "description": self.extract_creature_description(html),
            "image": self.extract_creature_image(html),
        }

    def extract_creature_name(self, raw):
        name = raw.select_one(".BoxContent h2")
        if name:
            return name.text

    def extract_creature_description(self, raw):
        descriptions = raw.select(".BoxContent p")
        data = []

        for description in descriptions:
            data.append(description.text)
        return data

    def extract_creature_image(self, raw):
        image = raw.select_one(".BoxContent img")
        if image:
            return image["src"]
