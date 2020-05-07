import pytest

from tests.tools import load_mock


@pytest.fixture
def output_html():
    return load_mock("output.html")
