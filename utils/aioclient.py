import contextlib
import json
from typing import Any

import aiohttp


class HTTPClient:
    def __init__(self):
        self.proxy: str | Any = None

    @contextlib.asynccontextmanager
    async def session(self):
        async with aiohttp.ClientSession() as session:
            yield session

    async def get(self, url, headers: dict = None, params=None, timeout: int = 10, proxy=None) -> Any:
        proxy = proxy if proxy else self.proxy
        params = params or {}
        async with self.session() as session:
            async with session.get(url, headers=headers, params=params, timeout=timeout, proxy=proxy) as response:
                return await response.json()

    async def post(self, url, headers: dict = None, data=None, timeout: int = 10, serializer=json.dumps,
                   proxy=None) -> Any:
        proxy = proxy if proxy else self.proxy
        async with self.session() as session:
            async with session.post(url, headers=headers, data=serializer(data), timeout=timeout,
                                    proxy=proxy) as response:
                return await response.json()

    async def put(self, url, headers: dict = None, data=None, timeout: int = 10, proxy=None,
                  serializer=json.dumps) -> Any:
        proxy = proxy if proxy else self.proxy
        serialized_data = serializer(data) if serializer else data
        async with self.session() as session:
            async with session.put(url, headers=headers, data=serialized_data, timeout=timeout,
                                   proxy=proxy) as response:
                return await response.json()
