from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from aiohttp import ClientSession


class HttpClient:
    def __init__(self, *, session: Optional[ClientSession]) -> None:
        self._session = session or ClientSession()
        self.inexistent_endpoints: List[str] = []

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()

    async def get(self, endpoint: str) -> Dict[str, Any]:
        async with self._session.get(
            f"https://pokeapi.co/api/v2/{endpoint}"
        ) as response:
            if endpoint in self.inexistent_endpoints:
                raise ValueError(f"The id or name for {endpoint} was not found.")

            if response.status == 404:
                self.inexistent_endpoints.append(endpoint)
                raise ValueError(f"The id or name for {endpoint} was not found.")

            data: Dict[str, Any] = await response.json()
            return data
