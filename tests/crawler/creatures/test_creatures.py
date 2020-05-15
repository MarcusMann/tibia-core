from unittest.mock import AsyncMock, patch

import pytest

from crawler.creatures.crawler import Crawler


@pytest.mark.asyncio
@patch("crawler.downloader.Downloader", new_callable=AsyncMock)
@patch("crawler.creatures.crawler.DB")
async def test_crawler(
    db_mock, downloader_mock, creatures_html, creature_html, data_regression
):
    default_url = "https://www.tibia.com/library/?subtopic=creatures"
    downloader = downloader_mock.return_value

    creatures_html = AsyncMock(text=creatures_html)
    creature_html = AsyncMock(text=creature_html)
    img = AsyncMock(content=b"tibia.jpg")

    downloader.get.side_effect = [creatures_html, creature_html, img]

    crawler = Crawler(downloader, default_url)
    await crawler.download()
    data_regression.check(crawler.creatures)
