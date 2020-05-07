from bs4 import BeautifulSoup

from crawler.character.parser import Parser


def test_extract_name(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    name = parsed.extract_name(html)
    data_regression.check({"name": name})


def test_extract_level(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    level = parsed.extract_level(html)
    data_regression.check({"level": level})


def test_extract_achievement_points(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    points = parsed.extract_achievement_points(html)
    data_regression.check({"points": points})


def test_extract_last_login(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    last_login = parsed.extract_last_login(html)
    data_regression.check({"last_login": last_login})


def test_extract_world(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    world = parsed.extract_world(html)
    data_regression.check({"world": world})


def test_extract_vocation(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    vocation = parsed.extract_vocation(html)
    data_regression.check({"vocation": vocation})


def test_extract_title(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    title = parsed.extract_title(html)
    data_regression.check({"title": title})


def test_extract_residence(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    residence = parsed.extract_residence(html)
    data_regression.check({"residence": residence})


def test_extract_account_status(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    account_status = parsed.extract_account_status(html)
    data_regression.check({"account_status": account_status})


def test_extract_sex(output_html, data_regression):
    parsed = Parser()
    html = BeautifulSoup(output_html, "html.parser")
    sex = parsed.extract_sex(html)
    data_regression.check({"sex": sex})
