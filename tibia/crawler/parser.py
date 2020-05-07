import re
from bs4 import BeautifulSoup

GET_ACCOUNT_STATUS_REGEX = r"(Account\sStatus\:)"

class Parser:
    def parse(self, text, **kwargs):
        html = BeautifulSoup(text, "html.parser")

        return {
            "name": self.extract_name(html),
            "title": self.extract_title(html),
            "level": self.extract_level(html),
            "sex": self.extract_sex(html),
            "vocation": self.extract_vocation(html),
            "achievement_points": self.extract_achievement_points(html),
            "world": self.extract_world(html),
            "residence": self.extract_residence(html),
            "last_login": self.extract_last_login(html),
            "account_status": self.extract_account_status(html)
        }

    def extract_name(self, html):
        name = html.find("td", string="Name:")
        return self.normalize_information(name)
    
    def extract_title(self, html):
        title = html.find("td", string="Title:")
        return self.normalize_information(title)
   
    def extract_level(self, html):
        level = html.find("td", string="Level:")
        return self.normalize_information(level)
   
    def extract_sex(self, html):
        sex = html.find("td", string="Sex:")
        return self.normalize_information(sex)
    
    def extract_vocation(self, html):
        vocation = html.find("td", string="Vocation:")
        return self.normalize_information(vocation)

    def extract_achievement_points(self, html):
        points = html.find("td", string="Achievement Points:")
        return self.normalize_information(points)

    def extract_world(self, html):
        world = html.find("td", string="World:")
        return self.normalize_information(world)

    def extract_residence(self, html):
        residence = html.find("td", string="Residence:")
        return self.normalize_information(residence)

    def extract_last_login(self, html):
        last_login = html.find("td", string="Last Login:")
        return self.normalize_information(last_login)
    
    def extract_account_status(self, html):
        account_status = html.find("td", string=re.compile(GET_ACCOUNT_STATUS_REGEX))
        return self.normalize_information(account_status)

    
    def normalize_information(self, html):
        if html:
            return html.find_next("td").text.strip()
