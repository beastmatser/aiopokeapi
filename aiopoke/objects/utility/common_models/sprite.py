import os
from typing import Optional
from typing import TYPE_CHECKING

import aiofiles

if TYPE_CHECKING:
    from aiopoke.aiopoke_client import AiopokeClient


class Sprite:
    url: str
    bytes_: Optional[bytes]

    def __init__(self, url) -> None:
        self.url = url
        self.file_extention = url[url.rfind(".") + 1 :]  # noqa: E203
        self.bytes_ = None

    @classmethod
    def from_url(cls, url: Optional[str]) -> Optional["Sprite"]:
        if url is None:
            return None

        return cls(url)

    async def save(
        self, client: "AiopokeClient", *, path: Optional[str] = None
    ) -> None:
        if path is None:
            path = os.getcwd()

        elif not isinstance(path, str):
            raise TypeError("path must be a string")

        if path.split("/")[-1].__contains__("."):
            raise ValueError(
                "You can not set the file extension, this is to avoid file corruption. Use os.system() instead"
            )

        if self.bytes_ is None:
            bytes_ = await self.read(client)

        async with aiofiles.open(path + "/." + self.file_extention, "wb") as f:
            await f.write(bytes_)

    async def read(self, client: "AiopokeClient") -> bytes:
        session = await client._get_session()

        async with session.get(self.url) as response:
            bytes_: bytes = await response.read()
            self.bytes_ = bytes_

        return bytes_
