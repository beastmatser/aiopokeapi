from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from aiohttp import ClientSession


class HttpClient:
    _session: ClientSession
    inexistent_endpoints: List[str]
    base_url: str

    def __init__(self, *, session: Optional[ClientSession], base_url: str) -> None:
        self._session = session or ClientSession()
        self.inexistent_endpoints = []
        self.base_url = base_url

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()

    async def get(self, endpoint: str) -> Dict[str, Any]:
        if endpoint in self.inexistent_endpoints:
            raise ValueError(f"The id or name for {endpoint} was not found.")

        async with self._session.get(f"{self.base_url}/{endpoint}") as response:
            if response.status == 404:
                self.inexistent_endpoints.append(endpoint)
                raise ValueError(f"The id or name for {endpoint} was not found.")

            data: Dict[str, Any] = await response.json()
            return data
