from unittest.mock import patch, AsyncMock
from crawler.character import Crawler
import pytest


@pytest.mark.asyncio
@patch("crawler.character.Downloader", new_callable=AsyncMock)
@patch("crawler.character.crawler.DB")
async def test_character_crawler(
    mock_db, mock_downloader, data_regression, output_html
):
    downloader = mock_downloader.return_value
    downloader.post.return_value = AsyncMock(text=output_html)

    crawler = Crawler("community/?subtopic=characters", downloader, name="hello")
    response = await crawler.init()
    data_regression.check(response)
