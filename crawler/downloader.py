from collections import namedtuple

import httpx


Response = namedtuple("Response", "text content status_code headers")


class Downloader:
    def __init__(self):
        self.downloader = httpx.AsyncClient()

    async def get(self, url: str):
        response = await self.downloader.get(url)

        return Response(
            text=response.text,
            content=response.content,
            status_code=response.status_code,
            headers=response.headers,
        )

    async def post(self, url):
        response = await self.downloader.post(url)

        return Response(
            text=response.text,
            content=response.content,
            status_code=response.status_code,
            headers=response.headers,
        )
