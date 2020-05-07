from collections import namedtuple
from typing import Dict

import httpx


Response = namedtuple("Response", "text content status_code headers")


class Downloader:
    def __init__(self):
        self.http = httpx.AsyncClient()

    async def get(self, url: str):
        response = await self.http.get(url)

        response.raise_for_status()

        return Response(
            text=response.text,
            content=response.content,
            status_code=response.status_code,
            headers=response.headers,
        )

    async def post(self, url: str, data: Dict[str, str]):
        response = await self.http.post(url, data=data)

        response.raise_for_status()

        return Response(
            text=response.text,
            content=response.content,
            status_code=response.status_code,
            headers=response.headers,
        )
