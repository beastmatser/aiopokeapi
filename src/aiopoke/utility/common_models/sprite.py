import aiofiles
import os
from typing import Optional


class Sprite:
    url: str
    bytes_: Optional[bytes]

    def __init__(self, url) -> None:
        self.url = url
        self.file_extention = url[url.rfind(".") + 1:]
        self.bytes_ = None

    @classmethod
    def from_url(cls, url: Optional[str]) -> Optional["Sprite"]:
        if url is None:
            return None

        return cls(url)

    async def save(self, *, path: Optional[str] = None) -> None:
        if path is None:
            path = os.getcwd()

        elif not isinstance(path, str):
            raise TypeError("path must be a string")

        if path.split("/")[-1].__contains__("."):
            raise ValueError(
                "You can not set the file extension, this is to avoid file corruption. Use os.system() instead"
            )

        from ...aiopoke_client import AiopokeClient  # type: ignore

        client = AiopokeClient()  # this will return an existing instance

        if self.bytes_ is None:
            bytes_ = await self.read(client)

        async with aiofiles.open(path + "/." + self.file_extention, "wb") as f:
            await f.write(bytes_)

    async def read(self) -> bytes:
        from ...aiopoke_client import AiopokeClient  # type: ignore

        client = AiopokeClient()  # this will return an existing instance

        async with client.session.get(self.url) as response:
            bytes_: bytes = await response.read()
            self.bytes_ = bytes_

        return bytes_
