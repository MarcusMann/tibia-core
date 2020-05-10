from pytest import fixture
from tests.tools import load_mock


@fixture
def creatures_html():
    return load_mock("creatures.html")


@fixture
def creature_html():
    return load_mock("creature.html")
