from unittest.mock import patch, AsyncMock
import pytest
from crawler.creatures.crawler import Crawler


@pytest.mark.asyncio
@patch("crawler.downloader.Downloader", new_callable=AsyncMock)
async def test_crawler(downloader_mock, creatures_html, creature_html, data_regression):
    default_url = "https://www.tibia.com/library/?subtopic=creatures"
    downloader = downloader_mock.return_value

    creatures_html = AsyncMock(text=creatures_html)
    creature_html = AsyncMock(text=creature_html)

    downloader.get.side_effect = [creatures_html, creature_html]

    crawler = Crawler(downloader, default_url)
    response = await crawler.download()
    data_regression.check(crawler.get_creatures)
