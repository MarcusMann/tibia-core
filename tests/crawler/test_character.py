from unittest import mock
from crawler.character import Crawler
import pytest


@pytest.mark.asyncio
@mock.patch("crawler.downloader.Downloader", new_callable=mock.AsyncMock)
async def test_character_crawler(mock_downloader, data_regression, output_html):
    downloader = mock_downloader.return_value
    downloader.get.return_value = mock.AsyncMock(text=output_html)

    crawler = Crawler(downloader, "https://")
    response = await crawler.download()
    data_regression.check(response)
